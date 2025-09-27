#
# Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import math
from typing import Any, Callable, List

import numpy as np
import onnx

from quark.shares.utils.log import ScreenLogger

from .quant_utils import (
    COP_DOMAIN,
    COP_IN_OP_NAME,
    HARD_SIGMOID_SCALE,
    check_hard_sigmoid_condition,
    dpu_leaky_relu_alpha,
    get_clip_min_max,
    remove_nodes,
)
from .simulate_dpu_softmax import SimulateDPUSoftmax

logger = ScreenLogger(__name__)


class SimulateDPU:
    def __init__(
        self,
        model: onnx.ModelProto,
        should_quantize_node: Callable[[Any], bool],
        nodes_to_quantize: list[str],
        nodes_to_exclude: list[str],
    ):
        self.model = model
        self.should_quantize_node = should_quantize_node
        self.nodes_to_quantize = nodes_to_quantize
        self.nodes_to_exclude = nodes_to_exclude

    def should_simulate_node(self, node: onnx.NodeProto) -> bool:
        if (
            self.nodes_to_quantize is not None
            and len(self.nodes_to_quantize) != 0
            and node.name not in self.nodes_to_quantize
        ):
            return False

        if self.nodes_to_exclude is not None and node.name in self.nodes_to_exclude:
            return False

        return True

    def insert_mul(self, node: onnx.NodeProto, scale: float) -> None:
        constant_node = onnx.helper.make_node(
            "Constant",
            inputs=[],
            outputs=[node.output[0] + "_Scale"],
            value=onnx.helper.make_tensor("scale", onnx.TensorProto.FLOAT, [], [scale]),
        )
        mul_tensor = node.output[0] + "_Mul"
        mul_node = onnx.helper.make_node(
            "Mul", inputs=[mul_tensor, node.output[0] + "_Scale"], outputs=[node.output[0]], name=mul_tensor
        )
        self.model.graph.node.extend([constant_node, mul_node])
        if not node.name:
            node.name = node.output[0]
        node.output[0] = mul_tensor

    def convert_leaky_relu_to_dpu_version(self) -> None:
        """Convert LeakyReLU to DPU version.
        LeakyReLU(alpha) --> LeakyReLU(round(alpha*256)/256)
        """
        for node in self.model.graph.node:
            if node.op_type == "LeakyRelu" and self.should_quantize_node(node):
                alpha_attr = next((attr for attr in node.attribute if attr.name == "alpha"), None)
                if alpha_attr:
                    ori_alpha = alpha_attr.f
                    dpu_alpha = dpu_leaky_relu_alpha(alpha_attr.f)
                    alpha_attr.f = dpu_alpha
                    logger.info(
                        f"Found Leaky ReLU node {node.name} with alpha={ori_alpha}. "
                        f"Replacing with new alpha={dpu_alpha}."
                    )

    def convert_sigmoid_to_hard_sigmoid(self) -> None:
        """Convert Sigmoid to HardSigmoid."""
        nodes_to_remove = []
        for node in self.model.graph.node:
            if node.op_type == "Sigmoid" and self.should_quantize_node(node):
                hard_sigmoid_node = onnx.helper.make_node(
                    "HardSigmoid", inputs=node.input, outputs=node.output, name=node.name
                )
                hard_sigmoid_alpha = onnx.helper.make_attribute("alpha", 1.0 / 6.0)
                hard_sigmoid_node.attribute.append(hard_sigmoid_alpha)
                self.model.graph.node.append(hard_sigmoid_node)
                nodes_to_remove.append(node)
                logger.info(f"Found Sigmoid node {node.name}. Replacing with HardSigmoid.")
        self.model = remove_nodes(self.model, nodes_to_remove)

    def convert_hard_sigmoid_to_dpu_version(self) -> None:
        """Convert HardSigmoid to DPU version."""
        for node in self.model.graph.node:
            if node.op_type == "HardSigmoid" and check_hard_sigmoid_condition(node) and self.should_simulate_node(node):
                self.insert_mul(node, HARD_SIGMOID_SCALE)
                logger.info(f"Found HardSigmoid node {node.name} with alpha={1.0 / 6.0}. Convert to DPU version.")

    def convert_avg_pool_to_dpu_version(self) -> None:
        """Convert AveragePool to DPU version."""

        def _get_avgpool_scale(kh: int, kw: int) -> Any:
            if kh > 255 or kw > 255:
                return 1.0
            elif kh == 3 and kw == 3:
                return 9.0 * 7.0 / 64.0
            elif kh == 5 and kw == 5:
                return 25.0 * 10.0 / 256.0
            elif kh == 6 and kw == 6:
                return 36.0 * 7.0 / 256.0
            elif kh == 7 and kw == 7:
                return 49.0 * 21.0 / 1024.0
            elif kh == 14 and kw == 14:
                return 196.0 * 21.0 / 4096.0
            else:
                rec = kw * kh
                n_max = 7 + math.ceil(math.log2(rec))
                ns = range(0, n_max)
                ns_pow = [2**n for n in ns]
                ks = [round(ns_p / rec) for ns_p in ns_pow]
                diffs = [abs(k / ns_p - 1 / rec) for k, ns_p in zip(ks, ns_pow, strict=False)]
                n = diffs.index(min(diffs))
                k = ks[n]
                scale = k / 2**n
                scale *= rec
                return scale

        for node in self.model.graph.node:
            if node.op_type in ["AveragePool", "GlobalAveragePool"] and self.should_quantize_node(node):
                is_global_avg_pool = node.op_type == "GlobalAveragePool"
                input_name = node.input[0]
                for n1 in self.model.graph.node:
                    if n1.output[0] == input_name:
                        if n1.op_type == "DequantizeLinear":
                            input_name = n1.input[0]
                            for n2 in self.model.graph.node:
                                if n2.output[0] == input_name:
                                    input_name = n2.input[0]
                                    break
                        else:
                            break
                input_shape = None
                shape_to_check = False
                kh = 0
                kw = 0
                if is_global_avg_pool:
                    for input_info in self.model.graph.value_info:
                        if input_info.name == input_name:
                            input_shape = [dim.dim_value for dim in input_info.type.tensor_type.shape.dim]
                            if len(input_shape) == 4 and input_shape[2] == input_shape[3]:
                                shape_to_check = True
                                kh = input_shape[2]
                                kw = input_shape[3]
                            break
                    if not input_shape:
                        logger.warning(
                            f"Failed to get the input shape of GlobalAveragePool {node.name}, skip simulating DPU behavior."
                        )
                        continue
                else:
                    kernel_shape_attr = next((attr for attr in node.attribute if attr.name == "kernel_shape"), None)
                    if kernel_shape_attr:
                        kernel_shape = kernel_shape_attr.ints
                        if len(kernel_shape) == 2 and kernel_shape[0] == kernel_shape[1]:
                            shape_to_check = True
                            kh = kernel_shape[0]
                            kw = kernel_shape[1]

                if shape_to_check and (kh * kw > 0):
                    scale = _get_avgpool_scale(kh, kw)
                    self.insert_mul(node, scale)
                    logger.info(f"Rescale {node.op_type} {node.name} with factor {scale} to simulate DPU behavior.")
                else:
                    logger.warning(f"Do not support rescale {node.op_type} {node.name} to simulate DPU behavior.")

    def convert_reduce_mean_to_dpu_version(self) -> None:
        """Convert ReduceMean to DPU version."""

        def _get_reduce_mean_scale(rec: int) -> Any:
            n_max = 7 + math.ceil(math.log2(rec))
            ns = range(0, n_max)
            ns_pow = [2**n for n in ns]
            ks = [round(ns_p / rec) for ns_p in ns_pow]
            diffs = [abs(k / ns_p - 1 / rec) for k, ns_p in zip(ks, ns_pow, strict=False)]
            n = diffs.index(min(diffs))
            k = ks[n]
            scale = k / 2**n
            scale *= rec
            return scale

        for node in self.model.graph.node:
            if node.op_type in ["ReduceMean"] and self.should_quantize_node(node):
                input_name = node.input[0]
                input_shape = None
                for n1 in self.model.graph.node:
                    if n1.output[0] == input_name:
                        if n1.op_type == "DequantizeLinear":
                            input_name = n1.input[0]
                            for n2 in self.model.graph.node:
                                if n2.output[0] == input_name:
                                    input_name = n2.input[0]
                                    break
                        else:
                            break
                for input_info in self.model.graph.value_info:
                    if input_info.name == input_name:
                        input_shape = [dim.dim_value for dim in input_info.type.tensor_type.shape.dim]
                axes = None
                if len(node.input) == 1:
                    for attr in node.attribute:
                        if attr.name == "axes":
                            axes = attr.ints
                elif len(node.input) == 2:
                    for init in self.model.graph.initializer:
                        if init.name == node.input[1]:
                            axes = onnx.numpy_helper.to_array(init).tolist()

                if axes is not None and input_shape is not None and len(input_shape) > 0:
                    rec = 1
                    for i in axes:
                        rec *= input_shape[i]
                    if isinstance(rec, int) and rec > 0:
                        scale = _get_reduce_mean_scale(rec)
                        self.insert_mul(node, scale)
                        logger.info(f"Rescale {node.op_type} {node.name} with factor {scale} to simulate DPU behavior.")
                    else:
                        logger.warning(
                            f"Do not support rescale {node.op_type} {node.name} to simulate DPU behavior."
                            f"Please check axes: {axes} and input shape: {input_shape}."
                        )
                else:
                    logger.warning(
                        f"Do not support rescale {node.op_type} {node.name} to simulate DPU behavior. Please check axes and input shape."
                    )

    def convert_softmax_to_dpu_version(self) -> None:
        """Convert Softmax to DPU version."""

        def get_opset_version(model: onnx.ModelProto) -> Any:
            ai_onnx_domain = [opset for opset in model.opset_import if not opset.domain or opset.domain == "ai.onnx"]
            if len(ai_onnx_domain) != 1:
                raise ValueError("Failed to find proper ai.onnx domain")
            opset_version = ai_onnx_domain[0].version
            return opset_version

        nodes = []

        for node in self.model.graph.node:
            if node.op_type == "Softmax" and self.should_quantize_node(node):
                nodes.append(node)

        opset_version = get_opset_version(self.model)
        for node in nodes:
            new_nodes = SimulateDPUSoftmax(opset_version=opset_version).simulate(
                node
            )  # several nodes simulate a softmax

            if len(new_nodes):
                self.model.graph.node.remove(node)
                self.model.graph.node.extend(new_nodes)

                self.nodes_to_exclude.extend(new_nodes[:-1])
                logger.info(f"Softmax {node.name} to simulate DPU behavior under opset {opset_version}.")
            else:
                logger.warning(f"Softmax {node.name} to simulate DPU behavior under opset {opset_version} failed.")

    def convert_instance_norm_to_dpu_version(self) -> None:
        """Convert Instance Normalization to DPU version."""
        nodes_to_remove = []
        nodes_to_add = []
        for node in self.model.graph.node:
            if node.op_type == "InstanceNormalization" and self.should_quantize_node(node):
                epsilon = next((attr.f for attr in node.attribute if attr.name == "epsilon"), 1e-05)
                new_node = onnx.helper.make_node(
                    COP_IN_OP_NAME,
                    node.input,
                    node.output,
                    domain=COP_DOMAIN,
                    name=node.name,
                    epsilon=epsilon,
                )
                nodes_to_remove.append(node)
                nodes_to_add.append(new_node)
                logger.info(f"InstanceNormalization node {node.name} to simulate DPU behavior by {new_node.op_type}.")
        self.model = remove_nodes(self.model, nodes_to_remove)
        self.model.graph.node.extend(nodes_to_add)

    def convert_clip_to_dpu_version(self) -> None:
        """Convert Clip to DPU version."""
        nodes_to_remove: list[Any] = []
        nodes_to_add: list[Any] = []
        for node in self.model.graph.node:
            if node.op_type == "Clip" and self.should_quantize_node(node):
                min_value, max_value, para_type = get_clip_min_max(self.model, node)

                if para_type != 1:  # Get from initializers
                    logger.warning(
                        f"The min and max of Clip node '{node.name}' are not initializers, conversion to the DPU version is not supported yet."
                    )
                    continue

                if min_value is not None:
                    min_value = max(-128, min(127, round(min_value)))
                    new_min_value = np.array(min_value, dtype=np.float32)
                    for initializer in self.model.graph.initializer:
                        if initializer.name == node.input[1]:
                            new_tensor = onnx.numpy_helper.from_array(new_min_value, name=node.input[1])
                            initializer.CopyFrom(new_tensor)
                            break
                elif min_value is None:
                    assert node.input[1] == "" and node.attribute == []
                    min_value = -128
                    new_min_value = np.array(min_value, dtype=np.float32)
                    new_weight_name = node.name + "_dpu_min"
                    node.input[1] = new_weight_name
                    new_weight_tensor = onnx.numpy_helper.from_array(new_min_value, name=new_weight_name)
                    self.model.graph.initializer.append(new_weight_tensor)

                if max_value is not None:
                    max_value = max(-128, min(127, round(max_value)))
                    new_max_value = np.array(max_value, dtype=np.float32)
                    for initializer in self.model.graph.initializer:
                        if initializer.name == node.input[2]:
                            new_tensor = onnx.numpy_helper.from_array(new_max_value, name=node.input[2])
                            initializer.CopyFrom(new_tensor)
                            break
                elif max_value is None:
                    assert node.input[2] == "" and node.attribute == []
                    max_value = 127
                    new_max_value = np.array(max_value, dtype=np.float32)
                    new_weight_name = node.name + "_dpu_max"
                    node.input[2] = new_weight_name
                    new_weight_tensor = onnx.numpy_helper.from_array(new_max_value, name=new_weight_name)
                    self.model.graph.initializer.append(new_weight_tensor)

                logger.info(
                    f"Clip node '{node.name}' is converted to DPU version, min is {new_min_value}, max is {new_max_value}."
                )


def simulate_transforms(
    model: onnx.ModelProto,
    should_quantize_node: Callable[[Any], bool],
    nodes_to_quantize: list[str],
    nodes_to_exclude: list[str],
    convert_leaky_relu_to_dpu_version: bool = True,
    convert_sigmoid_to_hard_sigmoid: bool = True,
    convert_hard_sigmoid_to_dpu_version: bool = True,
    convert_avg_pool_to_dpu_version: bool = True,
    convert_reduce_mean_to_dpu_version: bool = True,
    convert_softmax_to_dpu_version: bool = True,
    convert_instance_norm_to_dpu_version: bool = True,
    convert_clip_to_dpu_version: bool = True,
) -> tuple[onnx.ModelProto, list[str]]:
    """Transforming models to meet the DPU constraints."""

    simulate_dpu = SimulateDPU(model, should_quantize_node, nodes_to_quantize, nodes_to_exclude)

    if convert_leaky_relu_to_dpu_version:
        simulate_dpu.convert_leaky_relu_to_dpu_version()

    if convert_sigmoid_to_hard_sigmoid:
        simulate_dpu.convert_sigmoid_to_hard_sigmoid()

    if convert_hard_sigmoid_to_dpu_version:
        simulate_dpu.convert_hard_sigmoid_to_dpu_version()

    if convert_avg_pool_to_dpu_version:
        simulate_dpu.convert_avg_pool_to_dpu_version()

    if convert_reduce_mean_to_dpu_version:
        simulate_dpu.convert_reduce_mean_to_dpu_version()

    if convert_softmax_to_dpu_version:
        simulate_dpu.convert_softmax_to_dpu_version()

    if convert_instance_norm_to_dpu_version:
        simulate_dpu.convert_instance_norm_to_dpu_version()

    if convert_clip_to_dpu_version:
        simulate_dpu.convert_clip_to_dpu_version()

    return simulate_dpu.model, simulate_dpu.nodes_to_exclude

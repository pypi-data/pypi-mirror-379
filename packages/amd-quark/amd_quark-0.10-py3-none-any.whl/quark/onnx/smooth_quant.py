#
# Copyright (C) 2024, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
import copy
import os
from collections import OrderedDict
from typing import Any, Dict, List, Tuple

import numpy as np
import onnx
import onnxruntime
import torch
from onnx import helper, numpy_helper, onnx_pb
from onnxruntime.transformers.onnx_model import OnnxModel
from tqdm.auto import tqdm

from quark.onnx.quant_utils import create_infer_session_for_onnx_model

from .quant_utils import create_tmp_dir


class SmoothQuant:
    """
    A class for model smooth
    Args:
        input_model (onnx.ModelProto): The ONNX model to be smoothed.
        dataloader (torch.utils.data.DataLoader): The dataloader used for calibrate.
        alpha (float): The extent to which the difficulty of quantification is shifted from activation to weighting.
        use_external_data_format (bool): True if the model size is larger than 2GB.
    """

    def __init__(
        self,
        input_model: onnx.ModelProto,
        dataloader: torch.utils.data.DataLoader,  # type:ignore
        alpha: float,
        use_external_data_format: bool = False,
        providers: list[str] = ["CPUExecutionProvider"],
    ):
        self.dataloader = dataloader
        self.alpha = alpha
        self.use_external_data_format = use_external_data_format
        self.providers = providers

        self.base_dir = create_tmp_dir(prefix="quark_onnx.sq.").name
        if self.use_external_data_format:
            for prop in input_model.metadata_props:
                if prop.key == "cache_path":
                    self.base_dir = prop.value
        self.smoothed_model_path = os.path.join(self.base_dir, "decoder_model_smoothed.onnx")

        self.model = copy.deepcopy(input_model) if use_external_data_format else input_model
        self.onnx_model = OnnxModel(self.model)

        self.output_num = len(self.onnx_model.get_graphs_output_names())

        self.linear_dic: dict[str, list[onnx.NodeProto]] = {}
        self.ln_outputs: list[str] = []
        self.act_scales: dict[str, np.ndarray[Any, np.dtype[np.float32]]] = {}
        self.extend_output_nodes: list[str] = []
        self.smooth_nodes: list[str] = []

    def match_matmul_output(self) -> None:
        matmul_node_list = self.onnx_model.get_nodes_by_op_type("MatMul")
        smooth_matmul_node_list = []
        # determine whether matmul op has parameters
        for node in matmul_node_list:
            for init in self.onnx_model.model.graph.initializer:
                if init.name == node.input[1]:
                    smooth_matmul_node_list.append(node)
        for node in smooth_matmul_node_list:
            if node.input[0] not in self.ln_outputs:
                self.ln_outputs.append(node.input[0])
                self.model.graph.output.extend([onnx.ValueInfoProto(name=node.input[0])])
                self.extend_output_nodes.append(node.input[0])
            if node.input[0] not in self.linear_dic:
                self.linear_dic[node.input[0]] = [node]
            else:
                self.linear_dic[node.input[0]].append(node)

    def get_act_scale(self) -> None:
        sess_options = onnxruntime.SessionOptions()
        sess_options.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL
        session = create_infer_session_for_onnx_model(
            self.onnx_model.model,
            sess_options=sess_options,
            providers=self.providers,
            use_external_data_format=self.use_external_data_format,
        )
        # calculate act_scale
        for inputs in tqdm(self.dataloader):
            inputs_dict = inputs
            ort_outs = session.run(self.ln_outputs, inputs_dict)
            out_dict = OrderedDict(zip(self.ln_outputs, ort_outs, strict=False))

            for output in self.ln_outputs:
                hidden_dim = out_dict[output].shape[-1]
                tensor = np.absolute(out_dict[output].reshape(-1, hidden_dim))
                comming_max = np.max(tensor, axis=0)
                if output in self.act_scales:
                    self.act_scales[output] = np.where(
                        self.act_scales[output] > comming_max, self.act_scales[output], comming_max
                    )
                else:
                    self.act_scales[output] = comming_max

    def get_initializer_tensor(self, init_name: str) -> tuple[onnx.TensorProto, np.ndarray[Any, np.dtype[np.float32]]]:
        weight_tensor_proto = [init for init in self.onnx_model.model.graph.initializer if init.name == init_name][0]
        weight_tensor = numpy_helper.to_array(weight_tensor_proto, self.base_dir)
        return weight_tensor_proto, weight_tensor

    def smooth_ln_linear(self) -> None:
        for output in self.ln_outputs:
            linear = self.linear_dic[output]
            act_scale = self.act_scales[output]

            # calculate weight scale
            # linear in attention
            for node in linear:
                linear_weight_init, linear_weight = self.get_initializer_tensor(node.input[1])
                weight_scale = np.max(abs(linear_weight), axis=1)
                scale = np.power(act_scale, self.alpha) / np.power(weight_scale + 1e-9, (1 - self.alpha))
                self.insert_smooth_mul_op(scale, output, node)
                linear_weight = np.multiply(scale.reshape(-1, 1), linear_weight)
                linear_weight_init.CopyFrom(numpy_helper.from_array(linear_weight, linear_weight_init.name))

    def insert_smooth_mul_op(
        self, scale: np.ndarray[Any, np.dtype[np.float32]], input_name: str, node: onnx.NodeProto
    ) -> None:
        scale_factor = 1.0 / (scale + 1e-9)

        scale_tensor = helper.make_tensor(
            name=input_name + "_" + node.name + "_" + "smooth_scale",
            data_type=onnx_pb.TensorProto.FLOAT,
            dims=scale_factor.shape,
            vals=scale_factor.flatten().tolist(),
        )

        self.mul_output_name = input_name + "_" + node.name + "_smooth_output"
        mul_node = helper.make_node(
            "Mul",
            inputs=[input_name, input_name + "_" + node.name + "_" + "smooth_scale"],
            outputs=[self.mul_output_name],
            name=input_name + "_" + node.name + "_smooth_mul",
        )
        self.smooth_nodes.append(mul_node.name)

        self.onnx_model.add_node(mul_node)
        self.onnx_model.add_initializer(scale_tensor)
        self.onnx_model.remove_node(node)
        self.onnx_model.replace_node_input(node, node.input[0], self.mul_output_name)
        self.onnx_model.add_node(node)

    def remove_extend_output_node(self) -> None:
        for node in self.extend_output_nodes:
            if onnx.ValueInfoProto(name=node) in self.model.graph.output:
                self.model.graph.output.remove(onnx.ValueInfoProto(name=node))

    def transform(self) -> None:
        self.match_matmul_output()
        self.get_act_scale()
        self.smooth_ln_linear()
        self.remove_extend_output_node()

    def get_smooth_node(self) -> list[str]:
        return self.smooth_nodes

    def get_smooth_path(self) -> str:
        self.onnx_model.save_model_to_file(
            self.smoothed_model_path,
            use_external_data_format=self.use_external_data_format,
            all_tensors_to_one_file=True,
        )
        return self.smoothed_model_path

    def get_smooth_model(self) -> onnx.ModelProto:
        return self.onnx_model.model  # type:ignore


def smooth_transforms(
    input_model: onnx.ModelProto,
    dataloader: torch.utils.data.DataLoader,  # type:ignore
    alpha: float = 0.5,
    use_external_data_format: bool = False,
) -> onnx.ModelProto:
    smooth_ = SmoothQuant(input_model, dataloader, alpha=alpha, use_external_data_format=use_external_data_format)
    smooth_.transform()
    return smooth_.get_smooth_model()

#
# Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
import itertools
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union

import numpy as np
import onnx
import onnxruntime
from onnx import ModelProto, TensorProto, numpy_helper
from onnxruntime.quantization.calibrate import CalibrationMethod
from onnxruntime.quantization.onnx_model import ONNXModel
from onnxruntime.quantization.quant_utils import (
    QuantType,
    load_model_with_shape_infer,
    save_and_reload_model_with_shape_infer,
)

from quark.onnx.calibration import CachedDataReader, PowerOfTwoMethod
from quark.onnx.quant_utils import (
    ExtendedQuantType,
    create_infer_session_for_onnx_model,
    dequantize_data,
    get_output_nodes_of_node,
    get_tensor_type_from_qType,
    inference_sub_model_with_data,
    quantize_data,
)
from quark.shares.utils.log import ScreenLogger

logger = ScreenLogger(__name__)


class BiasCorrection:
    def __init__(self, quant_model: ModelProto, use_external_data_format: bool, execution_providers: list[str]) -> None:
        self.quant_model = quant_model
        self.augmented_quant_model: ModelProto
        self.target_type = ["Conv", "Gemm"]
        self.use_external_data_format = use_external_data_format
        self.execution_providers = execution_providers
        self.origin_intermediate_outputs: list[str] = []
        self.quant_intermediate_outputs: list[str] = []

    def select_tensors_to_calibrate(self, model: onnx.ModelProto) -> tuple[set[str], dict[str, onnx.ValueInfoProto]]:
        """
        select all quantization_candidates op type nodes' input/output tensors.
        returns:
            tensors (set): set of tensor name.
            value_infos (dict): tensor name to value info.
        """
        value_infos = {vi.name: vi for vi in model.graph.value_info}
        value_infos.update({ot.name: ot for ot in model.graph.output})
        value_infos.update({it.name: it for it in model.graph.input})
        initializer = {init.name for init in model.graph.initializer}

        tensors_to_calibrate = set()
        tensor_type_to_calibrate = {TensorProto.FLOAT, TensorProto.FLOAT16}

        for node in model.graph.node:
            if node.op_type in ["Conv", "Gemm"]:
                for tensor_name in itertools.chain(node.input, node.output):
                    if tensor_name in value_infos:
                        vi = value_infos[tensor_name]
                        if (
                            vi.type.HasField("tensor_type")
                            and vi.type.tensor_type.elem_type in tensor_type_to_calibrate
                            and tensor_name not in initializer
                        ):
                            tensors_to_calibrate.add(tensor_name)

        return tensors_to_calibrate, value_infos

    def get_bias_corr_pattern_augment_graph(self) -> tuple[dict[str, tuple[str, str, str | None]], set[str]]:
        """
        make all quantization_candidates op type nodes as part of the graph output.
        """
        node_bias_corr_output_map = {}
        model = self.quant_model

        tensors_to_calibrate, value_infos = self.select_tensors_to_calibrate(model)
        model_original_outputs = set(output.name for output in model.graph.output)
        linear_and_quant_node_type = ["Relu", "Clip", "QuantizeLinear", "DequantizeLinear"]
        all_sub_model_in_out = []
        for node in model.graph.node:
            sub_model_input = None
            sub_model_output = None
            if node.op_type in self.target_type:
                sub_model_input = node.input[0]
                sub_model_output = node.output[0]
                node_output_nodes1 = get_output_nodes_of_node(node, model.graph)
                while node_output_nodes1:
                    if node_output_nodes1[0].op_type in linear_and_quant_node_type:
                        sub_model_output = node_output_nodes1[0].output[0]
                        inter_node = node_output_nodes1[0]
                        node_output_nodes1 = get_output_nodes_of_node(inter_node, model.graph)
                    else:
                        break
                logger.debug(f"node: {node.name}, output: {sub_model_output}")
                bias_tensor_name = None
                if len(node.input) == 3:
                    bias_tensor_name = node.input[2]
                node_bias_corr_output_map[node.name] = (sub_model_input, sub_model_output, bias_tensor_name)
                if sub_model_input not in all_sub_model_in_out:
                    all_sub_model_in_out.append(sub_model_input)
                if sub_model_output not in all_sub_model_in_out:
                    all_sub_model_in_out.append(sub_model_output)
        for inter_output in all_sub_model_in_out:
            if inter_output not in model_original_outputs:
                logger.debug(f"output:{value_infos[inter_output]}")
                model.graph.output.append(value_infos[inter_output])
        onnx_model = ONNXModel(model)
        onnx_model.topological_sort()

        self.augmented_quant_model = onnx_model.model
        return node_bias_corr_output_map, tensors_to_calibrate

    def augment_origin_quant_graph(self) -> tuple[dict[str, tuple[str, str, str | None]], set[str]]:
        quant_bc_pattern, quant_tensors_to_bc = self.get_bias_corr_pattern_augment_graph()
        return quant_bc_pattern, quant_tensors_to_bc

    def create_inference_session(self, model: onnx.ModelProto) -> onnxruntime.InferenceSession:
        """
        create an OnnxRuntime InferenceSession.
        """
        sess_options = onnxruntime.SessionOptions()
        sess_options.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_DISABLE_ALL
        return create_infer_session_for_onnx_model(
            model,
            sess_options=sess_options,
            providers=self.execution_providers,
            use_external_data_format=self.use_external_data_format,
        )

    def collect_data(
        self, data_reader: CachedDataReader, infer_session: onnxruntime.InferenceSession, tensors_to_bc: set[str]
    ) -> tuple[dict[Any, Any], list[Any]]:
        data_reader.reset_iter()
        intermediate_outputs = []
        while True:
            inputs = data_reader.get_next()
            if not inputs:
                break
            intermediate_outputs.append(infer_session.run(None, inputs))

        if len(intermediate_outputs) == 0:
            logger.warning("No data is collected.")

        output_names = [infer_session.get_outputs()[i].name for i in range(len(intermediate_outputs[0]))]
        output_dicts_list = [
            dict(zip(output_names, intermediate_output, strict=False)) for intermediate_output in intermediate_outputs
        ]
        merged_dict: dict[Any, Any] = {}
        for d in output_dicts_list:
            for k, v in d.items():
                merged_dict.setdefault(k, []).append(v)

        clean_merged_dict = dict((i, merged_dict[i]) for i in merged_dict)
        #                         if i in tensors_to_bc)
        return clean_merged_dict, intermediate_outputs


def bias_correction(
    fmodel_input: Union[str, Path, onnx.ModelProto],
    qmodel_input: Union[str, Path, onnx.ModelProto],
    use_external_data_format: bool,
    calibration_data_reader: CachedDataReader,
    activation_type: Union[QuantType, ExtendedQuantType],
    calibrate_method: Union[PowerOfTwoMethod, CalibrationMethod],
    extra_options: dict[str, Any],
    execution_providers: list[str] = ["CPUExecutionProvider"],
) -> Any:
    logger.info("Start the Bias Correction processing ...")

    float_model = fmodel_input if isinstance(fmodel_input, onnx.ModelProto) else onnx.load(fmodel_input)
    if isinstance(qmodel_input, onnx.ModelProto):
        if use_external_data_format:
            quant_model = save_and_reload_model_with_shape_infer(qmodel_input)
        else:
            quant_model = onnx.shape_inference.infer_shapes(qmodel_input)
    else:
        quant_model = load_model_with_shape_infer(Path(qmodel_input))

    topo_model = ONNXModel(float_model)
    topo_model.topological_sort()
    model = topo_model.model

    bias_corr = BiasCorrection(quant_model, use_external_data_format, execution_providers)
    quant_bc_pattern, quant_tensors_bc = bias_corr.augment_origin_quant_graph()

    bias_corr.execution_providers = execution_providers
    quant_infer_session = bias_corr.create_inference_session(bias_corr.augmented_quant_model)
    quant_clean_merged_dict, _ = bias_corr.collect_data(calibration_data_reader, quant_infer_session, quant_tensors_bc)
    quant_output_tensor_node_map = {}
    activation_type = get_tensor_type_from_qType(activation_type)
    # get all output tensor name to node obj

    for node in quant_model.graph.node:
        for out in node.output:
            quant_output_tensor_node_map[out] = node
    # get all weight name to obj map
    quant_initializer_name_map = {}
    for init in quant_model.graph.initializer:
        quant_initializer_name_map[init.name] = init
    # get all node name to obj map
    float_node_obj_map = {}
    for node in model.graph.node:
        float_node_obj_map[node.name] = node
    linear_and_quant_node_type = ["Relu", "Clip"]
    for bc_node_name, bc_in_out_bias_tensor in quant_bc_pattern.items():
        if bc_node_name in float_node_obj_map:
            bc_node_start = float_node_obj_map[bc_node_name]
            bc_node_end = float_node_obj_map[bc_node_name]
            node_output_nodes1 = get_output_nodes_of_node(bc_node_start, model.graph)
            while len(node_output_nodes1) > 0:
                if node_output_nodes1[0].op_type in linear_and_quant_node_type:
                    inter_node = node_output_nodes1[0]
                    bc_node_end = inter_node
                    node_output_nodes1 = get_output_nodes_of_node(inter_node, model.graph)
                else:
                    break

            quant_in_out_bias_tensor = bc_in_out_bias_tensor
            bc_input_tensor_name = quant_in_out_bias_tensor[0]
            bc_output_tensor_name = quant_in_out_bias_tensor[1]
            quant_node_bias_name = quant_in_out_bias_tensor[2]
            quant_input = quant_clean_merged_dict[bc_input_tensor_name]
            quant_output = quant_clean_merged_dict[bc_output_tensor_name]
            quant_in_tensor = quant_input
            float_output = inference_sub_model_with_data(model, {bc_node_name: quant_in_tensor}, [bc_node_end.name])

            quant_out_tensor = np.array(quant_output)
            float_out_tensor = np.array(float_output)
            if quant_out_tensor.ndim == 5:
                axis_reduce_4dim = (0, 1, 3, 4)
                float_quant_diff = np.mean((float_out_tensor - quant_out_tensor), axis=axis_reduce_4dim)
            elif quant_out_tensor.ndim == 3:
                axis_reduce_2dim = (0, 1)
                float_quant_diff = np.mean((float_out_tensor - quant_out_tensor), axis=axis_reduce_2dim)
            else:
                logger.warning("the bias correction only support ndim 2 or 4")
                continue
            float_quant_diff_mean = float_quant_diff
            if quant_node_bias_name:
                quant_bias_node = quant_output_tensor_node_map[quant_node_bias_name]
                bias_name = quant_bias_node.input[0]
                scale_name = quant_bias_node.input[1]
                zp_name = quant_bias_node.input[2]
                bias_init = quant_initializer_name_map[bias_name]
                scale_init = quant_initializer_name_map[scale_name]
                zp_init = quant_initializer_name_map[zp_name]
                bias_data = numpy_helper.to_array(bias_init)
                scale_data = numpy_helper.to_array(scale_init)
                zp_data = numpy_helper.to_array(zp_init)
                bias_data_float = dequantize_data(bias_data, scale_data, zp_data)
                max_diff = np.max(np.abs(float_quant_diff_mean))
                max_bias = np.max(np.abs(bias_data_float))
                scale = 1
                plus_bias = max_bias / 256
                if max_diff > plus_bias and max_diff > 0.1:
                    scale = scale * plus_bias / max_diff
                bias_data_bc = bias_data_float + float_quant_diff_mean * scale
                logger.debug(f"the bias_data_float max: {np.max(np.abs(bias_data_float))}")
                logger.debug(f"the diff_mean max: {np.max(np.abs(float_quant_diff_mean * scale))}")
                quantized_data = None
                if calibrate_method in [PowerOfTwoMethod.NonOverflow, PowerOfTwoMethod.MinMSE]:
                    symmetric = (
                        False if "ActivationSymmetric" not in extra_options else extra_options["ActivationSymmetric"]
                    )
                    _, _, zp, scale, quantized_data = quantize_data(
                        data=bias_data_bc, qType=bias_init.data_type, symmetric=symmetric, method=calibrate_method
                    )
                elif calibrate_method in [CalibrationMethod.MinMax, CalibrationMethod.Percentile]:
                    # for cpu the bias is symmetry
                    quantized_data = (np.asarray(bias_data_bc) / scale_data).round().astype(np.int32)
                    quantized_data = np.asarray(quantized_data, dtype=np.int32).reshape(bias_init.dims)
                if quantized_data is not None:
                    bias_bc = numpy_helper.from_array(quantized_data, bias_name)
                    quant_model.graph.initializer.extend([bias_bc])
                    quant_model.graph.initializer.remove(bias_init)
    calibration_data_reader.reset_iter()
    logger.info("BiasCorrection Done...")
    return quant_model

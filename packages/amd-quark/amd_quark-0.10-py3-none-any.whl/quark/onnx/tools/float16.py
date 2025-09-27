#
# Modifications copyright(c) 2023 Advanced Micro Devices,Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
###########################################################################

import itertools
import warnings
from typing import Dict, List, Optional, Set

import numpy as np
import onnx
import packaging.version as pv
from numpy.typing import NDArray
from onnx import helper, numpy_helper
from onnx import onnx_pb as onnx_proto


def _npfloat16_to_int(np_list: NDArray[np.float16]) -> list[int]:
    """
    Convert numpy float16 to python int.

    :param np_list: numpy float16 list
    :return int_list: python int list
    """
    return [int(bin(_.view("H"))[2:].zfill(16), 2) for _ in np_list]


def _npint_to_float(np_list: NDArray[np.int32]) -> list[float]:
    """
    Convert numpy int to python float.

    :param np_list: numpy int list
    :return float_list: python float list
    """
    return [_.astype(np.uint16).view(np.float16).astype(np.float32).item() for _ in np_list]


def convert_np_to_float16(
    np_array: NDArray[np.float32], min_positive_val: float = 1e-7, max_finite_val: float = 1e4
) -> NDArray[np.float16]:
    """
    Convert float32 numpy array to float16 without changing sign or finiteness.
    Positive values less than min_positive_val are mapped to min_positive_val.
    Positive finite values greater than max_finite_val are mapped to max_finite_val.
    Similar for negative values. NaN, 0, inf, and -inf are unchanged.
    """

    def between(a: float, b: NDArray[np.float32], c: float) -> NDArray[np.bool_]:
        return np.logical_and(a < b, b < c)

    if np_array[np.where(np_array > 0)].shape[0] > 0:
        pos_max = np_array[np.where(np_array > 0)].max()
        pos_min = np_array[np.where(np_array > 0)].min()

        if pos_max >= max_finite_val:
            warnings.warn(f"the float32 number {pos_max} will be truncated to {max_finite_val}")

        if pos_min <= min_positive_val:
            warnings.warn(f"the float32 number {pos_min} will be truncated to {min_positive_val}")

    if np_array[np.where(np_array < 0)].shape[0] > 0:
        neg_max = np_array[np.where(np_array < 0)].max()
        neg_min = np_array[np.where(np_array < 0)].min()

        if neg_min <= -max_finite_val:
            warnings.warn(f"the float32 number {neg_min} will be truncated to {-max_finite_val}")

        if neg_max >= -min_positive_val:
            warnings.warn(f"the float32 number {neg_max} will be truncated to {-min_positive_val}")

    np_array = np.where(between(0, np_array, min_positive_val), min_positive_val, np_array)
    np_array = np.where(between(-min_positive_val, np_array, 0), -min_positive_val, np_array)
    np_array = np.where(between(max_finite_val, np_array, float("inf")), max_finite_val, np_array)
    np_array = np.where(between(float("-inf"), np_array, -max_finite_val), -max_finite_val, np_array)
    return np_array.astype(np.float16)  # np.float16(np_array)


def convert_tensor_float_to_float16(
    tensor: onnx_proto.TensorProto, min_positive_val: float = 1e-7, max_finite_val: float = 1e4
) -> onnx_proto.TensorProto:
    """
    Convert tensor float to float16.

    :param tensor: TensorProto object
    :return tensor_float16: converted TensorProto object

    Example:

    ::

        from onnxmltools.utils.float16_converter import convert_tensor_float_to_float16
        new_tensor = convert_tensor_float_to_float16(tensor)

    """
    if not isinstance(tensor, onnx_proto.TensorProto):
        raise ValueError("Expected input type is an ONNX TensorProto but got %s" % type(tensor))

    if tensor.data_type == onnx_proto.TensorProto.FLOAT:
        tensor.data_type = onnx_proto.TensorProto.FLOAT16
        # convert float_data (float type) to float16 and write to int32_data
        if tensor.float_data:
            float16_data = convert_np_to_float16(np.array(tensor.float_data), min_positive_val, max_finite_val)
            int_list = _npfloat16_to_int(float16_data)
            tensor.int32_data[:] = int_list
            tensor.float_data[:] = []
        # convert raw_data (bytes type)
        if tensor.raw_data:
            # convert n.raw_data to float
            float32_list = np.fromstring(tensor.raw_data, dtype="float32")  # type: ignore
            # convert float to float16
            float16_list = convert_np_to_float16(float32_list, min_positive_val, max_finite_val)
            # convert float16 to bytes and write back to raw_data
            tensor.raw_data = float16_list.tostring()  # type: ignore

    return tensor


def make_value_info_from_tensor(tensor: onnx_proto.TensorProto) -> onnx_proto.ValueInfoProto:
    shape = numpy_helper.to_array(tensor).shape
    return helper.make_tensor_value_info(tensor.name, tensor.data_type, shape)


DEFAULT_OP_BLOCK_LIST_FP16 = [
    "ArrayFeatureExtractor",
    "Binarizer",
    "CastMap",
    "CategoryMapper",
    "DictVectorizer",
    "FeatureVectorizer",
    "Imputer",
    "LabelEncoder",
    "LinearClassifier",
    "LinearRegressor",
    "Normalizer",
    "OneHotEncoder",
    "RandomUniformLike",
    "SVMClassifier",
    "SVMRegressor",
    "Scaler",
    "TreeEnsembleClassifier",
    "TreeEnsembleRegressor",
    "ZipMap",
    "NonMaxSuppression",
    "TopK",
    "RoiAlign",
    "Resize",
    "Range",
    "CumSum",
    "Min",
    "Max",
    "Upsample",
]

DEFAULT_OP_BLOCK_LIST_FP32: list[str] = []


def sort_graph_node(graph_proto: onnx_proto.GraphProto) -> None:
    # find the "first" node in Nodes that its input is not any node's output
    def find_first_node(output2node_dict: dict[str, onnx_proto.NodeProto]) -> onnx_proto.NodeProto | None:
        for node in org_nodes:
            is_not_first_node = any(item in output2node_dict for item in node.input)
            if not is_not_first_node:
                return node  # type: ignore
        return None

    # remove the node from output2node_dict using output as key
    def remove_first_node_from_dict2(first_node: onnx_proto.NodeProto) -> None:
        for output in first_node.output:
            if output in output2node_dict:
                del output2node_dict[output]

    org_nodes = graph_proto.node
    # create a dict to store output as key and node as value
    output2node_dict = {}
    for node in org_nodes:
        for output in node.output:
            output2node_dict[output] = node

    # save the final node after sorted
    sorted_node = []
    # traverse the Nodes to find the first node
    while len(output2node_dict) > 0:
        first_node = find_first_node(output2node_dict)
        sorted_node.append(first_node)
        assert first_node is not None, "Cannot find the first node in the graph."
        remove_first_node_from_dict2(first_node)
        # del node from original nodes list to avoid duplicate traverse
        org_nodes.remove(first_node)

    for new_node in sorted_node:
        graph_proto.node.extend([new_node])


# The input graph should be mode.graph
# Recursevly sort the topology for each sub-graph
def sort_topology(graph_proto: onnx_proto.GraphProto) -> None:
    assert isinstance(graph_proto, onnx_proto.GraphProto)
    sort_graph_node(graph_proto)  # sort global graph
    for node in graph_proto.node:
        for attr in node.attribute:
            if isinstance(attr.g, onnx_proto.GraphProto) and len(attr.g.node) > 0:
                sort_topology(attr.g)  # sort sub-graph
            for g in attr.graphs:
                if isinstance(g, onnx_proto.GraphProto):
                    sort_topology(g)  # sort sub-graph


def convert_np_to_float(
    np_array: NDArray[np.float16], min_positive_val: float = 1e-7, max_finite_val: float = 1e4
) -> NDArray[np.float32]:
    """
    Convert float16 numpy array to float32 without changing sign or finiteness.
    Similar for negative values. NaN, 0, inf, and -inf are unchanged.
    """
    return np_array.astype(np.float32)  # np.float32(np_array)


def convert_tensor_float16_to_float(tensor: onnx_proto.TensorProto) -> onnx_proto.TensorProto:
    """
    Convert tensor float16 to float.

    :param tensor: TensorProto object
    :return tensor_float: converted TensorProto object

    Example:

    ::

        new_tensor = convert_tensor_float16_to_float(tensor)

    """
    if not isinstance(tensor, onnx_proto.TensorProto):
        raise ValueError("Expected input type is an ONNX TensorProto but got %s" % type(tensor))

    if tensor.data_type == onnx_proto.TensorProto.FLOAT16:
        tensor.data_type = onnx_proto.TensorProto.FLOAT
        # convert float16_data (float16 type) to float and write to int32_data
        if tensor.int32_data:
            float_list = _npint_to_float(np.array(tensor.int32_data))
            tensor.int32_data[:] = []
            tensor.float_data[:] = float_list
        # convert raw_data (bytes type)
        if tensor.raw_data:
            # convert n.raw_data to float
            float16_list = np.fromstring(tensor.raw_data, dtype="float16")  # type: ignore
            # convert float to float16
            float32_list = convert_np_to_float(float16_list)
            # convert float16 to bytes and write back to raw_data
            tensor.raw_data = float32_list.tostring()  # type: ignore
    return tensor


def convert_float16_to_float(
    model: onnx_proto.ModelProto,
    disable_shape_infer: bool = False,
    op_block_list: list[str] | None = None,
    node_block_list: list[str] | None = None,
) -> onnx_proto.ModelProto:
    """
    Convert tensor float16 type in the ONNX ModelProto input to tensor float.

    :param model: ONNX ModelProto object
    :param disable_shape_infer: Type/shape information is needed for conversion to work.
                                Set to True only if the model already has type/shape information for all tensors.
    :return: converted ONNX ModelProto object

    Examples:

    ::

        Example 1: Convert ONNX ModelProto object:
        import float16
        new_onnx_model = float16.convert_float16_to_float(onnx_model)

        Example 2: Convert ONNX model binary file:
        import onnx
        import float16
        onnx_model = onnx.load_model('model.onnx')
        new_onnx_model = float16.convert_float16_to_float(onnx_model)
        onnx.save_model(new_onnx_model, 'new_model.onnx')

    """
    func_infer_shape = None
    if not disable_shape_infer and pv.Version(onnx.__version__) >= pv.Version("1.2"):  # type: ignore
        try:
            from onnx.shape_inference import infer_shapes

            func_infer_shape = infer_shapes
        finally:
            pass

    if not isinstance(model, onnx_proto.ModelProto):
        raise ValueError("Expected model type is an ONNX ModelProto but got %s" % type(model))

    # create blocklists
    if op_block_list is None:
        op_block_list = DEFAULT_OP_BLOCK_LIST_FP32
    if node_block_list is None:
        node_block_list = []
    op_block_list = set(op_block_list)
    node_block_list = set(node_block_list)
    # create a queue for BFS
    queue = []
    value_info_list = []
    node_list = []
    # key = node, value = graph, used to distinguish global with sub-graph
    node_dict = {}
    # type inference on input model
    if func_infer_shape is not None:
        model = func_infer_shape(model)
    queue.append(model)
    name_mapping: dict[str, str] = {}
    graph_io_to_skip: set[str] = set()
    io_casts: set[str] = set()

    while queue:
        next_level = []
        for q in queue:
            # if q is model, push q.graph (GraphProto)
            if isinstance(q, onnx_proto.ModelProto):
                next_level.append(q.graph)
            # if q is model.graph, push q.node.attribute (AttributeProto)
            if isinstance(q, onnx_proto.GraphProto):
                for n in q.node:
                    # if n is in the block list (doesn't support float16), no conversion for the node,
                    # and save the node for further processing
                    if n.name in io_casts:
                        continue
                    for i in range(len(n.input)):
                        if n.input[i] in name_mapping:
                            n.input[i] = name_mapping[n.input[i]]
                    for i in range(len(n.output)):
                        if n.output[i] in name_mapping:
                            n.output[i] = name_mapping[n.output[i]]
                    # don't add the attr into next_level for the node in node_keep_data_type_list
                    # so it will not be converted to float16
                    if n.op_type in op_block_list or n.name in node_block_list:
                        node_list.append(n)
                        node_dict[n.name] = q
                    else:
                        if n.op_type == "Cast":
                            for attr in n.attribute:
                                if attr.name == "to" and attr.i == 10:
                                    attr.i = 1
                                    break
                        for attr in n.attribute:
                            next_level.append(attr)
            # if q is model.graph.node.attribute, push q.g and q.graphs (GraphProto)
            # and process node.attribute.t and node.attribute.tensors (TensorProto)
            if isinstance(q, onnx_proto.AttributeProto):
                next_level.append(q.g)
                for n in q.graphs:
                    next_level.append(n)
                q.t.CopyFrom(convert_tensor_float16_to_float(q.t))
                for n in q.tensors:
                    n = convert_tensor_float16_to_float(n)
            # if q is graph, process graph.initializer(TensorProto), input, output and value_info (ValueInfoProto)
            if isinstance(q, onnx_proto.GraphProto):
                for n in q.initializer:  # TensorProto type
                    if n.data_type == onnx_proto.TensorProto.FLOAT16:
                        n = convert_tensor_float16_to_float(n)
                        value_info_list.append(make_value_info_from_tensor(n))
                # for all ValueInfoProto with tensor(float) type in input, output and value_info, convert them to
                # tensor(float16) except map and seq(map). And save them in value_info_list for further processing
                for n in itertools.chain(q.input, q.output, q.value_info):
                    if n.type.tensor_type.elem_type == onnx_proto.TensorProto.FLOAT16:
                        if n.name not in graph_io_to_skip:
                            n.type.tensor_type.elem_type = onnx_proto.TensorProto.FLOAT
                            value_info_list.append(n)
        queue = next_level

    # process the nodes in block list that doesn't support tensor(float16)
    for node in node_list:
        # if input's name is in the value_info_list meaning input is tensor(float16) type,
        # insert a float16 to float Cast node before the node,
        # change current node's input name and create new value_info for the new name
        for i in range(len(node.input)):
            input = node.input[i]
            for value_info in value_info_list:
                if input == value_info.name:
                    # create new value_info for current node's new input name
                    graph = node_dict[node.name]  # get the correct graph instead of the global graph
                    new_value_info = graph.value_info.add()
                    new_value_info.CopyFrom(value_info)
                    output_name = node.name + "_input_cast_" + str(i)
                    new_value_info.name = output_name
                    new_value_info.type.tensor_type.elem_type = onnx_proto.TensorProto.FLOAT16
                    # add Cast node (from tensor(float16) to tensor(float) before current node
                    node_name = node.name + "_input_cast" + str(i)
                    new_node = [helper.make_node("Cast", [input], [output_name], to=10, name=node_name)]
                    graph.node.extend(new_node)
                    # change current node's input name
                    node.input[i] = output_name
                    break
        # if output's name is in the value_info_list meaning output is tensor(float16) type, insert a float to
        # float16 Cast node after the node, change current node's output name and create new value_info for the new name
        for i in range(len(node.output)):
            output = node.output[i]
            for value_info in value_info_list:
                if output == value_info.name:
                    # create new value_info for current node's new output
                    graph = node_dict[node.name]  # get the correct graph instead of the global graph
                    new_value_info = graph.value_info.add()
                    new_value_info.CopyFrom(value_info)
                    input_name = node.name + "_output_cast_" + str(i)
                    new_value_info.name = input_name
                    new_value_info.type.tensor_type.elem_type = onnx_proto.TensorProto.FLOAT
                    # add Cast node (from tensor(float) to tensor(float16) after current node
                    node_name = node.name + "_output_cast" + str(i)
                    new_node = [helper.make_node("Cast", [input_name], [output], to=1, name=node_name)]
                    graph.node.extend(new_node)
                    # change current node's input name
                    node.output[i] = input_name
                    break

    sort_topology(model.graph)
    return model

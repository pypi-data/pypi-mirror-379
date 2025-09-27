#
# Copyright (C) 2024, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
"""Remove QDQ in the `mul + q + dq + add` structure operators."""

import argparse
import os
from typing import Any, List, Optional

import onnx
from onnx import ModelProto, NodeProto
from onnxruntime.quantization.onnx_model import ONNXModel

from quark.onnx.quant_utils import get_tensor_to_consumer
from quark.shares.utils.log import ScreenLogger

logger = ScreenLogger(__name__)


def remove_qdq_mul_add(onnx_model: ModelProto) -> Any:
    """
    Modify an ONNX quantized model to remove q and dq ops in the `mul + q + dq + add` structure.
    Start from `Add` nodes and traverse upwards.

    :param onnx_model: The input ONNX model.
    :return: Modified ONNX model with q and dq ops in the `mul + q + dq + add` structure removed.
    """

    try:
        tensor_to_consumer = get_tensor_to_consumer(onnx_model)
        nodes = onnx_model.graph.node
        nodes_to_remove = []
        edges_to_reconnect = []

        for add_node in nodes:
            if add_node.op_type == "Add":
                add_inputs = add_node.input

                for input_name in add_inputs:
                    dq_node = find_node_by_output(nodes, input_name)
                    if dq_node and dq_node.op_type == "DequantizeLinear":
                        consumers = tensor_to_consumer[dq_node.output[0]]
                        if len(consumers) > 1:
                            consumer_str = ", ".join(f"{n.op_type}('{n.name}')" for n in consumers)
                            logger.debug(
                                f"Skip pattern match: output of DequantizeLinear('{dq_node.name}') is connected to {len(consumers)} nodes: {consumer_str}."
                            )
                            continue

                        dq_input = dq_node.input[0]
                        q_node = find_node_by_output(nodes, dq_input)
                        if q_node and q_node.op_type == "QuantizeLinear":
                            q_input = q_node.input[0]

                            mul_node = find_node_by_output(nodes, q_input)
                            if mul_node and mul_node.op_type == "Mul":
                                nodes_to_remove.extend([q_node, dq_node])
                                edges_to_reconnect.append((mul_node.output[0], add_node, input_name))

        for node in nodes_to_remove:
            nodes.remove(node)

        for mul_output, add_node, original_input in edges_to_reconnect:
            for i, add_inp in enumerate(add_node.input):
                if add_inp == original_input:
                    add_node.input[i] = mul_output

        onnx_model = ONNXModel(onnx_model)
        onnx_model.clean_initializers()
        onnx_model.topological_sort()
        logger.info("Removed QuantizeLinear & DequantizeLinear operations: mul-add.")

        return onnx_model.model

    except Exception as e:
        logger.warning(f"Unable to remove QuantizeLinear & DequantizeLinear operations: mul-add. Exception: {e}")


def find_node_by_output(nodes: list[NodeProto], output_name: str) -> NodeProto | None:
    """
    Find a node that produces the specified output.

    :param nodes: List of nodes to search.
    :param output_name: The output name to match.
    :return: The node that matches the output or None if not found.
    """
    for node in nodes:
        if output_name in node.output:
            return node
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_model", type=str, default="", help="input onnx model file path.")
    parser.add_argument("--output_model", type=str, default="", help="output onnx model file path.")
    FLAGS, uparsed = parser.parse_known_args()

    if not os.path.isfile(FLAGS.input_model):
        print(f"Input model file '{FLAGS.input_model}' does not exist!")
        print(
            "Usage: python -m quark.onnx.tools.remove_qdq_mul_add --input_model INPUT_MODEL_PATH --output_model OUTPUT_MODEL_PATH."
        )
        exit()

    model = onnx.load_model(FLAGS.input_model)
    converted_model = remove_qdq_mul_add(model)
    onnx.save(converted_model, FLAGS.output_model)
    logger.info("Conversion Finished!")
    logger.info(f"Converted model saved in: {FLAGS.output_model}")


if __name__ == "__main__":
    main()

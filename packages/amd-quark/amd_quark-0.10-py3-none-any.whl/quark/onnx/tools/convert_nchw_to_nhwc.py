#
# Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
"""
Convert the input NCHW model to the NHWC model.

    Example : python -m quark.onnx.tools.convert_nchw_to_nhwc --input [INPUT_PATH] --output [OUTPUT_PATH]

"""

from argparse import ArgumentParser, Namespace

import onnx
import onnxruntime

from quark.onnx.utils.model_utils import convert_nchw_to_nhwc
from quark.shares.utils.log import ScreenLogger

logger = ScreenLogger(__name__)


def parse_args() -> Namespace:
    usage_str = "python -m quark.onnx.tools.convert_nchw_to_nhwc --input [INPUT_PATH] --output [OUTPUT_PATH]"
    parser = ArgumentParser("convert_nchw_to_nhwc", usage=usage_str)
    parser.add_argument("input", type=str, help="input onnx model path")
    parser.add_argument("output", type=str, help="output onnx model path")
    args, _ = parser.parse_known_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    try:
        ort_session = onnxruntime.InferenceSession(args.input, providers=["CPUExecutionProvider"])
    except Exception as e:
        raise RuntimeError(f"Invalid input model got, please check the input model. ONNX Runtime error: \n{e}")
    input_model = onnx.load(args.input)
    output_model = convert_nchw_to_nhwc(input_model)
    onnx.save_model(output_model, args.output)
    print(f"Converted the NCHW model {args.input} to the NHWC model {args.output}.")

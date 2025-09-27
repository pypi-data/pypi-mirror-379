//
// Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: MIT
//
#include "mx/mx.h"

#include <cassert>
#include <cmath>
#include <iostream>
#include <mutex>
#include <vector>

#include "mx/cuda/mx_kernel.h"

void to_mx(
  const Ort::Value &tensor, std::string &scale_dtype,
  std::string &element_dtype, int64_t block_size, int64_t rounding_mode,
  Ort::Value &out
) {
  const float *input = tensor.GetTensorData<float>();
  float *output = out.GetTensorMutableData<float>();
  size_t element_count = out.GetTensorTypeAndShapeInfo().GetElementCount();
  std::vector<int64_t> dimensions =
    tensor.GetTensorTypeAndShapeInfo().GetShape();

  assert(scale_dtype == "e8m0" && "Only supports 'e8m0' shared scale");

  std::vector<int> bits;
  std::vector<float> range;
  ParseElementDataTypeString(element_dtype, bits, range);
  assert(
    bits.size() >= 2 && bits[0] + bits[1] > 0 && "Unsupported element data type"
  );

  int axis_size = dimensions[dimensions.size() - 1];
  LaunchMXCUDAKernel(
    input, output, element_count, axis_size, block_size, bits[0], bits[1],
    bits[2], range[0], range[1], rounding_mode
  );
}

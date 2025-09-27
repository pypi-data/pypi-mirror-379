//
// Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: MIT
//

#include "funcs.cuh"

#include <ATen/ATen.h>
#include <torch/extension.h>

void fake_quantize_to_low_precision_fp_cpu(
  float *input, float *output, uint32_t num_elements, int ebits, int mbits,
  float max_norm, RoundMode round_mode
) {
  for (int i = 0; i < num_elements; i++) {
    output[i] =
      fake_quantize_element(input[i], max_norm, ebits, mbits, round_mode);
  }
}

torch::Tensor fake_quantize_to_low_precision_fp(
  torch::Tensor &input, int ebits, int mbits, float max_norm,
  uint32_t round_mode
) {
  float *input_data = input.data_ptr<float>();
  torch::Tensor output = torch::empty_like(input);
  float *output_data = output.data_ptr<float>();
#ifdef USE_CUDA
  if (input.is_cpu()) {
    fake_quantize_to_low_precision_fp_cpu(
      input_data, output_data, input.numel(), ebits, mbits, max_norm,
      (RoundMode)round_mode
    );
  } else {
    const at::cuda::OptionalCUDAGuard device_guard(device_of(input));
    fake_quantize_to_low_precision_fp_cuda(
      input_data, output_data, input.numel(), ebits, mbits, max_norm,
      (RoundMode)round_mode
    );
  }
#else
  fake_quantize_to_low_precision_fp_cpu(
    input_data, output_data, input.numel(), ebits, mbits, max_norm,
    (RoundMode)round_mode
  );
#endif
  return output;
}

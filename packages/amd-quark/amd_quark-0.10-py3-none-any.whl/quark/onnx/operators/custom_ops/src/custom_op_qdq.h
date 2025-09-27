//
// Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: MIT
//

#pragma once

#include "onnxruntime_c_api.h"
#define ORT_API_MANUAL_INIT
#include "onnxruntime_cxx_api.h"
#undef ORT_API_MANUAL_INIT

namespace quark_onnx {

// Since onnxruntime has no conversion for MLFloat16,
// we just used Cast op to do this.

#define USE_NATIVE_OP_CAST

struct KernelCustomQuantizeLinear {
  KernelCustomQuantizeLinear(const OrtApi &api, const OrtKernelInfo *info);
  ~KernelCustomQuantizeLinear();

  void Compute(OrtKernelContext *context);
#if ORT_API_VERSION >= 17
  // This is for adapting to onnxruntime_cxx_api.h in ORT 1.17.0 (and higher)
  OrtStatusPtr ComputeV2(OrtKernelContext *context) { return nullptr; }
#endif

 protected:
  void ComputeBase(OrtKernelContext *context);

 private:
  const OrtApi &api_;
  Ort::KernelInfo info_{nullptr};

  int64_t axis_ = 1;

#ifdef USE_NATIVE_OP_CAST
  Ort::Op cast_to_float16_{nullptr};
#endif
};

struct KernelCustomDequantizeLinear {
  KernelCustomDequantizeLinear(const OrtApi &api, const OrtKernelInfo *info);
  ~KernelCustomDequantizeLinear();

  void Compute(OrtKernelContext *context);
#if ORT_API_VERSION >= 17
  // This is for adapting to onnxruntime_cxx_api.h in ORT 1.17.0 (and higher)
  OrtStatusPtr ComputeV2(OrtKernelContext *context) { return nullptr; }
#endif

 protected:
  void ComputeBase(OrtKernelContext *context);

 private:
  const OrtApi &api_;
  Ort::KernelInfo info_{nullptr};

  int64_t axis_ = 1;

#ifdef USE_NATIVE_OP_CAST
  Ort::Op cast_from_float16_{nullptr};
#endif
};

}  // namespace quark_onnx

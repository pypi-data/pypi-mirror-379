#
# Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import gc
import os
from typing import Any, Dict, List, Optional, Tuple, Union

import torch
from torch.utils.data import DataLoader

from quark.shares.utils.import_utils import is_transformers_available
from quark.shares.utils.log import ScreenLogger, log_errors
from quark.torch.quantization.config.type import Dtype

QUARK_DEBUG = os.environ.get("QUARK_DEBUG", "0") == "1"
DEBUG_NAN = os.environ.get("QUARK_DEBUG_NAN", None) or QUARK_DEBUG

if is_transformers_available():
    from transformers.feature_extraction_utils import BatchFeature

logger = ScreenLogger(__name__)


def assert_no_nan(tensor: torch.Tensor, message: str) -> None:
    """
    Asserts that the tensor does not contain any NaN value. If it does, it will raise a `AssertionError` with the given message.

    Only does the assertion if the environment variable `QUARK_DEBUG_NAN` is set to `1`. This is useful to avoid the overhead of checking for NaNs in production code.

    Args:
        tensor (torch.Tensor): The tensor to check for NaNs.
        message (str): The message to display in the `AssertionError` if the tensor contains NaNs.
    """
    if DEBUG_NAN:
        torch._assert_async(~torch.isnan(tensor).any(), message)


def clear_memory(weight: torch.Tensor | None = None) -> None:
    if weight is not None:
        del weight
    gc.collect()
    torch.cuda.empty_cache()


def validate_qmin_qmax(quant_min: int, quant_max: int) -> None:
    assert quant_min < quant_max, "qmin must be less than qmax."


def calculate_qmin_qmax(dtype: Dtype) -> tuple[Union[int, float], Union[int, float]]:
    # Fallback onto default 8-bit qmin and qmax calculation if dynamic range is not used.
    if dtype == Dtype.int8:
        return -128, 127
    elif dtype == Dtype.uint8:
        return 0, 255
    elif dtype == Dtype.int16:
        return -(2**15), 2**15 - 1
    elif dtype == Dtype.int32:
        return -(2**31), 2**31 - 1
    elif dtype == Dtype.int4:
        return -8, 7
    elif dtype == Dtype.uint4:
        return 0, 15
    elif dtype == Dtype.int3:
        return -4, 3
    elif dtype == Dtype.int2:
        return -2, 1
    elif dtype == Dtype.fp8_e4m3:
        return -448, 448
    elif dtype == Dtype.fp8_e5m2:
        return -57344, 57344
    elif dtype == Dtype.bfloat16:
        return torch.finfo(torch.bfloat16).min, torch.finfo(torch.bfloat16).max
    elif dtype == Dtype.float16:
        return torch.finfo(torch.float16).min, torch.finfo(torch.float16).max
    elif dtype == Dtype.fp6_e3m2:
        return -28.0, 28.0
    elif dtype == Dtype.fp6_e2m3:
        return -7.5, 7.5
    elif dtype == Dtype.fp4:
        return -6.0, 6.0
    else:
        raise ValueError("The qmin and qmax of {dtype} are not defined")


def get_num_bits(dtype: Dtype) -> Union[int, tuple[int, int]] | None:
    if dtype in [Dtype.int4, Dtype.uint4]:
        return 4
    elif dtype in [Dtype.int8, Dtype.uint8]:
        return 8
    elif dtype in [Dtype.int16, Dtype.uint16]:
        return 16
    elif dtype in [Dtype.int32]:
        return 32
    elif dtype == Dtype.fp8_e4m3:
        return (4, 3)
    else:
        return None


def deep_compare(dict1: dict[str, Any], dict2: dict[str, Any]) -> bool:
    if type(dict1) != type(dict2):
        return False
    if isinstance(dict1, dict):
        if dict1.keys() != dict2.keys():
            return False
        return all(deep_compare(dict1[k], dict2[k]) for k in dict1)
    elif isinstance(dict1, list):
        return set(dict1) == set(dict2)
    else:
        return dict1 == dict2


_FORMAT_CACHE: dict[Dtype, tuple[int, int, int]] = {}


def get_dtype_params(dtype: Union[str, Dtype]) -> tuple[int, int, int]:
    if isinstance(dtype, str):
        dtype = Dtype.from_str(dtype)

    if dtype in _FORMAT_CACHE:
        return _FORMAT_CACHE[dtype]

    if dtype == Dtype.int8:
        ebits, mbits = 0, 8
        emax = 0
    elif dtype == Dtype.int4:
        ebits, mbits = 0, 4
        emax = 0
    elif dtype == Dtype.int3:
        ebits, mbits = 0, 3
        emax = 0
    elif dtype == Dtype.int2:
        ebits, mbits = 0, 2
        emax = 0
    elif dtype == Dtype.fp8_e5m2:
        ebits, mbits = 5, 2
        emax = 2 ** (ebits - 1) - 1
    elif dtype == Dtype.fp8_e4m3:
        ebits, mbits = 4, 3
        emax = 2 ** (ebits - 1)
    elif dtype == Dtype.fp6_e3m2:
        ebits, mbits = 3, 2
        emax = 2 ** (ebits - 1)
    elif dtype == Dtype.fp6_e2m3:
        ebits, mbits = 2, 3
        emax = 2 ** (ebits - 1)
    elif dtype == Dtype.fp4:
        ebits, mbits = 2, 1
        emax = 2 ** (ebits - 1)
    elif dtype == Dtype.float16:
        ebits, mbits = 5, 10
        emax = 2 ** (ebits - 1) - 1
    elif dtype == Dtype.bfloat16:
        ebits, mbits = 8, 7
        emax = 2 ** (ebits - 1) - 1
    else:
        raise Exception("Unknown element format %s" % dtype)

    _FORMAT_CACHE[dtype] = (ebits, mbits, emax)

    return ebits, mbits, emax


def pad_to_blocks(x: torch.Tensor, block_size: int) -> tuple[torch.Tensor, int]:
    num_elem_to_be_padded = block_size - x.size(-1) % block_size
    if num_elem_to_be_padded == block_size:
        return x, 0
    return torch.nn.functional.pad(x, (0, num_elem_to_be_padded)), num_elem_to_be_padded


def reshape_to_blocks(x: torch.Tensor, block_size: int, axis: int) -> torch.Tensor:
    if axis > x.dim() - 1:
        raise IndexError("Axis is larger than number of tensor dimensions")

    x = x.transpose(axis, -1)
    x = x.reshape(-1, x.size(-1))

    x, _ = pad_to_blocks(x, block_size)

    return x.reshape(x.size(0), x.size(1) // block_size, block_size)


@log_errors
def exponent_frexp_no_exception(t: torch.Tensor) -> torch.Tensor:
    with torch.no_grad():
        t_dtype = t.dtype

        if t_dtype == torch.float32:
            int_tensor = t.view(torch.int32)
            t_exp = ((int_tensor >> 23) & 0xFF) - 127
        elif t_dtype == torch.bfloat16:
            int_tensor = t.view(torch.int16)
            t_exp = ((int_tensor >> 7) & 0xFF) - 127
        elif t_dtype == torch.float16:
            # zero has a different exponent here comparing to the original version
            # exponent bias is now defined as -15
            int_tensor = t.view(torch.int16)
            t_exp = ((int_tensor >> 10) & 0x1F) - 15
        else:
            raise ValueError(f"Unsupported data type: {t_dtype}")  # pragma: no cover

        return t_exp


def t_exponent(t: torch.Tensor) -> torch.Tensor:
    """Get element exponents

    Args:
        t (torch.Tensor): Input tensor

    Returns:
        torch.Tensor: Exponents for each elements. NaN and Inf are treated as zeros.

    """
    with torch.no_grad():
        t = torch.nan_to_num(t, nan=0, posinf=0, neginf=0)
        t_exp = exponent_frexp_no_exception(t)

        return t_exp


def even_round(max_abs: torch.Tensor, dtype: Union[Dtype, str]) -> torch.Tensor:
    f32_min_normal = 2 ** (-127 + 1)
    eps = f32_min_normal * (max_abs == 0).type(max_abs.dtype)

    nan_mask = torch.isnan(max_abs)
    max_abs = max_abs.to(torch.float32).view(torch.int32)
    ebits, mbits, emax = get_dtype_params(dtype)

    # Rounding strategy between [2**n, 2**(n+1)]:
    # x in [2**n, 2**n *(1 + 0.5 + 0.25)[ => round to 2**n
    # x in [2**n * 1.75, 2**(n + 1)] => round to 2**(n+1)
    #
    # `val_to_add` overflows on the exponent bits in case we round up.
    val_to_add = 1 << (23 - mbits - 1)

    # Mask for the 9 leftmost bits (1 sign, 8 exponent) of the float32 representation.
    fp32_sign_exponent_mask = ((1 << (8 + 1)) - 1) << 23

    max_abs = (max_abs + val_to_add) & fp32_sign_exponent_mask
    max_abs = max_abs.view(torch.float32)

    max_abs.masked_fill_(nan_mask, float("nan"))

    # See section 6.3 of https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf
    # for the computation below.
    scale_e8m0_unbiased = torch.floor(torch.log2(max_abs + eps)) - emax
    scale_e8m0_unbiased = torch.clamp(scale_e8m0_unbiased, min=-127, max=127)
    scale_float = torch.pow(2, scale_e8m0_unbiased)
    return scale_float


def count_calibration_tokens(
    dataloader: Union[
        DataLoader[torch.Tensor],
        DataLoader[list[dict[str, torch.Tensor]]],
        DataLoader[dict[str, torch.Tensor]],
        DataLoader[list["BatchFeature"]],
    ],
) -> int:
    total_tokens = 0
    for data in dataloader:
        if isinstance(data, dict) or (is_transformers_available() and isinstance(data, BatchFeature)):
            if "input_ids" in data.keys():
                if isinstance(data["input_ids"], torch.Tensor):
                    total_tokens += data["input_ids"].numel()
                else:
                    logger.warning(
                        "Counting calibration tokens, "
                        f"unsupported calibration data type {type(data['input_ids'])}, returning 0."
                    )
                    return 0
        elif isinstance(data, torch.Tensor):
            total_tokens += data.numel()
        else:
            logger.warning(f"Counting calibration tokens, unsupported calibration data type {type(data)}, returning 0.")
            return 0

    return total_tokens

#
# Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
"""Quark Exporting Config API for PyTorch"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(eq=True)
class ExporterConfig:
    """
    A class that encapsulates comprehensive exporting configurations for a machine learning model, allowing for detailed control over exporting parameters across different exporting formats.

    :param Optional[JsonExporterConfig] json_export_config: Global configuration for json-safetensors exporting.
    :param Optional[OnnxExporterConfig] onnx_export_config: Global configuration onnx exporting. Default is None.
    """

    # Global json-safetensors exporting configuration
    json_export_config: JsonExporterConfig

    # Global onnx exporting configuration
    onnx_export_config: OnnxExporterConfig | None = None


# TODO: better `min_kv_scale` doc.
@dataclass(eq=True)
class JsonExporterConfig:
    """
    A data class that specifies configurations for json-safetensors exporting.

    :param Optional[List[List[str]]] weight_merge_groups: A list of operators group that share the same weight scaling factor. These operators' names should correspond to the original module names from the model. Additionally, wildcards can be used to denote a range of operators. Default is ``None``.
    :param List[str] kv_cache_group: A list of operators group that should be merged to kv_cache. These operators' names should correspond to the original module names from the model. Additionally, wildcards can be used to denote a range of operators. Defaults to ``[]``.
    :param float min_kv_scale: Minimum kv scale. Defaults to ``0.0``.
    :param str weight_format: The flag indicating whether to export the real quantized weights. Defaults to ``"real_quantized"``.
    :param str pack_method: The flag indicating whether to reorder the quantized tensors. Defaults to ``"reorder"``.

    """

    weight_merge_groups: list[list[str]] | None = None
    kv_cache_group: list[str] = field(default_factory=list)
    min_kv_scale: float = 0.0
    weight_format: str = "real_quantized"
    pack_method: str = "reorder"


@dataclass(eq=True)
class OnnxExporterConfig:
    """
    A data class that specifies configurations for onnx exporting.
    """

    pass

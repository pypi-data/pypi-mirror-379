#
# Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import fnmatch
import functools
from collections import OrderedDict
from functools import partial
from types import MethodType
from typing import Any, Callable, Dict, Optional, Union

import torch
import torch.nn as nn
from torch import dtype as DType
from tqdm import tqdm

from quark.shares.utils.log import DebugLogger, ScreenLogger, log_errors
from quark.torch.export.nn.modules.realquantizer import RealQuantizerBase, SequentialRealQuantizer
from quark.torch.quantization.config.config import Config, QuantizationConfig, QuantizationSpec
from quark.torch.quantization.nn.modules.quantize_conv import QuantConv2d, QuantConvTranspose2d
from quark.torch.quantization.nn.modules.quantize_embed import QuantEmbedding, QuantEmbeddingBag
from quark.torch.quantization.nn.modules.quantize_linear import QuantLinear
from quark.torch.quantization.tensor_quantize import FakeQuantizeBase, SequentialQuantize
from quark.torch.utils import setattr_recursive

in_place_replace_ops = DebugLogger(name="in_place_replace_ops")
logger = ScreenLogger(__name__)

LAYER_TO_QUANT_LAYER_MAP = {
    nn.Conv2d: QuantConv2d,
    nn.Linear: QuantLinear,
    nn.ConvTranspose2d: QuantConvTranspose2d,
    nn.Embedding: QuantEmbedding,
    nn.EmbeddingBag: QuantEmbeddingBag,
}


def process_model_transformation(model: nn.Module, config: Config) -> nn.Module:
    """
    Replaces modules to be quantized by their quantized equivalent (e.g. nn.Linear by QuantLinear), based on the provided global `config`.
    """
    logger.info("In-place OPs replacement start.")
    named_modules = dict(model.named_modules(remove_duplicate=False))
    module_configs: dict[str, QuantizationConfig] = {}

    prepare_for_attention_quant(model, config, FakeQuantizeBase.get_fake_quantize)
    setup_config_per_layer(config, named_modules, module_configs)
    setup_kv_cache_config(config, named_modules, module_configs)
    in_place_replace_layer(model, config, named_modules, module_configs)

    logger.info("In-place OPs replacement end.")
    return model


def setup_config_per_layer(
    config: Config, named_modules: dict[str, nn.Module], module_configs: dict[str, QuantizationConfig]
) -> None:
    """
    Retrieves the `QuantizationConfig` used for each layer, based on the
    `config`'s `global_quant_config`, `layer_quant_config` and `layer_type_quant_config`.
    """
    exclude_count = dict.fromkeys(config.exclude, 0)
    exclude_fullname = []
    for name, module in named_modules.items():
        strict = False
        if type(module) in [nn.Embedding, nn.EmbeddingBag]:
            strict = True

        if type(module) in LAYER_TO_QUANT_LAYER_MAP:
            excluded = False
            for name_pattern in config.exclude:
                if fnmatch.fnmatch(name, name_pattern):
                    exclude_fullname.append(name)
                    excluded = True
                    exclude_count[name_pattern] += 1
                    break
            if excluded:
                continue

            # Determine the quantization config of the layer according to priority. Specifically, layer_quant_config>layer_type_quant_config>global_quant_config
            reset = False
            for name_pattern, quant_config in config.layer_quant_config.items():
                if fnmatch.fnmatch(name, name_pattern):
                    module_configs[name] = quant_config
                    reset = True
                    break

            if not reset:
                for module_pattern, quant_config in config.layer_type_quant_config.items():
                    if isinstance(module, module_pattern):
                        module_configs[name] = quant_config
                        reset = True
                        break

            if not reset and not strict:
                module_configs[name] = config.global_quant_config

    if len(config.exclude) > 0:
        row_format = "|{:^28}|{:^28}|"
        table = row_format.format("Exclude pattern", "Number of modules excluded") + "\n"
        for name_pattern in config.exclude:
            table += row_format.format(name_pattern, exclude_count[name_pattern]) + "\n"

        logger.info(f"Module exclusion from quantization summary:\n{table}")

    config.exclude = exclude_fullname


def setup_kv_cache_config(
    config: Config, named_modules: dict[str, nn.Module], module_configs: dict[str, QuantizationConfig]
) -> None:
    for name, module in named_modules.items():
        if type(module) in LAYER_TO_QUANT_LAYER_MAP:
            for name_pattern, kv_cache_quant_config in config.kv_cache_quant_config.items():
                if fnmatch.fnmatch(name, name_pattern):
                    module_configs[name] = kv_cache_quant_config
                    for name_exclude_pattern in config.exclude:
                        if fnmatch.fnmatch(name, name_exclude_pattern):
                            module_configs[name].input_tensors = None
                            module_configs[name].weight = None


def prepare_for_attention_quant(
    model: nn.Module,
    config: Config,
    get_quantize: Callable[
        [Union[QuantizationSpec, list[QuantizationSpec]]],
        Union[FakeQuantizeBase, RealQuantizerBase, SequentialQuantize, SequentialRealQuantizer],
    ],
) -> None:
    if config.softmax_quant_spec is not None:
        if model.config._attn_implementation != "eager":
            logger.warning(
                "When model.config._attn_implementation != 'eager', the output of torch.nn.functional.softmax will not be quantized."
            )
        else:
            logger.info("Add a quantize node to the output of each torch.nn.functional.softmax.")
            for name, module in model.named_modules():
                if name.endswith("attn") or name.endswith("attention"):
                    module.prob_quantizer = get_quantize(config.softmax_quant_spec)
                    assert isinstance(module.prob_quantizer, (FakeQuantizeBase, RealQuantizerBase)), (
                        "module.prob_quantizer only supports FakeQuantizeBase or RealQuantizerBase instance currently"
                    )

                    original_softmax = nn.functional.softmax

                    def q_softmax(
                        prob_quantizer: Union[FakeQuantizeBase, RealQuantizerBase],
                        input: torch.Tensor,
                        dim: int | None = None,
                        _stacklevel: int = 3,
                        dtype: DType | None = None,
                    ) -> Any:
                        output = original_softmax(input, dim=dim, _stacklevel=_stacklevel, dtype=dtype).to(input.dtype)
                        if prob_quantizer is not None:
                            output = prob_quantizer(output)
                        return output

                    def patch_softmax(
                        module: nn.Module, prob_quantizer: Union[FakeQuantizeBase, RealQuantizerBase]
                    ) -> None:
                        original_forward = module.forward

                        @functools.wraps(original_forward)
                        def q_softmax_forward(*args: Any, **kwargs: Any) -> Any:
                            nn.functional.softmax = partial(q_softmax, prob_quantizer)
                            try:
                                return original_forward(*args, **kwargs)
                            finally:
                                nn.functional.softmax = original_softmax

                        def q_softmax_state_dict(
                            self: Any, destination: Any = None, prefix: str = "", keep_vars: bool = False
                        ) -> Any:
                            if destination is None:
                                destination = OrderedDict()
                                destination._metadata = OrderedDict()

                            if self.prob_quantizer is not None and hasattr(self.prob_quantizer, "scale"):
                                key = prefix + "prob_output_scale"
                                destination[key] = (
                                    self.prob_quantizer.scale.detach() if not keep_vars else self.prob_quantizer.scale
                                )

                            prob_quantizer = self.prob_quantizer
                            del self.prob_quantizer

                            super(type(self), self).state_dict(
                                destination=destination, prefix=prefix, keep_vars=keep_vars
                            )

                            self.prob_quantizer = prob_quantizer

                            return destination

                        def q_softmax_load_state_dict(
                            self: Any,
                            state_dict: Any,
                            prefix: str,
                            local_metadata: Any,
                            strict: bool,
                            missing_keys: Any,
                            unexpected_keys: Any,
                            error_msgs: Any,
                        ) -> None:
                            keys = list(state_dict.keys())

                            for name in keys:
                                to_remap = name[len(prefix) :]
                                if to_remap == "prob_output_scale":
                                    state_dict[prefix + "prob_quantizer.scale"] = state_dict[name]
                                    del state_dict[name]

                            super(type(self), self)._load_from_state_dict(
                                state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs
                            )

                        module.forward = q_softmax_forward
                        module.state_dict = MethodType(q_softmax_state_dict, module)  # type: ignore[assignment]
                        module._load_from_state_dict = MethodType(q_softmax_load_state_dict, module)

                    patch_softmax(module, module.prob_quantizer)


@log_errors
def in_place_replace_layer(
    model: nn.Module, config: Config, named_modules: dict[str, nn.Module], module_configs: dict[str, QuantizationConfig]
) -> None:
    """
    Replaces `nn.Linear`, `nn.Conv2d`, etc. marked for quantization in `module_configs` by their quantized module equivalent.
    """
    replace_count = {module_class.__name__: 0 for module_class in LAYER_TO_QUANT_LAYER_MAP.keys()}
    module_count = {module_class.__name__: 0 for module_class in LAYER_TO_QUANT_LAYER_MAP.keys()}

    for name, module in tqdm(named_modules.items()):
        module_name = module.__class__.__name__
        if type(module) in LAYER_TO_QUANT_LAYER_MAP:
            module_count[module_name] += 1

            # Some modules may be excluded.
            if name in module_configs:
                quant_module_class = LAYER_TO_QUANT_LAYER_MAP[type(module)]
                replace_count[module_name] += 1

                if hasattr(quant_module_class, "from_float"):
                    quant_module = quant_module_class.from_float(module, module_configs[name])
                    setattr_recursive(model, name, quant_module)
                    in_place_replace_ops.debug(name)
                else:
                    raise ValueError(f"The class {str(quant_module_class)} does not have a method `from_float`.")
        else:
            module_count[module_name] = module_count.get(module_name, 0) + 1

    row_format = "|{:^40}|{:^20}|{:^20}|"
    table = row_format.format("Original module", "Number original", "Number replaced") + "\n"
    for module_name, num_original in module_count.items():
        table += row_format.format(module_name, num_original, replace_count.get(module_name, 0)) + "\n"

    logger.info(f"Module replacement for quantization summary:\n{table}")

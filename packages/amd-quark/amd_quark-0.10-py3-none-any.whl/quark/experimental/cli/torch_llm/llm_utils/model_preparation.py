#
# Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
import os
import random
from typing import Dict, Optional, Tuple, Union

import numpy as np
import psutil  # type: ignore[import-untyped]
import torch
import torch.nn as nn
from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    Llama4ForCausalLM,
    Llama4ForConditionalGeneration,
    MllamaForConditionalGeneration,
    PreTrainedTokenizerBase,
)

from quark.shares.utils.import_utils import is_transformers_version_higher_or_equal

if is_transformers_version_higher_or_equal("4.55.1"):
    from transformers import Mxfp4Config  # type: ignore[attr-defined]
    from transformers.models.gpt_oss.modeling_gpt_oss import GptOssExperts

from transformers.models.dbrx.modeling_dbrx import DbrxExperts, DbrxForCausalLM
from transformers.models.llama4.modeling_llama4 import Llama4TextMoe

from quark.experimental.cli.torch_llm.module_replacement.dbrx_expert import DbrxExperts_
from quark.experimental.cli.torch_llm.module_replacement.replacement_utils import (
    replace_gptoss_experts_with_linear,
    replace_llama4_experts_with_sequential,
)
from quark.torch.utils import setattr_recursive

MODEL_NAME_KV_LAYERS_MAP = {
    "mllama": ["*language_model.*k_proj", "*language_model.*v_proj"],
    "llama4": ["*language_model.*.k_proj", "*language_model.*.v_proj"],
    "llama": ["*k_proj", "*v_proj"],
    "opt": ["*k_proj", "*v_proj"],
    "qwen2moe": ["*k_proj", "*v_proj"],
    "qwen2": ["*k_proj", "*v_proj"],
    "qwen": ["*c_attn"],
    "chatglm": ["*query_key_value"],
    "phi3": ["*qkv_proj"],
    "phi": ["*k_proj", "*v_proj"],
    "mistral": ["*k_proj", "*v_proj"],
    "mixtral": ["*k_proj", "*v_proj"],
    "gptj": ["*k_proj", "*v_proj"],
    "grok": ["*k_proj", "*v_proj"],
    "cohere": ["*k_proj", "*v_proj"],
    "dbrx": ["*Wqkv"],
    "deepseekv2v3": ["*kv_b_proj"],
    "deepseek": ["*k_proj", "*v_proj"],
    "gemma2": ["*k_proj", "*v_proj"],
    "gemma3_llm": ["*k_proj", "*v_proj"],
    "gemma3_mllm": ["*language_model.*k_proj", "*language_model.*v_proj"],
    "gptoss": ["*k_proj", "*v_proj"],
}

MODEL_NAME_Q_LAYERS_MAP = {
    "mllama": "*self_attn.q_proj",
    "llama4": "*language_model.*.q_proj",
    "llama": "*q_proj",
    "opt": "*q_proj",
    "qwen2moe": "*q_proj",
    "qwen2": "*q_proj",
    "chatglm": "*query_key_value",
    "phi3": "*qkv_proj",
    "phi": "*q_proj",
    "mistral": "*q_proj",
    "mixtral": "*q_proj",
    "gptj": "*q_proj",
    "grok": "*q_proj",
    "cohere": "*q_proj",
    "dbrx": ["*Wqkv"],
    "deepseek": "*q_proj",
    "deepseekv2v3": ["*q_a_proj", "*q_b_proj"],
    "gemma3_llm": "*q_proj",
    "gemma3_mllm": "*language_model.*q_proj",
}

MODEL_NAME_EXCLUDE_LAYERS_MAP = {
    "mllama": ["*lm_head", "*patch_embedding", "multi_modal_projector"],
    "llama4": [
        "multi_modal_projector*",
        "*feed_forward.router*",
        "*feed_forward.router*",
        "vision_model*",
        "*lm_head",
    ],  # quant language only, excluding vision part
    "llama": ["lm_head"],
    "opt": ["lm_head"],
    "qwen2moe": ["lm_head", "*.gate", "*.shared_expert_gate"],
    "qwen2": ["lm_head"],
    "qwen": ["lm_head"],
    "qwq": ["lm_head"],
    "chatglm": ["transformer.output_layer"],
    "phi3": ["lm_head"],
    "phi": ["lm_head"],
    "mistral": ["lm_head"],
    "mixtral": ["lm_head", "*.gate"],
    "gptj": ["lm_head"],
    "grok": ["lm_head", "*.gate"],
    "cohere": ["lm_head"],
    "dbrx": ["lm_head", "*router.layer"],
    "deepseek": ["lm_head", "*.gate"],
    "deepseekv2v3": ["lm_head", "*self_attn*", "*mlp.gate"],  # quant mlp and moe, excluding attn
    "olmo": ["lm_head"],
    "gemma2": ["lm_head"],
    "gemma3_llm": ["*lm_head"],
    "gemma3_mllm": ["*vision_tower*", "*multi_modal_projector*", "*lm_head"],
    "instella": ["lm_head"],
    "gptoss": ["*lm_head"],
}

MOE_MODEL_NAME_EXPERTS_LAYERS_MAP = {
    "llama4": ["*feed_forward.experts*", "*feed_forward.shared_expert*"],
    "deepseek": ["*.mlp.experts.*"],
    "grok": ["*.moe_block.experts.*"],
}

MODEL_NAME_PATTERN_MAP = {
    "Mllama": "mllama",
    "Llama4": "llama4",
    "Llama": "llama",
    "OPT": "opt",
    "Qwen2Moe": "qwen2moe",
    "QWen2": "qwen2",
    "QWen": "qwen",
    "ChatGLM": "chatglm",
    "Phi3": "phi3",
    "Phi": "phi",
    "Mistral": "mistral",
    "Mixtral": "mixtral",
    "GPTJ": "gptj",
    "Grok": "grok",
    "Cohere": "cohere",
    "dbrx": "dbrx",
    "DeepseekV": "deepseekv2v3",
    "Deepseek": "deepseek",
    "olmo": "olmo",
    "gemma2": "gemma2",
    "Gemma3ForCausalLM": "gemma3_llm",
    "Gemma3ForConditionalGeneration": "gemma3_mllm",
    "instella": "instella",
    "gptoss": "gptoss",
}


def get_tokenizer(
    ckpt_path: str,
    max_seq_len: int = 2048,
    model_type: str | None = None,
) -> PreTrainedTokenizerBase:
    print(f"Initializing tokenizer from {ckpt_path}")
    tokenizer = AutoTokenizer.from_pretrained(ckpt_path, padding_side="left", trust_remote_code=True)  # type: ignore[no-untyped-call]
    if model_type and model_type in ["qwen", "qwen2"]:
        # qwen2 use token id 151643 as pad and eos tokens
        tokenizer.pad_token = tokenizer.convert_ids_to_tokens(151643)
        tokenizer.eos_token = tokenizer.convert_ids_to_tokens(151643)

    if tokenizer.pad_token != "<unk>":
        tokenizer.pad_token = tokenizer.eos_token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    assert tokenizer.pad_token is not None, f"Pad token for {model_type} cannot be set!"

    return tokenizer


def prepare_for_moe_quant(model: nn.Module) -> None:
    if isinstance(model, (DbrxForCausalLM, Llama4ForConditionalGeneration, Llama4ForCausalLM)):
        for name, module in model.named_modules(remove_duplicate=False):
            if isinstance(module, DbrxExperts):
                new_experts = DbrxExperts_.from_float(module)
                setattr_recursive(model, name, new_experts)
                print(f"Module {name} has been replaced")
            elif isinstance(module, Llama4TextMoe):
                replace_llama4_experts_with_sequential(module, model.config.text_config)
    elif model.config.model_type == "gpt_oss":
        for name, module in model.named_modules(remove_duplicate=False):
            if isinstance(module, GptOssExperts):
                replace_gptoss_experts_with_linear(module)


def get_model(
    ckpt_path: str,
    data_type: str = "auto",
    device: str = "cuda",
    multi_gpu: bool = False,
    multi_device: bool = False,
    attn_implementation: str = "eager",
    trust_remote_code: bool = True,
) -> tuple[nn.Module, torch.dtype]:
    if data_type == "float16":
        model_dtype = torch.float16
    elif data_type == "bfloat16":
        model_dtype = torch.bfloat16
    elif data_type == "float32":
        model_dtype = torch.float32
    elif data_type == "auto":
        model_dtype = data_type
    else:
        raise ValueError(f"{data_type} not support for current model")
    config = AutoConfig.from_pretrained(ckpt_path, trust_remote_code=trust_remote_code)
    max_memory: dict[Union[int, str], Union[int, str]] | None = None
    if multi_device:
        device = "auto"
        max_memory = get_device_max_memory()
    if multi_gpu:
        device = "auto"
    if config.model_type == "mllama":
        model = MllamaForConditionalGeneration.from_pretrained(
            ckpt_path,
            device_map=device,
            torch_dtype=model_dtype,
            max_memory=max_memory,
            trust_remote_code=trust_remote_code,
            attn_implementation=attn_implementation,
        )
    elif config.model_type == "llama4":
        model = Llama4ForConditionalGeneration.from_pretrained(
            ckpt_path,
            device_map=device,
            torch_dtype=model_dtype,
            max_memory=max_memory,
            trust_remote_code=trust_remote_code,
            attn_implementation=attn_implementation,
        )
    elif config.model_type == "gpt_oss":
        quantization_config = Mxfp4Config(dequantize=True)  # type: ignore[attr-defined]
        model = AutoModelForCausalLM.from_pretrained(
            ckpt_path,
            device_map=device,
            torch_dtype=model_dtype,
            max_memory=max_memory,
            trust_remote_code=trust_remote_code,
            attn_implementation=attn_implementation,
            quantization_config=quantization_config,
        )
    else:
        try:
            model = AutoModelForCausalLM.from_pretrained(
                ckpt_path,
                device_map=device,
                torch_dtype=model_dtype,
                max_memory=max_memory,
                trust_remote_code=trust_remote_code,
                attn_implementation=attn_implementation,
            )
        except Exception as e:
            model = AutoModelForCausalLM.from_pretrained(
                ckpt_path,
                device_map=device,
                torch_dtype=model_dtype,
                max_memory=max_memory,
                trust_remote_code=trust_remote_code,
            )
    if multi_device and hasattr(model, "hf_device_map"):
        print("device_map:", model.hf_device_map)
    # For certain models, the attribute model.config._name_or_path is an empty string; enforce the setting here.
    model.config._name_or_path = ckpt_path

    model.eval()
    model_dtype = next(model.parameters()).dtype

    return model, model_dtype


def get_model_type(model: nn.Module) -> str:
    for k, v in MODEL_NAME_PATTERN_MAP.items():
        if k.lower() in type(model).__name__.lower():
            return v
    print(f"\n[INFO]: This model: {type(model).__name__.lower()} has not been tested with the example provided!")
    print("        There may be risks associated with model loading, algorithm configuration, and exporting.")
    print("        However, this does not mean that Quark definitively does not support this model.")
    print(
        "        If you choose to run this model, please add the model information to the `get_model_type` function in utils/model_preparation.py."
    )
    exit(2)


def save_model(
    model: nn.Module,
    tokenizer: PreTrainedTokenizerBase | None,
    save_dir: str,
) -> None:
    model.save_pretrained(save_dir, safe_serialization=True)
    if tokenizer is None and getattr(model.config, "_name_or_path", None):
        try:
            tokenizer = AutoTokenizer.from_pretrained(model.config._name_or_path, trust_remote_code=True)  # type: ignore[no-untyped-call]
            print(f"Save the tokenizer from pretrained: {model.config._name_or_path}")
        except Exception as e:
            print(f"An error occurred when loading tokenizer: {e}")
    if tokenizer is not None:
        tokenizer.save_pretrained(save_dir)


def set_seed(seed: int) -> None:
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True


def get_device_max_memory() -> dict[Union[int, str], Union[int, str]]:
    max_memory: dict[Union[int, str], Union[int, str]] = {}
    for i in range(torch.cuda.device_count()):
        _ = torch.tensor([0], device=i)
        cuda_avail_memory = {i: torch.cuda.mem_get_info(i)[0] for i in range(torch.cuda.device_count())}
        cpu_avail_memory = psutil.virtual_memory().available
        for cuda_num, cuda_memory in cuda_avail_memory.items():
            cuda_memory_gb = cuda_memory / (10**9)
            print(f"GPU{cuda_num} cuda_avail_memory: {cuda_memory_gb:.1f}GB")
            if cuda_num == 0:
                # The ratio is an experience value that you can manually adjust yourself.
                gpu0_ratio = 0.5 if cuda_memory_gb > 30 else 0.3
                max_memory[cuda_num] = f"{cuda_memory_gb * gpu0_ratio:.1f}GB"
            else:
                other_ratio = 0.875 if cuda_memory_gb > 30 else 0.7
                max_memory[cuda_num] = f"{cuda_memory_gb * other_ratio:.1f}GB"
        print(f"cpu_avail_memory: {cpu_avail_memory / (10**9):.1f}GB")
        cpu_ratio = 0.875
        max_memory["cpu"] = f"{cpu_avail_memory / (10**9) * cpu_ratio:.1f}GB"
        print("final_use_model_kwargs: ", max_memory)
        # max_memory =  {0: '0.1GB', 'cpu': '100GB'}

    return max_memory

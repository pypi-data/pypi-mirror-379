#
# Copyright (C) 2024, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import json
import multiprocessing
import os
from contextlib import contextmanager
from functools import partial
from pathlib import Path
from typing import Any, Collection, Dict, Iterable, Iterator, List, Optional, Tuple, Union

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdm import tqdm

from quark.shares.utils.import_utils import is_matplotlib_available, is_transformers_available
from quark.shares.utils.log import ScreenLogger
from quark.torch.quantization.config.config import Config
from quark.torch.quantization.nn.modules.mixin import QuantMixin
from quark.torch.quantization.nn.modules.quantize_linear import QuantLinear
from quark.torch.quantization.tensor_quantize import FakeQuantizeBase, ScaledFakeQuantize

if is_transformers_available():
    from transformers.feature_extraction_utils import BatchFeature

if is_matplotlib_available():
    import matplotlib.pyplot as plt

logger = ScreenLogger(__name__)

SAVE_ACTIVATIONS_HISTOGRAM = os.environ.get("QUARK_DEBUG_ACT_HIST", None) == "1"
DEBUG_INPUT_PICKLE = os.environ.get("QUARK_DEBUG_INPUT_PICKLE", None)

QUARK_DEBUG = os.environ.get("QUARK_DEBUG", "0") == "1"
QUARK_GRAPH_DEBUG = os.environ.get("QUARK_GRAPH_DEBUG", "0") == "1"

# Selects the Q/DQ/QDQ implementation to use with mxfp4.
# Available: "hip", "triton". Default is "hip".
QUARK_MXFP4_IMPL = os.environ.get("QUARK_MXFP4_IMPL", "hip")

QUARK_ALGO_DEBUG = os.environ.get("QUARK_ALGO_DEBUG", "0") == "1"


def weight_stats_hook(
    module: FakeQuantizeBase,
    args: tuple[Any, ...],
    output: torch.Tensor,
    module_name: str,
    log_dir: Path,
    n_bins: int,
    stats: dict[str, Any],
) -> None:
    """
    Hook to collect statistics on the weight and bias quantization. This hook should only be attached to `FakeQuantizeBase` layers corresponding to weight and bias quantization.

    This hook should be attached with https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_forward_hook.

    Args:
        module (FakeQuantizeBase): The torch.nn.Module this hook is being attached to.
        args (Tuple[Any, ...]): The module inputs, as specified in `torch.nn.Module.register_forward_hook` documentation.
        output (torch.Tensor): The module output, as specified in `torch.nn.Module.register_forward_hook` documentation.
        module_name (str): The module name, set with `functools.partial`. This is useful to access the module name from within the hook.
        log_dir (Path): The directory the weight statistics will be saved to, set with `functools.partial`.
        n_bins (int): The number of bins inthe histograms of values that are saved for visualization.
        stats (Dict[str, Any]): The dictionary used to store statistics on the weight and bias quantization. It can be set using an empty handle using `functools.partial`. Passing a dictionary is useful to access outside of the hook its content that was modified from within the hook.
    """
    if module_name not in stats:
        if "_weight_quantizer" in module_name:
            quantizer_type = "weight"
        elif "_bias_quantizer" in module_name:
            quantizer_type = "bias"

        stats[module_name] = {"quantizer_type": quantizer_type, "module_name": module_name}

    with torch.no_grad():
        input_tensor = args[0].to(torch.float32)
        stats[module_name]["shape"] = input_tensor.shape
        quantized_tensor = output.to(torch.float32)

        if module.fake_quant_enabled and "l1_error" not in stats[module_name]:
            # Maximum entropy would be with an uniform distribution, all the quantization bins filled equally.
            # We should also compute the entropy of the quantized weight distribution, but it is a bit expensive with QDQ so not doing it for now.
            reference_entropy = -torch.sum(1 / n_bins * torch.log(torch.full((n_bins,), 1 / n_bins))).item()

            l1_error = (input_tensor - quantized_tensor).abs().max().item()

            stats[module_name]["l1_error"] = l1_error
            tensor_stats = {"l1_error": l1_error, "theorical_q_entropy": reference_entropy}

            short_module_name = module_name.replace("_weight_quantizer", "weight").replace("_bias_quantizer", "bias")
            with open(Path(log_dir, short_module_name + "_stats.json"), "w") as fp:
                json.dump(tensor_stats, fp)

        if "histogram" not in stats[module_name]:
            histogram = torch.histogram(input_tensor.flatten().cpu(), bins=100)
            stats[module_name]["histogram"] = (histogram[0].numpy(), histogram[1].numpy())


def activation_stats_hook(
    module: FakeQuantizeBase, args: tuple[Any, ...], output: torch.Tensor, module_name: str, stats: dict[str, Any]
) -> None:
    """
    Hook to collect statistics on the activation quantization. This hook should only be attached to `FakeQuantizeBase` layers corresponding to input/output quantization.
    """
    if not module.fake_quant_enabled:
        quantizer_enabled = False
    else:
        quantizer_enabled = True

    assert isinstance(args, tuple)
    assert isinstance(args[0], torch.Tensor)
    input_tensor = args[0].to(torch.float32)

    if not quantizer_enabled:
        stats[module_name]["ref_input_tensor"] = input_tensor
        stats[module_name]["ref_output_tensor"] = input_tensor  # For non-quantized models, QDQ is a no-op.

        if SAVE_ACTIVATIONS_HISTOGRAM:
            if "input_ref_histogram" not in stats[module_name]:
                histogram = torch.histogram(input_tensor.flatten().cpu(), bins=100)
                tuple_histogram = (histogram[0].numpy(), histogram[1].numpy())
                stats[module_name]["input_ref_histogram"] = tuple_histogram

            if "input_ref_histogram_absmean_ch0" not in stats[module_name]:
                histogram = torch.histogram(input_tensor.abs().mean(dim=-2).flatten().cpu(), bins=100)
                tuple_histogram = (histogram[0].numpy(), histogram[1].numpy())
                stats[module_name]["input_ref_histogram_absmean_ch0"] = tuple_histogram

            if "input_ref_histogram_absmean_ch1" not in stats[module_name]:
                histogram = torch.histogram(input_tensor.abs().mean(dim=-1).flatten().cpu(), bins=100)
                tuple_histogram = (histogram[0].numpy(), histogram[1].numpy())
                stats[module_name]["input_ref_histogram_absmean_ch1"] = tuple_histogram
    else:
        ref_input_tensor = stats[module_name]["ref_input_tensor"]
        ref_output_tensor = stats[module_name]["ref_output_tensor"]
        quantized_tensor = output.to(torch.float32)

        def reldiff(x: torch.Tensor, ref: torch.Tensor, eps: float = 1e-12) -> float:
            # Compute relative difference in high precision.
            ref = ref.to(torch.float32)
            x = x.to(torch.float32)

            reldiff = (x - ref).abs() / (ref.abs() + eps)
            assert torch.all(torch.isfinite(reldiff))
            return reldiff.mean().item()

        # Compare input tensor of FakeQuantizeBase to reference input tensor (non-quantized model).
        stats[module_name]["l1_ref_input"].append(reldiff(input_tensor, ref_input_tensor))

        # Compare output tensor of FakeQuantizeBase to reference output tensor (non-quantized model).
        stats[module_name]["l1_ref_output"].append(reldiff(quantized_tensor, ref_output_tensor))

        # Compare output tensor of FakeQuantizeBase to its input tensor.
        stats[module_name]["l1_io_error"].append(reldiff(quantized_tensor, input_tensor))

        if SAVE_ACTIVATIONS_HISTOGRAM and "input_histogram" not in stats[module_name]:
            histogram = torch.histogram(input_tensor.flatten().cpu(), bins=100)
            stats[module_name]["input_histogram"] = (histogram[0].numpy(), histogram[1].numpy())

        if SAVE_ACTIVATIONS_HISTOGRAM and "input_qdq_histogram" not in stats[module_name]:
            histogram = torch.histogram(quantized_tensor.flatten().cpu(), bins=100)
            stats[module_name]["input_qdq_histogram"] = (histogram[0].numpy(), histogram[1].numpy())


def distribution_plot(
    histogram: tuple[np.ndarray, np.ndarray],  # type: ignore[type-arg]
    save_path: Union[str, Path],
    title: str,
) -> None:
    """
    Plots and saves a bar plot using the bins and distribution from `histogram`. This is useful to save a given layer distribution, error, etc.
    """
    hist, bins = histogram
    width = bins[1] - bins[0]
    center = (bins[:-1] + bins[1:]) / 2
    plt.clf()
    plt.bar(center, hist, edgecolor="black", fill=True, align="center", width=width, linewidth=0.5)
    plt.axvline(bins.min(), color="r", label="min tensor value")
    plt.axvline(bins.max(), color="r", label="max tensor value")
    plt.legend()
    plt.title(title, fontsize=14)
    plt.grid()
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)


def barplot(labels: Collection[str], values: Iterable[float], name: str, log_dir: Union[str, Path]) -> None:
    """
    Plots and saves a bar plot summary of values, each value having a label. This is useful to plot a summary of e.g. quantization error over many layers.
    """
    x_range = range(len(labels))
    plt.clf()
    plt.figure(figsize=(2 + int(0.2 * len(x_range)), 5))  # Dynamic x axis size to avoid having its ticks overlap.
    plt.bar(x_range, list(values), edgecolor="black")
    plt.xticks(x_range, list(labels), rotation=65, fontsize=9, ha="right", rotation_mode="anchor")
    plt.xlim([-1, len(x_range)])
    plt.grid()
    plt.savefig(Path(log_dir, f"{name}.png"), dpi=300, bbox_inches="tight")


def save_distribution_histogram(module_name: str, tensor_stats: dict[str, Any], log_dir: str) -> None:
    """
    Saves bar plots of activations. Utility function to be used by multiprocessing.
    """
    input_shape_str = str(tuple(tensor_stats["ref_input_tensor"].shape))

    quantizer_type = tensor_stats["quantizer_type"]

    module_name = module_name.replace("_input_quantizer", "").replace("_output_quantizer", "")

    # Plot the histogram of values of the reference inputs at the point the FakeQuantize layer is inserted (input or output of a module).
    histogram_file = Path(log_dir, module_name + f"{quantizer_type}_ref_histogram.png")
    distribution_plot(
        tensor_stats["input_ref_histogram"],
        histogram_file,
        title=module_name + f"\nref input histogram (tensor={input_shape_str})",
    )

    # Plot the histogram of values of the reference inputs at the point the FakeQuantize layer is inserted, absmean reduced on the -2 dimension.
    histogram_file = Path(log_dir, module_name + f"{quantizer_type}_ref_histogram_absmean_ch0.png")
    reduced_shape_str = str(
        tuple(tensor_stats["ref_input_tensor"].shape[:-2] + tensor_stats["ref_input_tensor"].shape[-1:])
    )
    distribution_plot(
        tensor_stats["input_ref_histogram_absmean_ch0"],
        histogram_file,
        title=module_name
        + f"\nref input histogram, absmean ch0 (tensor={input_shape_str})\nreduction over -2 dim (tensor={reduced_shape_str})",
    )

    # Plot the histogram of values of the reference inputs at the point the FakeQuantize layer is inserted, absmean reduced on the -1 dimension.
    histogram_file = Path(log_dir, module_name + f"{quantizer_type}_ref_histogram_absmean_ch1.png")
    reduced_shape_str = str(tuple(tensor_stats["ref_input_tensor"].shape[:-1]))
    distribution_plot(
        tensor_stats["input_ref_histogram_absmean_ch1"],
        histogram_file,
        title=module_name
        + f"\nref input histogram, absmean ch1 (tensor={input_shape_str})\nreduction over -1 dim (tensor={reduced_shape_str})",
    )

    # Plot the histogram of values of the activation inputs to the FakeQuantize layer.
    histogram_file = Path(log_dir, module_name + f"{quantizer_type}_histogram.png")
    distribution_plot(
        tensor_stats["input_histogram"],
        histogram_file,
        title=module_name + f"\ninput histogram (tensor={input_shape_str})",
    )

    # Plot the histogram of values of the activation outputs of the FakeQuantize layer (after QDQ).
    histogram_file = Path(log_dir, module_name + f"{quantizer_type}_qdq_histogram.png")
    distribution_plot(
        tensor_stats["input_qdq_histogram"],
        histogram_file,
        title=module_name + f"\nqdq input histogram (tensor={input_shape_str})",
    )


def summarize_weight(stats: dict[str, Any], log_dir: Path) -> None:
    """
    Saves a histogram of the distribution of the weight tensor for each weight tracked. Saves as well a summary plot of the L1 quantization error over all the different weight tensors.
    """
    l1_errors_weights = {}

    distribution_plot_args = []

    # Plot the non-quantized weight distribution per layer.
    for module_name, tensor_stats in tqdm(stats.items(), desc="plot weight distribution"):
        if tensor_stats["quantizer_type"] in ["weight", "bias"]:
            module_name_short = module_name.replace("._weight_quantizer", "_w").replace("._bias_quantizer", "_b")

            l1_errors_weights[module_name_short] = tensor_stats["l1_error"]

            module_name = module_name.replace("._weight_quantizer", "").replace("._bias_quantizer", "")
            histogram_file = Path(log_dir, module_name + ".weight.png")
            shape_str = str(tuple(tensor_stats["shape"]))
            distribution_plot_args.append(
                (tensor_stats["histogram"], histogram_file, module_name + f"\n weight histogram (tensor= {shape_str})")
            )

    start_method = multiprocessing.get_start_method()
    multiprocessing.set_start_method("spawn", force=True)
    pool = multiprocessing.Pool(processes=32)

    for _ in tqdm(pool.starmap(distribution_plot, distribution_plot_args), total=len(distribution_plot_args)):
        pass

    pool.close()
    pool.join()

    if start_method is not None:
        multiprocessing.set_start_method(start_method, force=True)

    # Plot the summary of weight quantization error over each layers.
    barplot(l1_errors_weights.keys(), l1_errors_weights.values(), name="summary_weight_error", log_dir=log_dir)


def summarize_activation(stats: dict[str, Any], log_dir: Path) -> None:
    """
    Saves a summary over all activations of the error between the quantized / non-quantized model.
    """
    l1_errors_ref_input = {}
    l1_errors_ref_output = {}
    l1_io_error = {}

    # Average the activation metrics over all the input samples used in the statistics collection.
    for name, tensor_stats in stats.items():
        if tensor_stats["quantizer_type"] in ["input", "output"]:
            l1_errors_ref_input[name] = np.mean(tensor_stats["l1_ref_input"])
            l1_io_error[name] = np.mean(tensor_stats["l1_io_error"])
            l1_errors_ref_output[name] = np.mean(tensor_stats["l1_ref_output"])

    # Plot the summary of relative error of input tensor of FakeQuantizeBase compared to reference input tensor (non-quantized model).
    labels = [
        key.replace("._input_quantizer", "_i").replace("._output_quantizer", "_o") for key in l1_errors_ref_input.keys()
    ]
    barplot(labels, l1_errors_ref_input.values(), name="summary_ref_input_error", log_dir=log_dir)

    # Plot the summary of relative error of output tensor of FakeQuantizeBase compared to reference output tensor (non-quantized model).
    labels = [
        key.replace("._input_quantizer", "_i").replace("._output_quantizer", "_o")
        for key in l1_errors_ref_output.keys()
    ]
    barplot(labels, l1_errors_ref_output.values(), name="summary_ref_output_error", log_dir=log_dir)

    # Plot the summary of relative error of output tensor of FakeQuantizeBase compared to its input tensor.
    labels = [key.replace("._input_quantizer", "_i").replace("._output_quantizer", "_o") for key in l1_io_error.keys()]
    barplot(labels, l1_io_error.values(), name="summary_io_quantization_error", log_dir=log_dir)

    if SAVE_ACTIVATIONS_HISTOGRAM:
        save_distribution_args = [
            (module_name, tensor_stats, log_dir)
            for module_name, tensor_stats in stats.items()
            if tensor_stats["quantizer_type"] in ["input", "output"]
        ]

        start_method = multiprocessing.get_start_method()
        multiprocessing.set_start_method("spawn", force=True)
        pool = multiprocessing.Pool(processes=32)

        for _ in tqdm(
            pool.starmap(save_distribution_histogram, save_distribution_args), total=len(save_distribution_args)
        ):
            pass

        pool.close()
        pool.join()

        if start_method is not None:
            multiprocessing.set_start_method(start_method, force=True)


@contextmanager
def insert_stats_hooks(model: nn.Module, stats: dict[str, Any], log_dir: Path) -> Iterator[None]:
    """
    Inserts the hooks to track statistics about quantization error.
    """
    hooks = []
    for name, module in model.named_modules():
        if isinstance(module, FakeQuantizeBase):
            if "weight_quantizer" in name or "bias_quantizer" in name:
                hook = module.register_forward_hook(
                    partial(weight_stats_hook, module_name=name, log_dir=log_dir, n_bins=256, stats=stats)
                )
                hooks.append(hook)
            elif "input_quantizer" in name or "output_quantizer" in name:
                hook = module.register_forward_hook(partial(activation_stats_hook, module_name=name, stats=stats))
                hooks.append(hook)

    yield

    for hook in hooks:
        hook.remove()


def collect_quantization_statistics(
    model: nn.Module,
    dataloader: Union[
        DataLoader[torch.Tensor],
        DataLoader[list[dict[str, torch.Tensor]]],
        DataLoader[dict[str, torch.Tensor]],
        DataLoader[list["BatchFeature"]],
    ]
    | None,
    stats: dict[str, Any],
    log_dir: Path,
) -> None:
    """
    Collects (through the hooks attached to the model) statistics on the operators inputs/outputs to compute quantization error metrics, as well as on the weights.

    Moreover, this function writes to disk statistics, distribution and summary bar charts for the quantization of weights and activations.
    """
    if not is_matplotlib_available():
        raise ImportError(
            "The package `matplotlib` is required to collect quantization error statistics and plot them. Please install `matplotlib` (example: `pip install matplotlib`)."
        )

    if DEBUG_INPUT_PICKLE is None:
        if SAVE_ACTIVATIONS_HISTOGRAM:
            logger.warning(
                "The histograms of activations / activation errors are saved only for the first item in the dataloader. Please make sure that this input is meaningful, and bear in mind that this item was used as well for calibration. In order to use specific inputs to collect activation quantization statistics, please specify the environment variable `QUARK_DEBUG_INPUT_PICKLE` to a file containing the reference tensor or dict inputs saved with `torch.save`."
            )

        input_iterable: Iterable[Any] | None = dataloader
    else:
        input_dict = torch.load(DEBUG_INPUT_PICKLE, weights_only=True)
        input_iterable = [input_dict]

    if input_iterable is not None:
        for module_name, module in model.named_modules():
            if isinstance(module, FakeQuantizeBase) and (
                "input_quantizer" in module_name or "output_quantizer" in module_name
            ):
                if "input_quantizer" in module_name:
                    quantizer_type = "input"
                else:
                    quantizer_type = "output"

                if module_name not in stats:
                    stats[module_name] = {
                        "l1_ref_input": [],
                        "l1_io_error": [],
                        "l1_ref_output": [],
                        "quantizer_type": quantizer_type,
                    }
                else:
                    stats[module_name]["l1_ref_input"] = []
                    stats[module_name]["l1_io_error"] = []
                    stats[module_name]["l1_ref_output"] = []
                    stats[module_name]["quantizer_type"] = quantizer_type

        for data in tqdm(input_iterable, desc="Debug forward"):
            for module in model.modules():
                if isinstance(module, FakeQuantizeBase):
                    module.disable_fake_quant()

            with torch.no_grad():
                if (
                    isinstance(data, dict) or is_transformers_available() and isinstance(data, BatchFeature)
                ):  # pragma: no cover
                    _ = model(**data)
                else:
                    _ = model(data)

            for module in model.modules():
                if isinstance(module, FakeQuantizeBase):
                    module.enable_fake_quant()

            with torch.no_grad():
                if (
                    isinstance(data, dict) or is_transformers_available() and isinstance(data, BatchFeature)
                ):  # pragma: no cover
                    _ = model(**data)
                else:
                    _ = model(data)
    else:
        for module in model.modules():
            if isinstance(module, FakeQuantizeBase):
                module.enable_fake_quant()

        for module in tqdm(model.modules()):
            if isinstance(module, QuantMixin):
                if module._weight_quantizer is not None:
                    module.get_quant_weight(module.weight)
                if module._bias_quantizer is not None:
                    module.get_quant_bias(module.bias)

    summarize_weight(stats, log_dir)
    if input_iterable is not None:
        summarize_activation(stats, log_dir)


class QuantizerStatsHelper:
    def __init__(self, quantizer: ScaledFakeQuantize, quantizer_type: str, module_name: str, summary: dict[str, Any]):
        assert isinstance(quantizer, ScaledFakeQuantize)
        self.quantizer = quantizer
        summary[quantizer_type] = {}
        self.summary = summary[quantizer_type]
        self.quantizer_type = quantizer_type
        self.moudule_name = module_name

    def get_scale_min_max(self) -> tuple[Any, Any]:
        return self.quantizer.scale.min().item(), self.quantizer.scale.max().item()

    def check_scale(self) -> None:
        self.summary["scale_shape"] = self.quantizer.scale.shape
        self.summary["scale_dtype"] = str(self.quantizer.scale.dtype)

        min_max = self.get_scale_min_max()
        self.summary["scale_min_max"] = min_max
        is_zero = min_max[0] == 0.0
        if is_zero:
            logger.warning(
                f"{self.moudule_name + '.' + self.quantizer_type} has zero scale. This may lead to incorrect quantization."
            )
        self.summary["has_zero_scale"] = is_zero


class ModuleStatsHelper:
    def __init__(self, module_name: str, module: nn.Module, summary: dict[str, Any]):
        self.input_quantizer = None
        self.weight_quantizer = None
        self.output_quantizer = None
        self.bias_quantizer = None

        self.module = module

        summary[module_name] = {}
        self.summary = summary[module_name]

        if module.input_quantizer is not None and isinstance(module.input_quantizer, ScaledFakeQuantize):
            self.input_quantizer = QuantizerStatsHelper(
                module.input_quantizer, "_input_quantizer", module_name, self.summary
            )
        if module.weight_quantizer is not None and isinstance(module.weight_quantizer, ScaledFakeQuantize):
            self.weight_quantizer = QuantizerStatsHelper(
                module.weight_quantizer, "_weight_quantizer", module_name, self.summary
            )
        if module.output_quantizer is not None and isinstance(module.output_quantizer, ScaledFakeQuantize):
            self.output_quantizer = QuantizerStatsHelper(
                module.output_quantizer, "_output_quantizer", module_name, self.summary
            )
        if module.bias_quantizer is not None and isinstance(module.bias_quantizer, ScaledFakeQuantize):
            self.bias_quantizer = QuantizerStatsHelper(
                module.bias_quantizer, "_bias_quantizer", module_name, self.summary
            )

    def check_scale(self) -> None:
        self.summary["weight_shape"] = self.module.weight.shape
        if self.module.bias is not None:
            self.summary["bias_shape"] = self.module.bias.shape
        if self.input_quantizer is not None:
            self.input_quantizer.check_scale()
        if self.weight_quantizer is not None:
            self.weight_quantizer.check_scale()
        if self.output_quantizer is not None:
            self.output_quantizer.check_scale()
        if self.bias_quantizer is not None:
            self.bias_quantizer.check_scale()


SCALE_DEBUG_DIR = "./debug_scale"
SCALE_STATS_FILE = "scale_stats.json"
CHECK_MODULE = QuantLinear


def check_scale_stats(model: nn.Module, config: Config) -> None:
    """
    Check the scale of the model's quantizer.
    """
    summary = {}
    summary["quantization_config"] = config.to_dict()
    summary["scale_stats"] = {}
    for module_name, module in model.named_modules():
        if isinstance(module, CHECK_MODULE):
            module_stats = ModuleStatsHelper(module_name, module, summary["scale_stats"])
            module_stats.check_scale()

    # save to file
    os.makedirs(SCALE_DEBUG_DIR, exist_ok=True)
    save_file = SCALE_DEBUG_DIR + "/" + SCALE_STATS_FILE
    with open(save_file, "w") as f:
        json.dump(summary, f, indent=4)
    logger.info(f"Saving scale stats to {save_file}")

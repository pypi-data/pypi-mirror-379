#
# Copyright (C) 2024, Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
from typing import Callable

import torch.fx

import quark.torch.quantization.graph.optimization.post_calib as opt_post_calib_pass
import quark.torch.quantization.graph.optimization.post_quant.opt_pass_after_quant_float_scale as opt_post_qt_fs_pass
import quark.torch.quantization.graph.optimization.post_quant.opt_pass_after_quant_powof2_scale as opt_post_qt_pow2_pass
import quark.torch.quantization.graph.optimization.pre_quant.opt_pass_before_quant as opt_pre_qt_pass
from quark.shares.utils.log import ScreenLogger
from quark.torch.quantization.config.config import Config, QuantizationConfig, QuantizationSpec
from quark.torch.quantization.graph.optimization.opt_pass_manager import OptPassManager
from quark.torch.quantization.graph.optimization.pre_quant.convert_scalars_to_attrs import convert_scalars_to_attrs
from quark.torch.quantization.graph.optimization.pre_quant.cross_layer_equaliztion import (
    cross_layer_equalization,
    get_cle_pattern_pair,
)
from quark.torch.quantization.graph.optimization.pre_quant.fold_bn_after_concat import fold_bn_after_concat
from quark.torch.quantization.graph.optimization.pre_quant.modify_reshape_param import modify_reshape_param
from quark.torch.quantization.graph.optimization.pre_quant.replace_conv2d_to_qtconv2d import replace_conv2d_qtconv2d
from quark.torch.quantization.graph.optimization.pre_quant.replace_conv_bn_to_qt_model import (
    replace_conv2dbn_quantizedconv_module,
)
from quark.torch.quantization.graph.optimization.pre_quant.replace_convtranspose2d_to_qtconvtranspose2d import (
    replace_convtranspose2d_qtconvtranspose2d,
)

# Graph
# before quant optimization
from quark.torch.quantization.graph.optimization.pre_quant.replace_linear_to_qtlinear import replace_linear_qtlinear
from quark.torch.quantization.graph.optimization.pre_quant.replace_silu_2_sigmoid_mul import replace_silu_node
from quark.torch.quantization.graph.optimization.pre_quant.replace_transposeconv_bn_to_qt_model import (
    replace_transposeconv2dbn_quantconv_module,
)

# post quant optimization
from quark.torch.quantization.graph.torch_utils import (
    ADAPTIVE_AVG_POOL_OP,
    AVG_POOL_2D_OP,
    MAX_POOL_2D_OP,
    POW_OF_2_OBSERVER,
    SLICE_OP,
)
from quark.torch.quantization.nn.modules import QuantAdaptiveAvgPool2d, QuantAvgPool2d

logger = ScreenLogger(__name__)

__all__ = [
    "trans_opsfunc_2_quant_module",
    "apply_pre_hw_constrain_passes",
    "_apply_post_hw_powof2_constrain_passes",
    "select_proper_hw_constrain_passes",
    "fx_model_cross_layer_equalization",
]
"""
==========================================
optimize function used befor quantization
==========================================
"""


def trans_opsfunc_2_quant_module(model: torch.fx.GraphModule) -> torch.fx.GraphModule:
    """
    optimize the pure torch.ops.aten.*** functional model,
    replace the op like (linear, conv2d, transposeconv2d) to corresponding Quant module for bettter PTQ/QAT
    """
    # 0: [ops.aten.conv2d -> ops.aten.cudnn_batch_norm] -> QuantizedConvBatchNorm2d
    # TODO further refin 1.if CLE etc. con + bn -> qconv 2. IF NO FOLD: conv + vn -> QuantizedConvBatchNorm2d
    model = replace_conv2dbn_quantizedconv_module(model)
    # 1. [ops.aten.conv_transpose2d -> ops.aten.cudnn_batch_norm] -> QuantConvTransposeBatchNorm2d
    model = replace_transposeconv2dbn_quantconv_module(model)
    # 2. [multi ops.aten{conv, transposeconv} -> cat-> bn] to [multi ops.aten{conv, transposeconv} -> cat ->]
    model = fold_bn_after_concat(model)
    # 3. [ops.aten.linear] -> QuantLinear
    model = replace_linear_qtlinear(model)
    # 4. [ops.aten.conv2d] -> QuantConv2d
    model = replace_conv2d_qtconv2d(model)
    # 5. [ops.aten.conv_transpose2d] -> QuantConvTranspose2d
    model = replace_convtranspose2d_qtconvtranspose2d(model)
    # 6. change ops.aten,reshape param
    model = modify_reshape_param(model)
    # 7. convert scatal to tensor attrs
    model = convert_scalars_to_attrs(model)
    # 8. convert silu -> x * sigmoid(x)
    model = replace_silu_node(model)
    return model


def apply_pre_hw_constrain_passes(model: torch.fx.GraphModule) -> torch.fx.GraphModule:
    pass_manager = OptPassManager()
    # 1. Transfer the shared module to multiple copies where it is called.
    pass_manager.add_pass(opt_pre_qt_pass.SplitQuantModuleCalledOverOnce())
    # 2. transfer single bn to conv2d layer
    pass_manager.add_pass(opt_pre_qt_pass.ConvertBn2D2ConvQOPass())

    # 3. transfer mean bn to globalavgpooling(adaptive_avg_pool2d) layer if appliable
    pass_manager.add_pass(opt_pre_qt_pass.ConvertReduceMean2GapQOPass())
    # 4. split large global average pooling to smaler two pooling layer
    pass_manager.add_pass(opt_pre_qt_pass.SplitLargeKernelPoolQOPass())
    # 5. transfer aten.adaptive_avg_pool2d to QuantAdaptiveAvgPool2d (with NPU constrain)
    pass_manager.add_pass(opt_pre_qt_pass.ConvertAdaptiveavgpool2d2Quantadaptiveavgpool2DQOPass())
    # 6. transfer [aten.avg_pool2d] to QuantAvgPool2d
    pass_manager.add_pass(opt_pre_qt_pass.ConverAvgpool2d2QuantAvgPool2dQOPass())

    # 7. transfer split to slice
    pass_manager.add_pass(opt_pre_qt_pass.ConvertSplit2SliceQOPass())
    # 8. remove redundant slice op
    pass_manager.add_pass(opt_pre_qt_pass.ConvertDeleteRedundantSliceQOPass())
    # 9. change sigmoid to hardsigmoid
    pass_manager.add_pass(opt_pre_qt_pass.ConvertSigmoid2HardSigmoidQOPass())
    # 10. change silu to hardswish
    pass_manager.add_pass(opt_pre_qt_pass.ConvertSilu2HardswishQOPass())
    # 11. change ops.aten.leaky_relu to QuantLeakyReLU
    pass_manager.add_pass(opt_pre_qt_pass.ConvertLeakyReLu2QuantLeakyReLuQOPass())
    model = pass_manager(model)
    return model


def fx_model_cross_layer_equalization(model: torch.fx.GraphModule) -> torch.fx.GraphModule:
    cle_pattern_pair_list = get_cle_pattern_pair(model)
    cross_layer_equalization(model, cle_pattern_pair_list)
    return model


"""
==========================================
optimize function used during quantization
==========================================
"""


# after PTQ, we perform the optimization
def apply_post_calib_optimize_passes(model: torch.fx.GraphModule) -> torch.fx.GraphModule:
    pass_manager = OptPassManager()
    # 1. if bias is int32 quant format, then scale_bias = scale_w * scale_a , applied for conv/linear
    pass_manager.add_pass(opt_post_calib_pass.AdjustBiasScaleQOPass())
    model = pass_manager(model)
    return model


"""
==========================================
optimize function used after quantization
==========================================
"""


def _apply_post_hw_powof2_constrain_passes(model: torch.fx.GraphModule) -> torch.fx.GraphModule:
    pass_manager = OptPassManager()
    # 1. transfer clip to relu
    pass_manager.add_pass(opt_post_qt_pow2_pass.ConvertClip2ReLUQOPass())
    # 2. Align the Quantizer's scale to equal for cat's input and output (quark/onnx/refine.py: align_concat)
    pass_manager.add_pass(opt_post_qt_pow2_pass.ApplyConstrain2ConcatQOPass())
    # 3. Align Pool's input & output quantizer (quark/onnx/refine.py: align_pool)
    pass_manager.add_pass(
        opt_post_qt_pow2_pass.AlignSingleInOutOpScaleQOPass([MAX_POOL_2D_OP, AVG_POOL_2D_OP, ADAPTIVE_AVG_POOL_OP])
    )
    pass_manager.add_pass(
        opt_post_qt_pow2_pass.AlignSingleInOutModuleScaleQOPass(
            (  # type: ignore[arg-type]
                QuantAvgPool2d,
                QuantAdaptiveAvgPool2d,
            )
        )
    )

    # TODO manager.align_pad()
    # pass_manager.add_pass(opt_post_qt_pass.AlignSingleInOutOpScaleQOPass([PAD_OP]))

    # 4. Align slice's op input & output quantizer (quark/onnx/refine.py: align_slice)
    pass_manager.add_pass(opt_post_qt_pow2_pass.AlignSingleInOutOpScaleQOPass([SLICE_OP]))
    # 5. Align (quark/onnx/refine.py: adjust_shift_read)
    pass_manager.add_pass(opt_post_qt_pow2_pass.AdjustShiftReadQOPass())
    # 6. Align (quark/onnx/refine.py: adjust_shift_write)
    pass_manager.add_pass(opt_post_qt_pow2_pass.AdjustShiftWriteQOPass())
    # 7. Align (quark/onnx/refine.py: adjust_shift_cut)
    pass_manager.add_pass(opt_post_qt_pow2_pass.AdjustShiftCutQOPass())
    # 8. Align (quark/onnx/refine.py: adjust_shift_bias)
    pass_manager.add_pass(opt_post_qt_pow2_pass.AdjustShiftBiasQOPass())
    # 8. Align (quark/onnx/refine.py: adjust_hard_sigmoid)
    pass_manager.add_pass(opt_post_qt_pow2_pass.AdjustHardSigmoidQOPass())
    # 9. Align (quark/onnx/refine.py: adjust_shift_swish)
    pass_manager.add_pass(opt_post_qt_pow2_pass.AdjustShiftSwishQOPass())
    # 10. Align (quark/onnx/simulate_dpu.py: convert_hard_sigmoid_to_dpu_version)
    pass_manager.add_pass(opt_post_qt_pow2_pass.ConvertHardSigmoidDpuVersionQOPass())

    model = pass_manager(model)
    return model


def _apply_post_hw_fs_constrain_passes(model: torch.fx.GraphModule) -> torch.fx.GraphModule:
    pass_manager = OptPassManager()
    # 1. Align (quark/onnx/refine.py::QuantInfoManager::align_concat)
    pass_manager.add_pass(opt_post_qt_fs_pass.AlignConcatQOPass())

    # 2. Align (quark/onnx/refine.py::QuantInfoManager::align_pool)
    pass_manager.add_pass(opt_post_qt_fs_pass.AlignPoolQOPass())

    # 3. Align (quark/onnx/refine.py::QuantInfoManager::align_pad)
    pass_manager.add_pass(opt_post_qt_fs_pass.AlignPadQOPass())

    # 4. Align (quark/onnx/refine.py::QuantInfoManager::align_slice)
    pass_manager.add_pass(opt_post_qt_fs_pass.AlignSliceQOPass())

    # 5. Align (quark/onnx/refine.py::QuantInfoManager::align_transpose)
    pass_manager.add_pass(opt_post_qt_fs_pass.AlignTransposeQOPass())

    # 6. Align (quark/onnx/refine.py::QuantInfoManager::align_reshape)
    pass_manager.add_pass(opt_post_qt_fs_pass.AlignReshapeQOPass())

    # 7. Align (quark/onnx/refine.py::QuantInfoManager::adjust_bias_scale)
    pass_manager.add_pass(opt_post_calib_pass.AdjustBiasScaleQOPass())

    model = pass_manager(model)
    return model


def select_proper_hw_constrain_passes(config: Config) -> Callable[[torch.fx.GraphModule], torch.fx.GraphModule]:
    # NOTE this is a temporanr function
    # as currently we decide the pow-of-2 or float scale optimization only decided by the observer
    if config.global_quant_config is None:
        call_func = _apply_post_hw_powof2_constrain_passes

    # we need to chack the input/output/bias/weight
    quant_config: QuantizationConfig = config.global_quant_config
    in_obs = (
        quant_config.input_tensors.observer_cls if isinstance(quant_config.input_tensors, QuantizationSpec) else None
    )
    out_obs = (
        quant_config.output_tensors.observer_cls if isinstance(quant_config.output_tensors, QuantizationSpec) else None
    )
    w_obs = quant_config.weight.observer_cls if isinstance(quant_config.weight, QuantizationSpec) else None
    b_obs = quant_config.bias.observer_cls if isinstance(quant_config.bias, QuantizationSpec) else None

    call_func, print_str = (
        (_apply_post_hw_powof2_constrain_passes, "Pow-of-2")
        if any(v in POW_OF_2_OBSERVER for v in [in_obs, out_obs, w_obs, b_obs])
        else (_apply_post_hw_fs_constrain_passes, "float scale")
    )

    logger.info(f"Detected using {print_str} quant, using {print_str} post quant optimization")
    return call_func

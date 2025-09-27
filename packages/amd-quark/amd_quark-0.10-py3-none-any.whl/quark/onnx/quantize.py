#
# Modifications copyright(c) 2023 Advanced Micro Devices,Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import onnx
import onnxruntime
from onnxruntime.quantization.calibrate import CalibrationDataReader, CalibrationMethod
from onnxruntime.quantization.onnx_model import ONNXModel
from onnxruntime.quantization.quant_utils import (
    QuantFormat,
    QuantizationMode,
    QuantType,
    load_model_with_shape_infer,
    model_has_pre_process_metadata,
    ms_domain,
    save_and_reload_model_with_shape_infer,
)
from onnxsim import simplify

from quark.onnx.calibration import (
    CachedDataReader,
    Int16Method,
    LayerWiseMethod,
    PowerOfTwoMethod,
    create_calibrator_float_scale,
    fake_calibration,
    get_data_reader,
    run_calibration,
)
from quark.shares.utils.import_utils import _is_package_available
from quark.shares.utils.log import ScreenLogger, log_errors

from .bias_correction import bias_correction
from .equalization import cle_transforms, replace_all_clip6_to_relu
from .finetuning.fast_finetune import fast_finetune
from .mprecision.auto_mixprecision import auto_mixprecision
from .optimize import optimize
from .quant_utils import (
    COP_DOMAIN,
    ExtendedQuantFormat,
    ExtendedQuantType,
    VitisQuantFormat,
    VitisQuantType,
    add_or_update_opset_import,
    annotate_op_type,
    cache_onnx_model_and_infer_shapes,
    check_extra_quant_op_types,
    check_ir_version,
    check_model_is_fp16,
    check_model_quantizable,
    check_onnx_model,
    check_opset_version,
    check_qdq_model,
    convert_fp16_scale_to_fp32,
    create_tmp_dir,
    customqdq_to_contribqdq,
    eval_metrics,
    fp32_nodes,
    get_all_nodes_to_exclude,
    get_eltwise_op,
    get_exclude_nodes,
    get_matmul_nodes_without_weights,
    is_version_below,
    load_tensors_range,
    match_exclude_subgraphs,
    print_fp32_nodes,
    print_quantize_dynamic_info,
    print_quantize_info,
    print_quantized_info,
    remove_initializer_from_input,
    remove_qdq_op_type,
    run_onnx_model,
    save_onnx_model_with_external_data,
    save_tensor_hist_fig,
    save_tensors_range,
    skip_node_with_inf_tensor,
    update_tmp_dir,
)
from .quarot import rotation_transforms
from .registry import NPUCnnRegistry, NPUTransformerRegistry, QDQRegistry, QLinearOpsRegistry
from .smooth_quant import smooth_transforms

if is_version_below(onnxruntime, "1.18.0"):
    from .cpu_quantizer import VitisQDQCPUQuantizer
    from .onnx_quantizer import ONNXQuantizer, VitisONNXQuantizer
    from .qdq_quantizer import (
        QDQNPUTransformerQuantizer,
        VitisBFPQuantizer,
        VitisExtendedQuantizer,
        VitisQDQNPUCNNQuantizer,
        VitisQDQQuantizer,
    )
else:
    from .quantizers.bfp_quantizer import VitisBFPQuantizer
    from .quantizers.cpu_quantizer import VitisQDQCPUQuantizer  # type: ignore
    from .quantizers.extended_quantizer import VitisExtendedQuantizer
    from .quantizers.npu_cnn_quantizer import VitisQDQNPUCNNQuantizer
    from .quantizers.npu_transformer_quantizer import QDQNPUTransformerQuantizer
    from .quantizers.onnx_quantizer import ONNXQuantizer, VitisONNXQuantizer
    from .quantizers.qdq_quantizer import VitisQDQQuantizer
from .quantizers.matmul_nbits_quantizer import (
    DefaultWeightOnlyQuantConfig,
    GPTQWeightOnlyQuantConfig,
    HQQWeightOnlyQuantConfig,
    MatMulNBitsQuantizer,
)

logger = ScreenLogger(__name__)


@log_errors
def check_static_quant_arguments(
    quant_format: ExtendedQuantFormat,
    activation_type: Union[QuantType, ExtendedQuantType],
    weight_type: Union[QuantType, ExtendedQuantType],
    calibrate_method: Union[CalibrationMethod, PowerOfTwoMethod, Int16Method],
) -> None:
    vitis_qwb_types = [
        ExtendedQuantType.QInt32,
        ExtendedQuantType.QUInt32,
        ExtendedQuantType.QFloat16,
        ExtendedQuantType.QBFloat16,
    ]
    ort_int4_types = []
    if not is_version_below(onnxruntime, "1.19.0"):
        ort_int4_types = [QuantType.QInt4, QuantType.QUInt4]
    if (
        activation_type in vitis_qwb_types or weight_type in vitis_qwb_types
    ) and quant_format != ExtendedQuantFormat.QDQ:
        raise ValueError("Only ExtendedQuantFormat.QDQ supports wide bits quantization types.")

    elif (activation_type in ort_int4_types or weight_type in ort_int4_types) and (
        not isinstance(calibrate_method, CalibrationMethod) or not isinstance(quant_format, QuantFormat)
    ):
        raise ValueError(
            "Only MinMax, Percentile Method and QuantFormat supports int4/uint4 quantization types or onnxruntime version below 1.19.0"
        )


@log_errors
def check_fast_fintune_arguments(
    extra_options: dict[str, Any],
    activation_type: Union[QuantType, ExtendedQuantType],
    weight_type: Union[QuantType, ExtendedQuantType],
) -> None:
    if not is_version_below(onnxruntime, "1.19.0"):
        int_types = [QuantType.QInt4, QuantType.QUInt4]
        if activation_type in int_types or weight_type in int_types:
            raise ValueError("Fast finetune does not support int4 or uint4.")

    if weight_type in [ExtendedQuantType.QFloat16, ExtendedQuantType.QBFloat16]:
        if "AddQDQPairToWeight" in extra_options and not extra_options["AddQDQPairToWeight"]:
            logger.warning("Fast finetune requires not to fold QuantizeLinear for weights.")
        extra_options["AddQDQPairToWeight"] = True
    else:
        if "AddQDQPairToWeight" in extra_options and extra_options["AddQDQPairToWeight"]:
            logger.warning("Fast finetune requires folding QuantizeLinear for weights.")
        extra_options["AddQDQPairToWeight"] = False


@log_errors
def check_crypto_mode_arguments(
    extra_options: dict[str, Any], model_input: Union[str, Path, onnx.ModelProto], use_external_data_format: bool
) -> None:
    if not isinstance(model_input, onnx.ModelProto):
        raise ValueError("For the crypto mode, the input model should be in onnx.ModelProto format.")

    if use_external_data_format:
        raise ValueError(
            "Can not use external data for onnx model since we can't save exposed data to disk in crypto mode."
        )

    if extra_options.get("EncryptionAlgorithm", "") == "AES-256":
        if not _is_package_available("cryptography")[0]:
            raise ImportError(
                "The 'cryptography' is required but not installed. Please install it via 'pip install cryptography'."
            )

    if extra_options.get("FastFinetune", {}).get("MemOptLevel", 1) == 2:
        logger.warning("The 'MemOptLevel' cannot be set to 2 in crypto mode, change it back to the default value of 1.")
        extra_options["FastFinetune"]["MemOptLevel"] = 1

    if extra_options.get("CalibOptimizeMem", True):
        logger.warning("The optimization of memory consumption for calibration will be disabled in crypto mode.")
        extra_options["CalibOptimizeMem"] = False


@log_errors
def quantize_static(
    model_input: Union[str, Path, onnx.ModelProto],
    model_output: Union[str, Path] | None = None,
    calibration_data_reader: CalibrationDataReader | None = None,
    calibration_data_path: str | None = None,
    quant_format: Union[QuantFormat, ExtendedQuantFormat] = QuantFormat.QDQ,
    calibrate_method: Union[CalibrationMethod, PowerOfTwoMethod, Int16Method] = CalibrationMethod.MinMax,
    input_nodes: list[str] | None = [],
    output_nodes: list[str] | None = [],
    op_types_to_quantize: list[str] | None = [],
    extra_op_types_to_quantize: list[str] = [],
    per_channel: bool = False,
    reduce_range: bool = False,
    activation_type: QuantType = QuantType.QInt8,
    weight_type: QuantType = QuantType.QInt8,
    nodes_to_quantize: list[str] = [],
    nodes_to_exclude: list[str] = [],
    subgraphs_to_exclude: list[tuple[list[str]]] = [],
    optimize_model: bool = True,
    use_external_data_format: bool = False,
    execution_providers: list[str] | None = ["CPUExecutionProvider"],
    enable_dpu: bool = False,
    enable_npu_cnn: bool = False,
    enable_npu_transformer: bool = False,
    specific_tensor_precision: bool = False,
    convert_fp16_to_fp32: bool = False,
    convert_nchw_to_nhwc: bool = False,
    debug_mode: bool = False,
    crypto_mode: bool = False,
    include_cle: bool = True,
    include_sq: bool = False,
    include_rotation: bool = False,
    include_fast_ft: bool = False,
    include_auto_mp: bool = False,
    print_summary: bool = True,
    extra_options: dict[str, Any] | None = {},
) -> onnx.ModelProto | None:
    """Qantize a given onnx model using static quantization. This api will return an onnx.ModelProto format quantized model
    if the argument 'model_output' is None or 'crypto_mode' is True.
    """

    float_model: onnx.ModelProto = model_input if isinstance(model_input, onnx.ModelProto) else onnx.load(model_input)
    quant_model: onnx.ModelProto = onnx.ModelProto()  # the quantized model

    if nodes_to_quantize is None:
        nodes_to_quantize = []
    if nodes_to_exclude is None:
        nodes_to_exclude = []
    if subgraphs_to_exclude is None:
        subgraphs_to_exclude = []
    if extra_options is None:
        extra_options = {}

    tensors_range_file = extra_options.get("TensorsRangeFile")
    update_tmp_dir(extra_options.get("TmpDir"))

    if not use_external_data_format:
        if float_model.ByteSize() > onnx.checker.MAXIMUM_PROTOBUF:
            use_external_data_format = True
            logger.warning("The model size is bigger than 2GB, have set use_external_data_format to True.")

    if crypto_mode:
        check_crypto_mode_arguments(extra_options, model_input, use_external_data_format)

    encrypt_algo = extra_options.get("EncryptionAlgorithm") if crypto_mode else None
    secret_key = os.urandom(48) if crypto_mode else None  # It's used to encrypt and decrypt data

    cache_dir = create_tmp_dir(prefix="quark_onnx.quant.")
    cache_path = Path(cache_dir.name).joinpath("cache_model.onnx").as_posix()
    float_model = cache_onnx_model_and_infer_shapes(
        float_model, cache_path, use_external_data_format, encrypt_algo, secret_key
    )

    if not convert_fp16_to_fp32 and not extra_options.get("QuantizeFP16", False):
        model_is_fp16 = check_model_is_fp16(float_model)
        if model_is_fp16:
            logger.warning(
                "Detected that the input model is an FP16 model. It will proceed with quantization based on the FP16 model. "
            )
            extra_options["QuantizeFP16"] = True

    if enable_dpu:
        logger.warning(
            "The 'enable_dpu' parameter will be deprecated in future versions. Please use 'enable_npu_cnn' instead."
        )
        enable_npu_cnn = enable_dpu

    if not crypto_mode:
        print_quantize_info(
            model_input,
            model_output,
            calibration_data_reader,
            calibration_data_path,
            quant_format,
            input_nodes,
            output_nodes,
            op_types_to_quantize,
            extra_op_types_to_quantize,
            per_channel,
            reduce_range,
            activation_type,
            weight_type,
            nodes_to_quantize,
            nodes_to_exclude,
            subgraphs_to_exclude,
            optimize_model,
            use_external_data_format,
            calibrate_method,
            execution_providers,
            enable_npu_cnn,
            enable_npu_transformer,
            specific_tensor_precision,
            debug_mode,
            convert_fp16_to_fp32,
            convert_nchw_to_nhwc,
            include_cle,
            include_sq,
            include_rotation,
            include_fast_ft,
            extra_options,
        )

    nodes_to_exclude = get_all_nodes_to_exclude(float_model, nodes_to_exclude)

    if not extra_options.get("UseMatMulNBits", False):
        if not check_ir_version(float_model):
            logger.warning(
                "The ir version of input model is below 4. It is recommended to upgrade ir version to 7 or higher."
            )
        if not check_opset_version(float_model):
            logger.warning(
                "The opset version of input model is below 10. It is recommended to upgrade opset version to 17 or higher."
            )
        if check_qdq_model(float_model):
            logger.error(
                "The input model is already a quantized model. Please make sure that input model is a float model."
            )

    if isinstance(quant_format, VitisQuantFormat):
        if quant_format == VitisQuantFormat.BFPFixNeuron:
            weight_type = ExtendedQuantType.QBFP
            activation_type = ExtendedQuantType.QBFP
        elif quant_format == VitisQuantFormat.MXFixNeuron:
            weight_type = ExtendedQuantType.QMX
            activation_type = ExtendedQuantType.QMX
        quant_format = ExtendedQuantFormat.QDQ
        logger.warning("VitisQuantFormat will be deprecated in future versions, use ExtendedQuantFormat instead.")

    if isinstance(weight_type, VitisQuantType):
        weight_type = ExtendedQuantType(weight_type.value)
        logger.warning("VitisQuantType will be deprecated in future versions, use ExtendedQuantType instead.")
    if isinstance(activation_type, VitisQuantType):
        activation_type = ExtendedQuantType(activation_type.value)
        logger.warning("VitisQuantType will be deprecated in future versions, use ExtendedQuantType instead.")

    fp32_nodes_dict = fp32_nodes(float_model)

    if extra_options.get("QuantizeAllOpTypes", False):
        all_op_types = list(fp32_nodes_dict.keys())
        extra_op_types_to_quantize.extend(all_op_types)

    if subgraphs_to_exclude:
        nodes_to_exclude += match_exclude_subgraphs(float_model, subgraphs_to_exclude)
        nodes_to_exclude = list(set(nodes_to_exclude))

    if "ConvertOpsetVersion" in extra_options:
        opset_version = extra_options["ConvertOpsetVersion"]
        from .tools.convert_opset_version import convert_opset_version

        float_model = convert_opset_version(float_model, opset_version)

    skip_calibration = False
    if (
        extra_options.get("UseMatMulNBits", False)
        or (
            activation_type
            in [ExtendedQuantType.QBFloat16, ExtendedQuantType.QFloat16, ExtendedQuantType.QBFP, ExtendedQuantType.QMX]
            and not extra_options.get("ActivationScaled", False)
        )
        or (tensors_range_file is not None and os.path.exists(tensors_range_file) and (not crypto_mode))
    ):
        skip_calibration = True

    if convert_fp16_to_fp32:
        logger.info("Start converting the input model to float32.")
        from .tools import float16

        fp16_model = float_model
        try:
            fp32_model = float16.convert_float16_to_float(fp16_model)
            try:
                model_simp, check = simplify(fp32_model)
                assert check, "Simplified ONNX model could not be validated"
                logger.info("Convert the input model to float32 sucessfully.")
            except Exception as e2:
                logger.warning(f"Fail to simplify the ONNX model because {e2}.")
                model_simp = fp32_model
        except Exception as e:
            logger.warning(f"Fail to convert fp16 to fp32 beacuse {e}, skip fp16 to fp32 conversion.")
            model_simp = fp16_model
        float_model = cache_onnx_model_and_infer_shapes(
            model_simp, cache_path, use_external_data_format, encrypt_algo, secret_key
        )

    mode = QuantizationMode.QLinearOps

    quantize_fp16 = extra_options.get("QuantizeFP16", False)
    use_fp32_scale = extra_options.get("UseFP32Scale", quantize_fp16)
    if quantize_fp16:
        optimize_model = False
        if is_version_below(onnxruntime, "1.18.0"):
            logger.warning(
                "The parameter QuantizeFP16 only takes effect in onnxruntime 1.18 and above. It will output a model same as the input model if onnxruntime version is 1.17 or lower."
            )
        logger.info(
            "The parameter optimize_model is set to False automatically when the parameter QuantizeFP16 is set to True."
        )
    if not quantize_fp16 and use_fp32_scale:
        logger.warning("The parameter UseFP32Scale could be True only if the parameter QuantizeFP16 is True.")

    check_onnx_model(float_model)

    data_reader = get_data_reader(float_model, calibration_data_reader, calibration_data_path, extra_options)
    cached_data_reader = CachedDataReader(data_reader, None, convert_nchw_to_nhwc, quantize_fp16)

    if extra_options.get("SaveTensorHistFig", False):
        with create_tmp_dir(prefix="quark_onnx.quant.") as quant_tmp_dir:
            hist_calibrator = create_calibrator_float_scale(
                float_model,
                op_types_to_quantize,
                augmented_model_path=Path(quant_tmp_dir).joinpath("augmented_model.onnx").as_posix(),
                calibrate_method=CalibrationMethod.Percentile,
                use_external_data_format=use_external_data_format,
                execution_providers=execution_providers,
                extra_options={"symmetric": False},
            )
            save_tensor_hist_fig(hist_calibrator, cached_data_reader, extra_options)
            cached_data_reader.reset_iter()

    if input_nodes or output_nodes:
        if nodes_to_exclude:
            nodes_to_exclude += get_exclude_nodes(float_model, input_nodes, output_nodes)
        else:
            nodes_to_exclude = get_exclude_nodes(float_model, input_nodes, output_nodes)

    if extra_options.get("MatMulConstBOnly", enable_npu_transformer):
        nodes_to_exclude += get_matmul_nodes_without_weights(float_model)

    if not op_types_to_quantize or len(op_types_to_quantize) == 0:
        if enable_npu_transformer:
            op_types_to_quantize = list(NPUTransformerRegistry.keys())
        else:
            q_linear_ops = list(QLinearOpsRegistry.keys())
            qdq_ops = list(QDQRegistry.keys())
            if enable_npu_cnn or quant_format is ExtendedQuantFormat.QDQ:
                dpu_ops = list(NPUCnnRegistry.keys())
                qdq_ops = list(set(dpu_ops + qdq_ops))
            op_types_to_quantize = list(set(q_linear_ops + qdq_ops))

    check_extra_quant_op_types(float_model, extra_op_types_to_quantize)

    op_types_to_quantize += extra_op_types_to_quantize
    op_types_to_quantize = list(set(op_types_to_quantize))

    if extra_options.get("RemoveInputInit", True):
        try:
            model_opt = remove_initializer_from_input(float_model)
            float_model = cache_onnx_model_and_infer_shapes(
                model_opt, cache_path, use_external_data_format, encrypt_algo, secret_key
            )
            logger.info("Removed initializers from input")
        except Exception as e:
            logger.debug(f"Fail to remove init from input because {e}")

    if extra_options.get("SimplifyModel", True) and not extra_options.get("UseMatMulNBits", False):
        try:
            model_simp, check = simplify(float_model)
            float_model = cache_onnx_model_and_infer_shapes(
                model_simp, cache_path, use_external_data_format, encrypt_algo, secret_key
            )
            logger.info("Simplified model sucessfully")
        except Exception as e:
            logger.warning(f"Fail to Simplify ONNX model because {e}")

    shared_init_optypes = extra_options.get("CopySharedInit")
    if shared_init_optypes is not None:
        from quark.onnx.tools import convert_shared_initializer_to_unique

        try:
            model_copied = convert_shared_initializer_to_unique.convert(float_model, shared_init_optypes)
            float_model = cache_onnx_model_and_infer_shapes(
                model_copied, cache_path, use_external_data_format, encrypt_algo, secret_key
            )
            logger.info(
                "Duplicate the shared initializers in the model for separate quantization use across different nodes!"
            )
        except Exception as e:
            logger.warning(f"Fail to duplicate the shared initializers in the ONNX model because of {e}.")

    shared_bias_init_optypes = extra_options.get("CopyBiasInit", ["Conv", "ConvTranspose", "Gemm"])
    if shared_bias_init_optypes is not None:
        supported_quant_types = [
            QuantType.QUInt8,
            QuantType.QInt8,
            QuantType.QUInt16,
            QuantType.QInt16,
            ExtendedQuantType.QInt8,
            ExtendedQuantType.QUInt8,
            ExtendedQuantType.QInt16,
            ExtendedQuantType.QUInt16,
        ]
        if (
            (weight_type in supported_quant_types)
            and (activation_type in supported_quant_types)
            and (calibrate_method in CalibrationMethod)
        ):
            from quark.onnx.tools import convert_shared_initializer_to_unique

            try:
                model_copied = convert_shared_initializer_to_unique.convert(
                    float_model, shared_bias_init_optypes, prefix="duplicated", only_bias=True
                )
                float_model = cache_onnx_model_and_infer_shapes(
                    model_copied, cache_path, use_external_data_format, encrypt_algo, secret_key
                )
                logger.info(
                    "Duplicate the shared bias initializers in the model for separate quantization use across different nodes!"
                )
            except Exception as e:
                logger.warning(f"Fail to duplicate the shared bias initializers in the ONNX model because of {e}.")

    logger.info("Loading model...")
    fold_batch_norm = optimize_model
    if optimize_model and not use_external_data_format and not crypto_mode:
        from onnxruntime.quantization.quant_utils import optimize_model as om

        try:
            optimized_path = Path(cache_dir.name).joinpath("optimized_model.onnx")
            om(Path(cache_path), optimized_path)
            float_model = load_model_with_shape_infer(optimized_path)
            optimized_path.unlink()
        except Exception as e:
            logger.warning(
                f"Failed to run quantization preprocessing with error of {e}. Using original model. Please check."
            )
            try:
                float_model = load_model_with_shape_infer(Path(cache_path))
            except Exception as e:
                raise RuntimeError(
                    f"Model loading failed as {e}"
                    "Shape inference needs write access to the model input directory."
                    "Please verify permissions of the model input directory."
                )
                return None
    else:
        try:
            float_model = cache_onnx_model_and_infer_shapes(
                float_model, cache_path, use_external_data_format, encrypt_algo, secret_key
            )
        except Exception as e:
            raise RuntimeError(
                f"Model loading failed as {e}"
                "Shape inference needs write access to the model input directory."
                "Please verify permissions of the model input directory."
            )
            return None

    if convert_nchw_to_nhwc:
        from .utils.model_utils import convert_nchw_to_nhwc as convert_func

        logger.info("Start converting the input model from ncwh to nhwc model.")
        try:
            model_converted = convert_func(float_model)
            float_model = cache_onnx_model_and_infer_shapes(
                model_converted, cache_path, use_external_data_format, encrypt_algo, secret_key
            )
        except Exception as e:
            logger.warning(f"Failed to convert nchw to nhwc beacuse {e}, ")

    if not skip_calibration:
        run_onnx_model(float_model, cached_data_reader)
        cached_data_reader.reset_iter()

    if not check_model_quantizable(float_model, op_types_to_quantize, nodes_to_exclude):
        logger.warning("No quantizable ops in this model, quantization is skipped.")
        if model_output is None or crypto_mode:
            return float_model
        else:
            save_onnx_model_with_external_data(
                float_model, model_output, save_as_external_data=use_external_data_format
            )
            return None

    clip6_to_relu6 = False
    if "ReplaceClip6Relu" in extra_options:
        clip6_to_relu6 = extra_options["ReplaceClip6Relu"]

    if clip6_to_relu6:
        model_replaced = replace_all_clip6_to_relu(
            float_model, op_types_to_quantize, nodes_to_quantize, nodes_to_exclude
        )
        topo_model = ONNXModel(model_replaced)
        topo_model.topological_sort()
        float_model = cache_onnx_model_and_infer_shapes(
            topo_model.model, cache_path, use_external_data_format, encrypt_algo, secret_key
        )

    if "FixShapes" in extra_options:
        from .tools.fix_shapes import fix_input_and_output_shapes, infer_all_tensors_shape, save_all_tensors_shape

        fix_name_shape = extra_options["FixShapes"]
        try:
            model_temp = fix_input_and_output_shapes(float_model, fix_name_shape)
            tensor_name_shape_dict = infer_all_tensors_shape(model_temp, use_external_data_format)
            model_temp = save_all_tensors_shape(model_temp, tensor_name_shape_dict)
            float_model = cache_onnx_model_and_infer_shapes(
                model_temp, cache_path, use_external_data_format, encrypt_algo, secret_key
            )
        except Exception as e:
            logger.warning(
                f"Fail to fix shapes of the quantized model beacuse {e}skip fixing shapes for the quantized model."
            )

    if include_cle:
        cle_balance_method = "max"
        cle_steps = 1
        cle_weight_threshold = 0.5
        cle_scale_append_bias = True
        cle_scale_use_threshold = True
        cle_total_layer_diff_threshold = 2e-7

        if "CLEBalanceMethod" in extra_options:
            cle_balance_method = extra_options["CLEBalanceMethod"]
        if "CLEWeightThreshold" in extra_options:
            cle_weight_threshold = extra_options["CLEWeightThreshold"]
        if "CLEScaleUseThreshold" in extra_options:
            cle_scale_use_threshold = extra_options["CLEScaleUseThreshold"]
        if "CLEScaleAppendBias" in extra_options:
            cle_scale_append_bias = extra_options["CLEScaleAppendBias"]
        if "CLESteps" in extra_options:
            cle_steps = extra_options["CLESteps"]
        if "CLETotalLayerDiffThreshold" in extra_options:
            cle_total_layer_diff_threshold = extra_options["CLETotalLayerDiffThreshold"]
        if nodes_to_exclude is None:
            nodes_to_exclude = []
        model_transformed = cle_transforms(
            float_model,
            op_types_to_quantize,
            nodes_to_quantize,
            nodes_to_exclude,
            cle_steps,
            cle_balance_method,
            cle_weight_threshold,
            cle_scale_append_bias,
            cle_scale_use_threshold,
            cle_total_layer_diff_threshold,
        )
        float_model = cache_onnx_model_and_infer_shapes(
            model_transformed, cache_path, use_external_data_format, encrypt_algo, secret_key
        )

    if include_rotation:
        from quark.torch.algorithm.rotation.rotation_utils import get_rotation_matrix

        logger.info("Start rotation ....")
        hidden_size = extra_options.get("RMatrixDim", 4096)
        random_had = extra_options.get("UseRandomHad", False)
        rotation_config_file = extra_options.get("RConfigPath")
        assert rotation_config_file is not None, (
            'Error! Please specify the rotation config file via extra_options["RConfigPath"]'
        )

        try:
            r1_matrix = get_rotation_matrix(num_channels=hidden_size, random=random_had)
        except AssertionError as e:
            raise AssertionError(
                "Error! The dim of the target R1 matrix is not support while requiring random_had as true."
            )
        r1_matrix_np = r1_matrix.numpy()

        r_matrixs = {"R1": r1_matrix_np}

        model_rotated = rotation_transforms(float_model, r_matrixs, rotation_config_file, use_external_data_format)
        float_model = cache_onnx_model_and_infer_shapes(
            model_rotated, cache_path, use_external_data_format, encrypt_algo, secret_key
        )
        logger.info("Rotation complete!")

    if include_sq:
        smooth_alpha = 0.5
        if "SmoothAlpha" in extra_options:
            smooth_alpha = extra_options["SmoothAlpha"]
        logger.info(f"Start smoothing model, the smooth alpha was set as {smooth_alpha}")
        if use_external_data_format:
            new_prop = float_model.metadata_props.add()
            new_prop.key = "cache_path"
            new_prop.value = os.path.dirname(cache_path)
        model_smoothed = smooth_transforms(
            float_model, cached_data_reader, alpha=smooth_alpha, use_external_data_format=use_external_data_format
        )
        float_model = cache_onnx_model_and_infer_shapes(
            model_smoothed, cache_path, use_external_data_format, encrypt_algo, secret_key
        )
        cached_data_reader.reset_iter()

    skip_node_with_inf_tensor_list = skip_node_with_inf_tensor(float_model)
    nodes_to_exclude.extend(skip_node_with_inf_tensor_list)

    int16_scale = False
    if "Int16Scale" in extra_options:
        int16_scale = extra_options["Int16Scale"]
    if int16_scale:
        if enable_npu_cnn:
            raise ValueError(
                "Int16Scale is an experimental featureand cannot be used simultaneously with enable_npu_cnn"
            )

    add_or_update_opset_import(float_model, ms_domain, 1)
    # add_or_update_opset_import(float_model, VAI_DOMAIN, 1)
    add_or_update_opset_import(float_model, COP_DOMAIN, 1)

    fuse_instance_norm = True
    fuse_l2_norm = True
    fuse_gelu = True
    fuse_layer_norm = True
    convert_split_to_slice = False
    convert_bn_to_conv = False
    convert_reduce_mean_to_global_avg_pool = False
    split_large_kernel_pool = False

    # TODO: Refactor logics of optimization for xcompiler and vaiml in the future.
    if (
        enable_npu_cnn
        or enable_npu_transformer
        or (
            quant_format is ExtendedQuantFormat.QDQ
            and not extra_options.get("BF16QDQToCast", False)
            and not extra_options.get("EnableVaimlBF16", False)
        )
    ):
        logger.info("optimize the model for better hardware compatibility.")
        convert_split_to_slice = True
        convert_bn_to_conv = True
        convert_reduce_mean_to_global_avg_pool = True
        split_large_kernel_pool = True

    if "FoldBatchNorm" in extra_options:
        fold_batch_norm = extra_options["FoldBatchNorm"]
    if "FuseInstanceNorm" in extra_options:
        fuse_instance_norm = extra_options["FuseInstanceNorm"]
    if "FuseL2Norm" in extra_options:
        fuse_l2_norm = extra_options["FuseL2Norm"]
    if "FuseGelu" in extra_options:
        fuse_gelu = extra_options["FuseGelu"]
    if "FuseLayerNorm" in extra_options:
        fuse_layer_norm = extra_options["FuseLayerNorm"]
    if "ConvertSplitToSlice" in extra_options:
        convert_split_to_slice = extra_options["ConvertSplitToSlice"]
    if "ConvertBNToConv" in extra_options:
        convert_bn_to_conv = extra_options["ConvertBNToConv"]
    if "ConvertReduceMeanToGlobalAvgPool" in extra_options:
        convert_reduce_mean_to_global_avg_pool = extra_options["ConvertReduceMeanToGlobalAvgPool"]
    if "SplitLargeKernelPool" in extra_options:
        split_large_kernel_pool = extra_options["SplitLargeKernelPool"]

    if (
        fuse_instance_norm
        or fuse_l2_norm
        or fuse_gelu
        or fuse_layer_norm
        or convert_bn_to_conv
        or convert_reduce_mean_to_global_avg_pool
        or split_large_kernel_pool
        or convert_split_to_slice
        or fold_batch_norm
    ):
        model_optim = optimize(
            float_model,
            op_types_to_quantize,
            nodes_to_quantize,
            nodes_to_exclude,
            convert_bn_to_conv,
            convert_reduce_mean_to_global_avg_pool,
            split_large_kernel_pool,
            convert_split_to_slice,
            fuse_instance_norm,
            fuse_l2_norm,
            fuse_gelu,
            fuse_layer_norm,
            fold_batch_norm,
            convert_clip_to_relu=False,
            fold_batch_norm_after_concat=fold_batch_norm,
        )
        float_model = cache_onnx_model_and_infer_shapes(
            model_optim, cache_path, use_external_data_format, encrypt_algo, secret_key
        )

    quantized_tensor_type = {}
    if specific_tensor_precision:
        if extra_options.get("MixedPrecisionTensor"):
            for k, v in extra_options["MixedPrecisionTensor"].items():
                for t in v:
                    quantized_tensor_type[t] = k
            if quantized_tensor_type:
                logger.info("In the specific_tensor_precision mode, the quant_format will use ExtendedQuantFormat.QDQ")
                quant_format = ExtendedQuantFormat.QDQ

    if extra_options.get("AlignEltwiseQuantType"):
        if (
            enable_npu_cnn is False
            and enable_npu_transformer is False
            and enable_dpu is False
            and quant_format == ExtendedQuantFormat.QDQ
        ):
            eltwise_tensors = get_eltwise_op(float_model)
            for tensor_name in eltwise_tensors:
                quantized_tensor_type[tensor_name] = activation_type
            logger.info(
                "The parameter AlignEltwiseQuantType takes effect, the weights of nodes will be quantized with the activation quant type if the operation type is in [Mul, Div, Add, Sub, Min, Max]."
            )
        else:
            logger.warning(
                "The parameter AlignEltwiseQuantType only takes effect when quant_format is ExtendedQuantFormat.QDQ and enable_npu_cnn is False and enable_npu_transformer is False and enable_dpu is False"
            )

    # TODO: Refactor logics for quantize.py in the future.
    topo_model = ONNXModel(float_model)
    topo_model.topological_sort()
    float_model = cache_onnx_model_and_infer_shapes(
        topo_model.model, cache_path, use_external_data_format, encrypt_algo, secret_key
    )

    if extra_options.get("UseMatMulNBits", False):
        matmul_nbits_quantize_dict = extra_options.get("MatMulNBitsParams", {})
        assert isinstance(matmul_nbits_quantize_dict, dict), (
            "The parameter 'MatMulNBitsParams' in extra_options must be a dict."
        )
        if "GroupSize" in matmul_nbits_quantize_dict:
            matmul_nbits_group_size = matmul_nbits_quantize_dict["GroupSize"]
        else:
            matmul_nbits_group_size = 128
        if "Symmetric" in matmul_nbits_quantize_dict:
            matmul_nbits_symmetric = matmul_nbits_quantize_dict["Symmetric"]
        else:
            matmul_nbits_symmetric = True
        if "Bits" in matmul_nbits_quantize_dict:
            matmul_nbits_bits = matmul_nbits_quantize_dict["Bits"]
        else:
            matmul_nbits_bits = 4
        if "AccuracyLevel" in matmul_nbits_quantize_dict:
            matmul_nbits_accuracy_level = matmul_nbits_quantize_dict["AccuracyLevel"]
        else:
            matmul_nbits_accuracy_level = 0

        algo_config: Union[DefaultWeightOnlyQuantConfig, GPTQWeightOnlyQuantConfig, HQQWeightOnlyQuantConfig, None] = (
            None
        )
        if extra_options.get("MatMulNBitsParams", {}).get("Algorithm", "DEFAULT") == "GPTQ":
            algo_config = GPTQWeightOnlyQuantConfig(
                calibration_data_reader=cached_data_reader,
                percdamp=extra_options.get("GPTQParams", {}).get("PercDamp", 0.01),
                block_size=extra_options.get("GPTQParams", {}).get("BlockSize", 128),
                actorder=extra_options.get("GPTQParams", {}).get("ActOrder", False),
                mse=extra_options.get("GPTQParams", {}).get("MSE", False),
                perchannel=extra_options.get("GPTQParams", {}).get("PerChannel", False),
            )
        elif extra_options.get("MatMulNBitsParams", {}).get("Algorithm", "DEFAULT") == "HQQ":
            algo_config = HQQWeightOnlyQuantConfig(block_size=matmul_nbits_group_size, bits=matmul_nbits_bits)
        else:
            algo_config = DefaultWeightOnlyQuantConfig(
                block_size=matmul_nbits_group_size,
                is_symmetric=matmul_nbits_symmetric,
                bits=matmul_nbits_bits,
                accuracy_level=matmul_nbits_accuracy_level,
            )

        quantizer = MatMulNBitsQuantizer(
            float_model,
            matmul_nbits_group_size,
            matmul_nbits_symmetric,
            matmul_nbits_bits,
            accuracy_level=matmul_nbits_accuracy_level,
            algo_config=algo_config,
            extra_options=extra_options,
        )
        quantizer.quantize_model()
        quant_model = quantizer.model.model
        float_model = topo_model.model
        cached_data_reader.reset_iter()

    if not skip_calibration:
        tensors_range = run_calibration(
            float_model,
            cached_data_reader,
            op_types_to_quantize,
            activation_type,
            calibrate_method,
            use_external_data_format,
            execution_providers,
            quantized_tensor_type,
            extra_options,
        )
        cached_data_reader.reset_iter()

        if tensors_range_file is not None and not crypto_mode:
            save_tensors_range(tensors_range, tensors_range_file)
    else:
        if tensors_range_file is not None and not crypto_mode:
            tensors_range = load_tensors_range(tensors_range_file)
        else:
            tensors_range = fake_calibration(float_model)

    if extra_options.get("RemoveQDQConvClip", True):
        remove_qdq_op_type.append("Clip")
    if extra_options.get("RemoveQDQConvRelu", True):
        remove_qdq_op_type.append("Relu")
    if extra_options.get("RemoveQDQConvLeakyRelu", True):
        remove_qdq_op_type.append("LeakyRelu")
    if extra_options.get("RemoveQDQConvPRelu", True):
        remove_qdq_op_type.append("PRelu")
    if extra_options.get("RemoveQDQConvGelu", False):
        remove_qdq_op_type.append("Gelu")
    if extra_options.get("RemoveQDQInstanceNorm", False):
        annotate_op_type.append("InstanceNormalization")

    check_static_quant_arguments(quant_format, activation_type, weight_type, calibrate_method)
    if include_fast_ft and include_auto_mp is False:
        check_fast_fintune_arguments(extra_options, activation_type, weight_type)

    if int16_scale:
        calibrate_method = Int16Method.MinMax

    if not extra_options.get("UseMatMulNBits", False):
        # BFP and MX quantization don't need calibration, so they are not sensitive to calibration method
        if weight_type == activation_type and weight_type in [ExtendedQuantType.QBFP, ExtendedQuantType.QMX]:
            quantizer = VitisBFPQuantizer(
                float_model,
                per_channel,
                reduce_range,
                mode,
                True,
                weight_type,
                activation_type,
                tensors_range,
                nodes_to_quantize,
                nodes_to_exclude,
                op_types_to_quantize,
                calibrate_method,
                quantized_tensor_type,
                extra_options,
            )
        elif (calibrate_method in CalibrationMethod) or (calibrate_method in LayerWiseMethod):
            if quant_format is QuantFormat.QOperator:
                quantizer = ONNXQuantizer(
                    float_model,
                    per_channel,
                    reduce_range,
                    mode,
                    True,  # static
                    weight_type,
                    activation_type,
                    tensors_range,
                    nodes_to_quantize,
                    nodes_to_exclude,
                    op_types_to_quantize,
                    extra_options,
                )
            elif quant_format is QuantFormat.QDQ:
                if not enable_npu_transformer:
                    quantizer = VitisQDQCPUQuantizer(
                        float_model,
                        per_channel,
                        reduce_range,
                        mode,
                        True,  # static
                        weight_type,
                        activation_type,
                        tensors_range,
                        nodes_to_quantize,
                        nodes_to_exclude,
                        op_types_to_quantize,
                        calibrate_method,
                        quantized_tensor_type,
                        extra_options,
                    )
                else:
                    quantizer = QDQNPUTransformerQuantizer(
                        float_model,
                        per_channel,
                        reduce_range,
                        mode,
                        True,  # static
                        weight_type,
                        activation_type,
                        tensors_range,
                        nodes_to_quantize,
                        nodes_to_exclude,
                        op_types_to_quantize,
                        extra_options,
                    )
            elif quant_format is ExtendedQuantFormat.QDQ:
                quantizer = VitisExtendedQuantizer(
                    float_model,
                    per_channel,
                    reduce_range,
                    mode,
                    True,
                    weight_type,
                    activation_type,
                    tensors_range,
                    nodes_to_quantize,
                    nodes_to_exclude,
                    op_types_to_quantize,
                    calibrate_method,
                    quantized_tensor_type,
                    extra_options,
                )
            else:
                raise ValueError("No corresponding quantizer for this set of arguments.")
        elif calibrate_method in PowerOfTwoMethod or calibrate_method in Int16Method:
            if quant_format is QuantFormat.QOperator:
                quantizer = VitisONNXQuantizer(
                    float_model,
                    per_channel,
                    reduce_range,
                    mode,
                    True,
                    weight_type,
                    activation_type,
                    tensors_range,
                    nodes_to_quantize,
                    nodes_to_exclude,
                    op_types_to_quantize,
                    calibrate_method,
                    quantized_tensor_type,
                    extra_options,
                )
            elif quant_format is QuantFormat.QDQ:
                if not enable_npu_cnn:
                    quantizer = VitisQDQQuantizer(
                        float_model,
                        per_channel,
                        reduce_range,
                        mode,
                        True,
                        weight_type,
                        activation_type,
                        tensors_range,
                        nodes_to_quantize,
                        nodes_to_exclude,
                        op_types_to_quantize,
                        calibrate_method,
                        quantized_tensor_type,
                        extra_options,
                    )
                else:
                    quantizer = VitisQDQNPUCNNQuantizer(
                        float_model,
                        per_channel,
                        reduce_range,
                        mode,
                        True,
                        weight_type,
                        activation_type,
                        tensors_range,
                        nodes_to_quantize,
                        nodes_to_exclude,
                        op_types_to_quantize,
                        calibrate_method,
                        quantized_tensor_type,
                        extra_options,
                    )
            elif quant_format is ExtendedQuantFormat.QDQ:
                quantizer = VitisExtendedQuantizer(
                    float_model,
                    per_channel,
                    reduce_range,
                    mode,
                    True,
                    weight_type,
                    activation_type,
                    tensors_range,
                    nodes_to_quantize,
                    nodes_to_exclude,
                    op_types_to_quantize,
                    calibrate_method,
                    quantized_tensor_type,
                    extra_options,
                )
            else:
                raise ValueError("No corresponding quantizer for this set of arguments.")
        quantizer.quantize_model()

        if extra_options.get("RemoveQDQMulAdd", False):
            from .tools.remove_qdq_mul_add import remove_qdq_mul_add

            remove_qdq_mul_add(quantizer.model.model)

        if "RemoveQDQBetweenOps" in extra_options:
            from .tools.remove_qdq_between_ops import remove_qdq_between_ops

            between_ops = extra_options.get("RemoveQDQBetweenOps")
            if not (
                isinstance(between_ops, list)
                and all(
                    isinstance(item, tuple) and len(item) == 2 and all(isinstance(elem, str) for elem in item)
                    for item in between_ops
                )
            ):
                logger.warning(f"'RemoveQDQBetweenOps' should be a list of (str, str) tuples. Actual: {between_ops}")
            remove_qdq_between_ops(quantizer.model.model, between_ops)

        if extra_options.get("BF16QDQToCast", extra_options.get("EnableVaimlBF16", False)):
            from .tools.replace_bfloat16_qdq_cast import replace_bfloat16_qdq_cast

            quantizer.model.model = replace_bfloat16_qdq_cast(quantizer.model.model)

        if extra_options.get("EnableVaimlBF16", False):
            from .tools.remove_bf16_cast import remove_bf16_cast

            quantizer.model.model = remove_bf16_cast(quantizer.model.model)

        if quant_format is ExtendedQuantFormat.QDQ:
            customqdq_to_contribqdq(quantizer.model.model, use_external_data_format)

        quant_model = quantizer.model.model
        float_model = topo_model.model

    if quantize_fp16 and use_fp32_scale:
        quant_model = convert_fp16_scale_to_fp32(quant_model)

    if extra_options.get("BiasCorrection", False):
        quant_model = bias_correction(
            float_model,
            quant_model,
            use_external_data_format,
            cached_data_reader,
            activation_type,
            calibrate_method,
            extra_options,
        )
        cached_data_reader.reset_iter()

    if include_auto_mp:
        quant_model = auto_mixprecision(
            float_model,
            quant_model,
            use_external_data_format,
            cached_data_reader,
            activation_type,
            weight_type,
            extra_options,
        )
        cached_data_reader.reset_iter()

    if extra_options.get("Int16Bias", False):
        from .tools.convert_bias_int32_to_int16 import convert_bias_int32_to_int16

        try:
            quant_model, _ = convert_bias_int32_to_int16(quant_model)
        except Exception as e:
            logger.warning(
                f"Failed to convert bias from int32 to int16 beacuse {e}skip converting bias from int32 to int16."
            )

    if include_fast_ft:
        quant_model = fast_finetune(
            float_model, quant_model, use_external_data_format, cached_data_reader, extra_options
        )
        cached_data_reader.reset_iter()

    if extra_options.get("UseGPTQ", False):
        from .gptq.gptq import GptqProcessor

        gptq_processor = GptqProcessor(
            float_model,
            quant_model,
            cached_data_reader,
            extra_options,
            use_external_data_format=use_external_data_format,
        )
        quant_model = gptq_processor.apply()
        cached_data_reader.reset_iter()

    if extra_options.get("BF16WithClip", False):
        from .tools.insert_clip_bfloat16_qdq import insert_clip_bfloat16_qdq

        quant_model = insert_clip_bfloat16_qdq(quant_model)

    # This optimization should after calibration
    convert_clip_to_relu = False
    if "ConvertClipToRelu" in extra_options:
        convert_clip_to_relu = extra_options["ConvertClipToRelu"]
    # This is a post processing of quantization
    dedicate_dq_node = False
    if "DedicateDQNode" in extra_options:
        dedicate_dq_node = extra_options["DedicateDQNode"]
    if convert_clip_to_relu or dedicate_dq_node:
        quant_model = optimize(
            quant_model,
            op_types_to_quantize,
            nodes_to_quantize,
            nodes_to_exclude,
            convert_bn_to_conv=False,
            convert_reduce_mean_to_global_avg_pool=False,
            split_large_kernel_pool=False,
            convert_split_to_slice=False,
            fuse_instance_norm=False,
            fuse_l2_norm=False,
            fuse_gelu=False,
            convert_clip_to_relu=convert_clip_to_relu,
            dedicate_dq_node=dedicate_dq_node,
        )

    if print_summary and fp32_nodes_dict and not crypto_mode:
        print_fp32_nodes(fp32_nodes_dict, model_output)
        print_quantized_info(quant_model, debug_mode, shared_init_optypes)

    if model_output is None or crypto_mode:
        quant_model = onnx.shape_inference.infer_shapes(quant_model)
        return quant_model

    quant_model = save_and_reload_model_with_shape_infer(quant_model)
    save_onnx_model_with_external_data(quant_model, model_output, save_as_external_data=use_external_data_format)

    if "EvalMetrics" in extra_options:
        if "EvalDataReader" in extra_options:
            eval_data_reader = extra_options["EvalDataReader"]
        else:
            eval_data_reader = cached_data_reader

        eval_metrics(model_input, model_output, eval_data_reader)

    return None


def quantize_dynamic(
    model_input: Union[str, Path, onnx.ModelProto],
    model_output: Union[str, Path] | None = None,
    op_types_to_quantize: Union[list[str], None] = [],
    per_channel: bool = False,
    reduce_range: bool = False,
    weight_type: QuantType = QuantType.QInt8,
    nodes_to_quantize: list[str] = [],
    nodes_to_exclude: list[str] = [],
    subgraphs_to_exclude: list[tuple[list[str]]] = [],
    use_external_data_format: bool = False,
    debug_mode: bool = False,
    crypto_mode: bool = False,
    extra_options: dict[str, Any] | None = {},
) -> onnx.ModelProto | None:
    """Qantize a given onnx model using dynamic quantization. This api will return an onnx.ModelProto format quantized model
       if the argument 'model_output' is None or 'crypto_mode' is True.

    Args:
        model_input: file path of model or ModelProto to quantize
        model_output: file path of quantized model
        op_types_to_quantize:
            specify the types of operators to quantize, like ['Conv'] to quantize Conv only.
            It quantizes all supported operators by default.
        per_channel: quantize weights per channel
        reduce_range:
            quantize weights with 7-bits. It may improve the accuracy for some models running on non-VNNI machine,
            especially for per-channel mode
        weight_type:
            quantization data type of weight. Please refer to
            https://onnxruntime.ai/docs/performance/quantization.html for more details on data type selection
        nodes_to_quantize:
            List of nodes names to quantize. When this list is not None only the nodes in this list
            are quantized.
            example:
            [
                'Conv__224',
                'Conv__252'
            ]
        nodes_to_exclude:
            List of nodes names to exclude. The nodes in this list will be excluded from quantization
            when it is not None.
        subgraphs_to_exclude:
            List of start and end nodes names of subgraphs to exclude. The nodes matched by the subgraphs will be excluded from quantization
            when it is not None.
        use_external_data_format: option used for large size (>2GB) model. Set to False by default.
        extra_options:
            key value pair dictionary for various options in different case. Current used:
                extra.Sigmoid.nnapi = True/False  (Default is False)
                ActivationSymmetric = True/False: symmetrize calibration data for activations (default is False).
                WeightSymmetric = True/False: symmetrize calibration data for weights (default is True).
                EnableSubgraph = True/False :
                    Default is False. If enabled, subgraph will be quantized. Dynamic mode currently is supported. Will
                    support more in the future.
                ForceQuantizeNoInputCheck = True/False :
                    By default, some latent operators like maxpool, transpose, do not quantize if their input is not
                    quantized already. Setting to True to force such operator always quantize input and so generate
                    quantized output. Also the True behavior could be disabled per node using the nodes_to_exclude.
                MatMulConstBOnly = True/False:
                    Default is True for dynamic mode. If enabled, only MatMul with const B will be quantized.
    """
    from onnxruntime.quantization.registry import IntegerOpsRegistry

    extra_options = extra_options or {}
    nodes_to_exclude = nodes_to_exclude or []
    subgraphs_to_exclude = subgraphs_to_exclude or []
    nodes_to_quantize = nodes_to_quantize or []
    op_types_to_quantize = op_types_to_quantize or []

    mode = QuantizationMode.IntegerOps

    float_model: onnx.ModelProto = model_input if isinstance(model_input, onnx.ModelProto) else onnx.load(model_input)
    quant_model: onnx.ModelProto = onnx.ModelProto()  # the quantized model

    if not use_external_data_format:
        if float_model.ByteSize() > onnx.checker.MAXIMUM_PROTOBUF:
            use_external_data_format = True
            logger.warning("The model size is bigger than 2GB, have set use_external_data_format to True.")

    if crypto_mode:
        check_crypto_mode_arguments(extra_options, model_input, use_external_data_format)

    encrypt_algo = extra_options.get("EncryptionAlgorithm", None) if crypto_mode else None
    secret_key = os.urandom(48) if crypto_mode else None  # It's used to encrypt and decrypt data
    cache_dir = create_tmp_dir(prefix="quark_onnx.quant.")
    cache_path = Path(cache_dir.name).joinpath("cache_model.onnx").as_posix()
    float_model = cache_onnx_model_and_infer_shapes(
        float_model, cache_path, use_external_data_format, encrypt_algo, secret_key
    )

    if not op_types_to_quantize or len(op_types_to_quantize) == 0:
        op_types_to_quantize = list(IntegerOpsRegistry.keys())

    if not crypto_mode:
        print_quantize_dynamic_info(
            model_input,
            model_output,
            op_types_to_quantize,
            per_channel,
            reduce_range,
            weight_type,
            nodes_to_quantize,
            nodes_to_exclude,
            subgraphs_to_exclude,
            use_external_data_format,
            debug_mode,
            extra_options,
        )

    if subgraphs_to_exclude:
        nodes_to_exclude += match_exclude_subgraphs(float_model, subgraphs_to_exclude)
        nodes_to_exclude = list(set(nodes_to_exclude))

    pre_processed: bool = model_has_pre_process_metadata(float_model)
    if not pre_processed:
        logger.warning(
            "Please consider to run pre-processing before quantization. Refer to example: "
            "https://github.com/microsoft/onnxruntime-inference-examples/blob/main/quantization/image_classification"
            "/cpu/ReadMe.md "
        )

    if "MatMulConstBOnly" not in extra_options:
        extra_options["MatMulConstBOnly"] = True

    quantizer = ONNXQuantizer(
        float_model,
        per_channel,
        reduce_range,
        mode,
        False,  # static
        weight_type,
        QuantType.QUInt8,  # dynamic activation only supports uint8
        None,
        nodes_to_quantize,
        nodes_to_exclude,
        op_types_to_quantize,
        extra_options,
    )

    quantizer.quantize_model()
    quant_model = quantizer.model.model

    if model_output is None or crypto_mode:
        quant_model = onnx.shape_inference.infer_shapes(quant_model)
        return quant_model

    quant_model = save_and_reload_model_with_shape_infer(quant_model)
    save_onnx_model_with_external_data(quant_model, model_output, save_as_external_data=use_external_data_format)
    return None

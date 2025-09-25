import os
import sys
import torch

# Make "python/" importable as top-level modules
_THIS_DIR = os.path.dirname(__file__)
_PY_DIR = os.path.abspath(os.path.join(_THIS_DIR, "..", "python"))
if _PY_DIR not in sys.path:
    sys.path.insert(0, _PY_DIR)

from quantize import (
    compute_group_scales,
    quantize_int4_pack,
    dequantize_int4_packed,
    detect_outliers,
    apply_outlier_bypass,
)


@torch.no_grad()
def test_detect_outliers_zero_percent_returns_empty():
    torch.manual_seed(0)
    M, K = 8, 64
    W = torch.randn(M, K, dtype=torch.float32)

    idx, mask = detect_outliers(W, pct=0.0, axis="row", score="l2")

    assert idx.numel() == 0
    assert mask.shape == (M,)
    assert mask.dtype == torch.bool
    assert torch.count_nonzero(mask).item() == 0


@torch.no_grad()
def test_apply_outlier_bypass_rowwise():
    torch.manual_seed(1)
    M, K = 6, 32
    W = torch.randn(M, K, dtype=torch.float32)
    # Make row 2 and 5 strong outliers
    W[2] *= 100.0
    W[5] *= 50.0

    idx, mask = detect_outliers(W, pct=33.4, axis="row", score="l2")  # ceil(0.334*6)=3 rows
    assert idx.numel() == 3
    assert mask.sum().item() == 3

    W_q, outlier_w, meta = apply_outlier_bypass(W, idx, axis="row", store_dtype=torch.float16)

    # Selected rows are zeroed in quantizable tensor
    assert torch.allclose(W_q[idx, :], torch.zeros_like(W_q[idx, :]))
    # Outlier tensor matches original values for selected rows (up to cast)
    assert outlier_w.dtype == torch.float16
    assert torch.allclose(outlier_w.float(), W[idx, :])
    # Metadata soundness
    assert meta["axis"] == "row"
    assert tuple(meta["orig_shape"]) == (M, K)


@torch.no_grad()
def test_dequant_with_fp16_scales_matches_q_times_fp16_scale():
    torch.manual_seed(2)
    M, K = 4, 127
    group_size = 32
    W = torch.randn(M, K, dtype=torch.float32)

    # Compute FP32 scales for quantization
    scales_f32 = compute_group_scales(W, group_size=group_size, percentile=99.0)
    packed = quantize_int4_pack(W, scales_f32, group_size=group_size, pack_axis="K")

    # Dequant using FP16 scales like the on-disk format
    scales_f16 = scales_f32.to(torch.float16)
    W_dq_16 = dequantize_int4_packed(packed, scales_f16, group_size=group_size, K=K, dtype=torch.float32)

    # Build reference q from FP32 scales (same as quantization step)
    s_full_f32 = torch.repeat_interleave(scales_f32.to(torch.float32), group_size, dim=1)[:, :K]
    q_ref = torch.round(torch.clamp(W / torch.clamp(s_full_f32, min=1e-12), -7, 7)).to(torch.float32)

    # Multiply by FP16-expanded scales to float32
    s_full_16 = torch.repeat_interleave(scales_f16.to(torch.float32), group_size, dim=1)[:, :K]
    W_ref = q_ref * s_full_16

    # Exact equality expected (same math paths)
    assert torch.allclose(W_dq_16, W_ref, rtol=0.0, atol=1e-6)


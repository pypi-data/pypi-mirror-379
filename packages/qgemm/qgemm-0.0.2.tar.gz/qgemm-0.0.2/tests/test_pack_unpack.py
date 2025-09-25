import os
import sys
import math
import torch

# Make "python/" importable as top-level modules (quantize, convert_llama)
_THIS_DIR = os.path.dirname(__file__)
_PY_DIR = os.path.abspath(os.path.join(_THIS_DIR, "..", "python"))
if _PY_DIR not in sys.path:
    sys.path.insert(0, _PY_DIR)

from quantize import (
    compute_group_scales,
    quantize_int4_pack,
    unpack_packed_int4,
    dequantize_int4_packed,
)


def _build_full_scale(scales: torch.Tensor, K: int, group_size: int) -> torch.Tensor:
    return torch.repeat_interleave(scales.to(torch.float32), group_size, dim=1)[:, :K]


@torch.no_grad()
def test_pack_unpack_round_trip_exact_q():
    torch.manual_seed(0)
    M, K = 4, 127  # odd K to test tail byte
    group_size = 64
    W = torch.randn(M, K, dtype=torch.float32)

    scales = compute_group_scales(W, group_size=group_size, percentile=99.0)
    packed = quantize_int4_pack(W, scales, group_size=group_size, pack_axis="K")

    # Unpack to int4 values
    q = unpack_packed_int4(packed, K)

    # Reference q using same quant pipeline
    s_full = _build_full_scale(scales, K, group_size)
    q_ref = torch.round(torch.clamp(W / torch.clamp(s_full, min=1e-12), -7, 7)).to(torch.int8)

    assert q.shape == (M, K)
    assert torch.equal(q, q_ref)


@torch.no_grad()
def test_dequant_matches_q_times_scale():
    torch.manual_seed(1)
    M, K = 3, 256
    group_size = 64
    W = torch.randn(M, K, dtype=torch.float32)

    scales = compute_group_scales(W, group_size=group_size, percentile=99.0)
    packed = quantize_int4_pack(W, scales, group_size=group_size, pack_axis="K")

    # Dequantized via helper
    W_dq = dequantize_int4_packed(packed, scales, group_size=group_size, K=K, dtype=torch.float32)

    # Reference dequant = q_ref * s_full
    s_full = _build_full_scale(scales, K, group_size)
    q_ref = torch.round(torch.clamp(W / torch.clamp(s_full, min=1e-12), -7, 7)).to(torch.float32)
    W_ref = q_ref * s_full

    assert W_dq.shape == (M, K)
    assert torch.allclose(W_dq, W_ref, rtol=0.0, atol=1e-6)


@torch.no_grad()
def test_tail_nibble_zero_for_odd_K():
    torch.manual_seed(2)
    M, K = 2, 65  # odd K
    group_size = 32
    W = torch.randn(M, K, dtype=torch.float32)
    scales = compute_group_scales(W, group_size=group_size, percentile=99.0)
    packed = quantize_int4_pack(W, scales, group_size=group_size, pack_axis="K")

    # Last byte's high nibble should be zero by construction
    last_byte = packed[:, -1]
    high_nibble = (last_byte >> 4) & 0x0F
    # Only the leftover element uses the low nibble; high nibble is padding 0
    assert torch.count_nonzero(high_nibble).item() == 0

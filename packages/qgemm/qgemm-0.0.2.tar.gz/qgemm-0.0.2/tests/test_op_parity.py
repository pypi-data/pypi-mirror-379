import math
import os
import sys
import pytest
import torch

torch.manual_seed(0)

# Make "python/" importable as top-level modules (quantize, convert_llama)
_THIS_DIR = os.path.dirname(__file__)
_PY_DIR = os.path.abspath(os.path.join(_THIS_DIR, "..", "python"))
if _PY_DIR not in sys.path:
    sys.path.insert(0, _PY_DIR)

try:
    from quantize import compute_group_scales, quantize_int4_pack, dequantize_int4_packed
except Exception as e:  # pragma: no cover - tests will fail to import in some envs
    compute_group_scales = None
    quantize_int4_pack = None
    dequantize_int4_packed = None


def ops_available() -> bool:
    if not torch.cuda.is_available():
        return False
    if not hasattr(torch.ops, "qgemm"):
        return False
    return all(
        hasattr(torch.ops.qgemm, name)
        for name in ("int4_bias", "int4_bias_silu", "int4_bias_residual")
    )


pytestmark = pytest.mark.skipif(
    not ops_available() or compute_group_scales is None,
    reason="CUDA or qgemm ops not available, or quantize helpers missing",
)


def make_int4_weight(N: int, K: int, group_size: int, device: str = "cuda"):
    # Create a random full-precision weight [N, K]
    W = torch.randn(N, K, device=device, dtype=torch.float16)
    # Compute per-group scales (float32)
    scales = compute_group_scales(W.to(torch.float32), group_size=group_size, percentile=99.0)
    # Quantize and pack along K
    packed = quantize_int4_pack(W, scales, group_size=group_size, pack_axis="K")
    return packed.to(device), scales.to(device).to(torch.float16)


def baseline_mm(A: torch.Tensor, packed: torch.Tensor, scales: torch.Tensor, group_size: int) -> torch.Tensor:
    # A: [M,K] half (CUDA)
    # packed: [N, ceil(K/2)] uint8 (CUDA)
    # scales: [N, G] half (CUDA)
    M, K = A.shape
    N = packed.shape[0]
    # Dequantize to [N, K] on device
    B_t = dequantize_int4_packed(packed, scales.to(torch.float32), group_size=group_size, K=K, dtype=torch.float32)
    # Match kernel math: half*half accumulate in float, then epilogue in float and cast
    A_h = A.to(torch.float16)
    B_h = B_t.to(torch.float16)
    C = A_h.float() @ B_h.t().float()  # [M,N]
    return C


@pytest.mark.parametrize("M,K,N,group_size", [
    (1, 32, 64, 64),
    (7, 33, 65, 64),
    (16, 128, 96, 64),
    (64, 127, 64, 64),
])
def test_parity_bias(M, K, N, group_size):
    device = "cuda"
    A = torch.randn(M, K, device=device, dtype=torch.float16)
    packed, scales = make_int4_weight(N, K, group_size, device=device)
    bias = torch.randn(N, device=device, dtype=torch.float16)

    # kernel
    C_kernel = torch.ops.qgemm.int4_bias(A, packed, scales, group_size, bias)

    # baseline
    C_ref = baseline_mm(A, packed, scales, group_size)
    C_ref = C_ref + bias.float()

    mae = (C_kernel.float() - C_ref).abs().mean().item()
    assert mae < 3e-3, f"MAE too high: {mae}"


@pytest.mark.parametrize("M,K,N,group_size", [
    (1, 32, 64, 64),
    (7, 33, 65, 64),
    (16, 128, 96, 64),
    (64, 127, 64, 64),
])
def test_parity_bias_silu(M, K, N, group_size):
    device = "cuda"
    A = torch.randn(M, K, device=device, dtype=torch.float16)
    packed, scales = make_int4_weight(N, K, group_size, device=device)
    bias = torch.randn(N, device=device, dtype=torch.float16)

    # kernel
    C_kernel = torch.ops.qgemm.int4_bias_silu(A, packed, scales, group_size, bias)

    # baseline
    C_ref = baseline_mm(A, packed, scales, group_size)
    C_ref = C_ref + bias.float()
    C_ref = C_ref / (1.0 + torch.exp(-C_ref))  # SiLU

    mae = (C_kernel.float() - C_ref).abs().mean().item()
    assert mae < 3e-3, f"MAE too high: {mae}"


@pytest.mark.parametrize("M,K,N,group_size", [
    (1, 32, 64, 64),
    (7, 33, 65, 64),
    (16, 128, 96, 64),
    (64, 127, 64, 64),
])
def test_parity_bias_residual(M, K, N, group_size):
    device = "cuda"
    A = torch.randn(M, K, device=device, dtype=torch.float16)
    packed, scales = make_int4_weight(N, K, group_size, device=device)
    bias = torch.randn(N, device=device, dtype=torch.float16)
    residual = torch.randn(M, N, device=device, dtype=torch.float16)

    # kernel
    C_kernel = torch.ops.qgemm.int4_bias_residual(A, packed, scales, group_size, bias, residual)

    # baseline
    C_ref = baseline_mm(A, packed, scales, group_size)
    C_ref = C_ref + bias.float() + residual.float()

    mae = (C_kernel.float() - C_ref).abs().mean().item()
    assert mae < 3e-3, f"MAE too high: {mae}"

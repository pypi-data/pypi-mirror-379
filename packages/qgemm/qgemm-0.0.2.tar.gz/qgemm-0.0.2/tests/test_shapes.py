import os
import sys
import pytest
import torch

# Make "python/" importable as top-level modules (quantize, convert_llama)
_THIS_DIR = os.path.dirname(__file__)
_PY_DIR = os.path.abspath(os.path.join(_THIS_DIR, "..", "python"))
if _PY_DIR not in sys.path:
    sys.path.insert(0, _PY_DIR)

try:
    from quantize import compute_group_scales, quantize_int4_pack
except Exception:
    compute_group_scales = None
    quantize_int4_pack = None


def ops_available() -> bool:
    if not torch.cuda.is_available():
        return False
    if not hasattr(torch.ops, "qgemm"):
        return False
    return hasattr(torch.ops.qgemm, "int4_bias")


pytestmark = pytest.mark.skipif(
    not ops_available() or compute_group_scales is None,
    reason="CUDA or qgemm ops not available, or quantize helpers missing",
)


def make_inputs(M: int, K: int, N: int, group_size: int, device: str = "cuda"):
    A = torch.randn(M, K, device=device, dtype=torch.float16).contiguous()
    W = torch.randn(N, K, device=device, dtype=torch.float16)
    scales = compute_group_scales(W.to(torch.float32), group_size=group_size, percentile=99.0)
    packed = quantize_int4_pack(W, scales, group_size=group_size, pack_axis="K")
    bias = torch.randn(N, device=device, dtype=torch.float16)
    return A, packed.to(device), scales.to(device).to(torch.float16), bias


@pytest.mark.parametrize("M,K,N,group_size", [
    (1, 1, 1, 1),
    (2, 3, 4, 2),
    (4, 32, 64, 64),
    (17, 63, 65, 64),
    (64, 127, 129, 64),
])
def test_valid_shapes(M, K, N, group_size):
    A, packed, scales, bias = make_inputs(M, K, N, group_size)
    out = torch.ops.qgemm.int4_bias(A, packed, scales, group_size, bias)
    assert out.shape == (M, N)
    assert out.dtype == torch.float16


def test_bad_dtypes_and_contiguity():
    M, K, N, group_size = 4, 33, 65, 64
    A, packed, scales, bias = make_inputs(M, K, N, group_size)
    # Non-contiguous A
    A_nc = A.t().t()  # ensures same content but contiguous; make truly non-contiguous by slicing
    A_nc = A[:, ::2][:, : (K // 2)]  # non-contiguous view
    with pytest.raises(Exception):
        torch.ops.qgemm.int4_bias(A_nc, packed, scales, group_size, bias)

    # Wrong dtype for A
    with pytest.raises(Exception):
        torch.ops.qgemm.int4_bias(A.float(), packed, scales, group_size, bias)

    # Wrong dtype for B_packed
    with pytest.raises(Exception):
        torch.ops.qgemm.int4_bias(A, packed.to(torch.int32), scales, group_size, bias)

    # Wrong dtype for scales
    with pytest.raises(Exception):
        torch.ops.qgemm.int4_bias(A, packed, scales.to(torch.float32), group_size, bias)


def test_shape_mismatch():
    device = "cuda"
    M, K, N, group_size = 8, 33, 65, 64
    A = torch.randn(M, K, device=device, dtype=torch.float16)
    W = torch.randn(N, K, device=device, dtype=torch.float16)
    scales = compute_group_scales(W.to(torch.float32), group_size=group_size, percentile=99.0)
    packed = quantize_int4_pack(W, scales, group_size=group_size, pack_axis="K")

    # Break B_packed second dim (K_bytes)
    wrong_packed = packed[:, :-1].contiguous()
    with pytest.raises(Exception):
        torch.ops.qgemm.int4_bias(A, wrong_packed, scales.to(torch.float16), group_size, None)

    # Break scales G dimension
    wrong_scales = scales[:, :-1].contiguous()
    with pytest.raises(Exception):
        torch.ops.qgemm.int4_bias(A, packed, wrong_scales.to(torch.float16), group_size, None)

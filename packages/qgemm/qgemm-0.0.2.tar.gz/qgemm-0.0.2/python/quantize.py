from math import ceil
from typing import Any, Iterable, Optional, Tuple, Union, Literal

import torch
from loguru import logger

from torch import FloatTensor, IntTensor, Tensor


def compute_group_scales(
    weight: Tensor,
    group_size: int,
    percentile: float,
) -> Tensor:
    """
    Compute per-group quantization scales for INT4 using a percentile of |W|.

    Semantics: scale is the quantization step size such that the given
    percentile of |W| maps to the INT4 max magnitude (7).

    - weight: [M, K]
    - group_size: number of contiguous K elements per group
    - percentile: (0, 100] percentile of absolute values used as the clip level
    Returns: scales [M, ceil(K / group_size)] in float32 where
             scale = percentile(|W|) / 7.0 per group.
    """
    if weight.ndim != 2:
        raise ValueError(f"Expected 2D weight. Got: {weight.ndim}D")
    if group_size <= 0:
        raise ValueError(f"Group size must be greater than 0. Got: {group_size}")
    if not (0.0 < percentile <= 100.0):
        raise ValueError(f"Percentile must be in (0, 100]. Got: {percentile}")

    M, K = weight.shape
    num_groups = ceil(K / group_size)

    # allocate per-group scales: [M, num_groups]
    scales = torch.empty((M, num_groups), device=weight.device, dtype=torch.float32)

    # computes per-group percentiles of abs values
    abs_w = weight.to(torch.float32).abs()
    end = 0
    for g in range(num_groups):
        start = end
        end = min(start + group_size, K)
        group = abs_w[:, start:end]

        # compute percentile per row, then convert to step size by dividing by 7
        q = torch.quantile(group, q=percentile / 100.0, dim=1)
        q = torch.clamp(q, min=1e-12)
        scales[:, g] = q / 7.0
    return scales

def quantize_int4_pack(
    weight: Tensor,
    scales: Tensor,
    group_size: int,
    pack_axis: str,
):
    if weight.ndim != 2:
        raise ValueError(f"Expected 2D weight. Got: {weight.ndim}D")
    if group_size <= 0:
        raise ValueError(f"Group size must be greater than 0. Got: {group_size}")
    if pack_axis != "K":
        raise ValueError(f"Pack axis must be K. Got: {pack_axis}")
    
    M,K = weight.shape
    num_groups = ceil(K / group_size)

    if scales.shape != (M, num_groups):
        raise ValueError(f"Scales must be in shape [M, ceil(K / group_size)]. Got shapes: {scales.shape}")
    
    # use fp32 for stability
    W = weight.to(torch.float32)
    S = scales.to(torch.float32)

    # prepare output: 2 nibbles per byte along K
    # bytes per row
    K_bytes = ceil(K / 2)
    packed = torch.empty(
        (M, K_bytes), dtype = torch.uint8, device=weight.device
    )

    # per-row processing
    abs_max_q = 7  # symmetric int4 range is [-7, 7]
    for m in range(M):
        row = W[m] # [K]
        # build the per-element scale s_k for this row from per-group S[m, :]
        s_row = torch.empty_like(row, dtype=torch.float32)
        for g in range(num_groups):
            start = g * group_size
            end = min(start + group_size, K)
            s = S[m, g]
            s_row[start:end] = s
        
        # quantize: q = round(clip(W/s, -7..7))
        s_row = torch.clamp(s_row, min = 1e-12)

        q = torch.round(torch.clamp(
            row / s_row, 
            min = -abs_max_q,
            max = abs_max_q
        )).to(torch.int8) 

        # map signed int4 to nibble [0..15]
        q_nibble = (q & 0x0F).to(torch.uint8)  # [K] uint8 with 4 bits used

        # pack 2 nibbles per byte along K
        kb = 0
        k = 0
        while k + 1 < K:
            low = q_nibble[k]
            high = q_nibble[k + 1]
            packed[m, kb] = low | (high << 4)
            kb += 1
            k += 2
        if k < K:
            # odd tail
            low = q_nibble[k]
            packed[m, kb] = low # high nibble = 0
    return packed

def unpack_packed_int4(
    packed: Tensor,
    K: int,
) -> IntTensor:
    """
    Unpack uint8-packed INT4 values into int8 in [-8, 7].
    - packed: [M, ceil(K/2)] uint8 where low nibble is element k, high nibble is element k+1
    - K: original number of elements along K
    Returns: q_int4 [M, K] int8 with values in [-8, 7]
    """
    if packed.dtype != torch.uint8:
        raise ValueError("packed must be uint8")
    if packed.ndim != 2:
        raise ValueError("packed must be 2D [M, ceil(K/2)]")

    M, K_bytes = packed.shape
    if K_bytes != (K + 1) // 2:
        raise ValueError(f"packed second dim must be ceil(K/2). Got: {K_bytes} vs ceil({K}/2)")

    # Vectorized unpack: split low/high nibbles, interleave, trim to K
    low = packed & 0x0F
    high = (packed >> 4) & 0x0F
    interleaved = torch.stack((low, high), dim=-1).reshape(M, K_bytes * 2)
    nibbles = interleaved[:, :K].to(torch.int16)

    # Sign-extend from 4-bit two's complement to int8
    signed = nibbles.clone()
    signed[signed >= 8] -= 16
    return signed.to(torch.int8)

def dequantize_int4_packed(
    packed: Tensor,
    scales: Tensor,
    group_size: int,
    K: int,
    dtype: torch.dtype = torch.float32,
) -> Tensor:
    """
    Dequantize packed INT4 weights back to floating point using per-group scales.
    - packed: [M, ceil(K/2)] uint8
    - scales: [M, ceil(K/group_size)] float
    - group_size: int, number of contiguous K elements per group
    - K: original K length
    Returns: dequantized [M, K] tensor in `dtype`
    """
    if scales.ndim != 2 or packed.ndim != 2:
        raise ValueError("packed and scales must be 2D")
    M, K_bytes = packed.shape
    if K_bytes != (K + 1) // 2:
        raise ValueError("packed shape does not match K")
    num_groups = ceil(K / group_size)
    if scales.shape != (M, num_groups):
        raise ValueError(f"scales must be [M, ceil(K/group_size)], got {scales.shape}")

    # Unpack to int4 values in [-8, 7]
    q = unpack_packed_int4(packed, K=K).to(torch.int32)

    # Build per-element step sizes by repeating group scales along K
    s_full = torch.repeat_interleave(scales.to(torch.float32), repeats=group_size, dim=1)[:, :K]

    # Dequant
    out = (q.to(torch.float32) * s_full).to(dtype)
    return out

def detect_outliers(
    weight: Tensor,
    pct: float,
    axis: str = "row",
    score: str = "l2",
    group_size: Optional[int] = None,
    scales: Optional[Tensor] = None,
) -> Tuple[Tensor, Tensor]:
    if weight.ndim != 2:
        raise ValueError(f"weight must be [M,K], got {weight.shape}")
    if axis not in ("row", "col"):
        raise ValueError("axis must be 'row' or 'col'")
    if not (0.0 <= pct <= 100.0):
        raise ValueError("pct must be in [0, 100]")
    
    M, K = weight.shape
    dim = 1 if axis == "row" else 0
    n_channels = M if axis == "row" else K

    # interpret pct as a percentage in [0, 100]
    # allow zero outliers when pct == 0
    if pct == 0.0:
        idx = torch.empty(0, dtype=torch.long, device=weight.device)
        mask = torch.zeros(n_channels, dtype=torch.bool, device=weight.device)
        return idx, mask

    frac = pct / 100.0
    # use ceil for a conservative selection (never under-select for non-zero pct)
    k = int(ceil(frac * n_channels))

    W = weight.to(torch.float32)

    if score == "l2":
        # L2 score per channel: sum of squares along the reduction dim
        s = (W * W).sum(dim=dim)
    elif score == "est_error":
        if group_size is None or scales is None:
            raise ValueError("est_error requires group_size and scales")
        if axis != "row":
            raise NotImplementedError("est_error currently supports axis = 'row' only.")
        
        num_groups = ceil(K / group_size)
        if scales.shape != (M, num_groups):
            raise ValueError(f"scales must be [M, ceil(K / group_size)]. Got: {scales.shape}")
        
        abs_max_q = 7.0
        s_vals = []
        for m in range(M):
            row = W[m]  # [K]
            # build per-element scale vector along K
            s_row = torch.repeat_interleave(scales[m], group_size)[:K]
            s_row = torch.clamp(s_row, min=1e-12)

            q = torch.round(
                torch.clamp(row / s_row, min=-abs_max_q, max=abs_max_q)
            )

            err = row - s_row * q
            # MSE over K
            s_vals.append((err * err).mean())
        s = torch.stack(s_vals, dim=0)  # [M]
    else:
        raise ValueError(f"Unknown score '{score}'")
    
    # take top-k channels by score
    # if k >= n_channels, return all indices
    k = min(k, n_channels)
    if k == n_channels:
        idx = torch.arange(n_channels, device=weight.device)
    else:
        idx = torch.topk(s, k=k, largest=True, sorted=False).indices
    
    # build boolean mask in channel space.
    mask = torch.zeros(n_channels, dtype=torch.bool, device=weight.device)
    mask[idx] = True

    return idx, mask

def apply_outlier_bypass(
    weight: Tensor,
    outliers: Tensor,
    axis: Literal["row", "col"] = "row",
    store_dtype: torch.dtype = torch.float16
):
    if weight.ndim != 2:
        raise ValueError(f"Weight must be [M,K], got {weight.shape}")
    if axis not in ("row", "col"):
        raise ValueError("Axis must be 'row' or 'col'")
    if outliers.numel() == 0:
        # no outliers, trivial split
        return weight, torch.empty(0, device=weight.device, dtype=store_dtype), {
            "axis": axis,
            "indices": outliers.to(torch.int64),
            "orig_shape": tuple(weight.shape),
        }

    M, K = weight.shape
    outliers = outliers.to(torch.int64).to(weight.device)

    # validate bounds
    n_channels = M if axis == "row" else K
    if (outliers.min() < 0) or (outliers.max() >= n_channels):
        raise IndexError("Outlier indices out of bounds")

    # clone once to avoid touching original
    quantizable_w = weight.clone()

    if axis == "row":
        # extract outlier rows compactly and zero them 
        outlier_w = weight[outliers, :].to(store_dtype)
        quantizable_w[outliers, :] = 0
    else: 
        outlier_w = weight[:, outliers].to(store_dtype)
        quantizable_w[:, outliers] = 0

    metadata = {
        "axis": axis,
        "indices": outliers,         
        "orig_shape": (M, K),
        "outlier_shape": tuple(outlier_w.shape),
        "outlier_dtype": store_dtype,
    }

    return quantizable_w, outlier_w, metadata























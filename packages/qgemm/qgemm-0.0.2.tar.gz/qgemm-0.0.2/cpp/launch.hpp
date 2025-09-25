#pragma once

#include <ATen/ATen.h>
#include <c10/util/Optional.h>

namespace qgemm {

// Launch wrappers (host): validate and dispatch to CUDA kernels.

void gemm_int4_bias(
    const at::Tensor& A,                // [M, K], half, row-major contiguous
    const at::Tensor& B_packed,         // [N, ceil(K/2)], uint8
    const at::Tensor& scales,           // [N, G], half
    int64_t group_size,
    const c10::optional<at::Tensor>& bias, // [N], half
    at::Tensor& C_out                   // [M, N], half, row-major contiguous
);

void gemm_int4_bias_silu(
    const at::Tensor& A,
    const at::Tensor& B_packed,
    const at::Tensor& scales,
    int64_t group_size,
    const c10::optional<at::Tensor>& bias,
    at::Tensor& C_out
);

void gemm_int4_bias_residual(
    const at::Tensor& A,
    const at::Tensor& B_packed,
    const at::Tensor& scales,
    int64_t group_size,
    const c10::optional<at::Tensor>& bias,
    const c10::optional<at::Tensor>& residual,
    at::Tensor& C_out
);

} // namespace qgemm


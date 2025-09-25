#include <ATen/ATen.h>
#include <torch/library.h>
#include "launch.hpp"

namespace qgemm {

// Allocate output and dispatch to launchers

at::Tensor int4_bias(
    const at::Tensor& A,                // [M,K], half
    const at::Tensor& B_packed,         // [N, ceil(K/2)], uint8
    const at::Tensor& scales,           // [N, G], half
    int64_t group_size,
    c10::optional<at::Tensor> bias      // [N], half
) {
  TORCH_CHECK(A.is_cuda(), "A must be CUDA tensor");
  const auto M = A.size(0);
  const auto K = A.size(1);
  (void)K;
  const auto N = B_packed.size(0);
  at::Tensor C = at::empty({M, N}, A.options().dtype(at::kHalf));
  gemm_int4_bias(A, B_packed, scales, group_size, bias, C);
  return C;
}

at::Tensor int4_bias_silu(
    const at::Tensor& A,
    const at::Tensor& B_packed,
    const at::Tensor& scales,
    int64_t group_size,
    c10::optional<at::Tensor> bias
) {
  TORCH_CHECK(A.is_cuda(), "A must be CUDA tensor");
  const auto M = A.size(0);
  const auto N = B_packed.size(0);
  at::Tensor C = at::empty({M, N}, A.options().dtype(at::kHalf));
  gemm_int4_bias_silu(A, B_packed, scales, group_size, bias, C);
  return C;
}

at::Tensor int4_bias_residual(
    const at::Tensor& A,
    const at::Tensor& B_packed,
    const at::Tensor& scales,
    int64_t group_size,
    c10::optional<at::Tensor> bias,
    c10::optional<at::Tensor> residual
) {
  TORCH_CHECK(A.is_cuda(), "A must be CUDA tensor");
  const auto M = A.size(0);
  const auto N = B_packed.size(0);
  at::Tensor C = at::empty({M, N}, A.options().dtype(at::kHalf));
  gemm_int4_bias_residual(A, B_packed, scales, group_size, bias, residual, C);
  return C;
}

// Optional FP8 stub; not implemented yet.
at::Tensor fp8_bias(
    const at::Tensor& A,
    const at::Tensor& B_fp8,
    const at::Tensor& scales,
    c10::optional<at::Tensor> bias) {
  TORCH_CHECK(false, "qgemm.fp8_bias is not implemented in this build");
}

} // namespace qgemm

// Register ops into torch.ops.qgemm.*
TORCH_LIBRARY(qgemm, m) {
  m.def("int4_bias(Tensor A, Tensor B_packed, Tensor scales, int group_size, Tensor? bias=None) -> Tensor");
  m.def("int4_bias_silu(Tensor A, Tensor B_packed, Tensor scales, int group_size, Tensor? bias=None) -> Tensor");
  m.def("int4_bias_residual(Tensor A, Tensor B_packed, Tensor scales, int group_size, Tensor? bias=None, Tensor? residual=None) -> Tensor");
  m.def("fp8_bias(Tensor A, Tensor B_fp8, Tensor scales, Tensor? bias=None) -> Tensor");
}

TORCH_LIBRARY_IMPL(qgemm, CUDA, m) {
  m.impl("int4_bias", qgemm::int4_bias);
  m.impl("int4_bias_silu", qgemm::int4_bias_silu);
  m.impl("int4_bias_residual", qgemm::int4_bias_residual);
  m.impl("fp8_bias", qgemm::fp8_bias);
}


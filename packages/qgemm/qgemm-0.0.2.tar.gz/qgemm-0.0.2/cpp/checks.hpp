#pragma once

#include <ATen/ATen.h>
#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAException.h>
#include <c10/util/Optional.h>

namespace qgemm {

// Simple ceil-div helper
inline int64_t ceil_div_i64(int64_t a, int64_t b) { return (a + b - 1) / b; }

inline void check_cuda_tensor(const at::Tensor& t, const char* name) {
  TORCH_CHECK(t.is_cuda(), name, " must be a CUDA tensor");
}

inline void check_dtype(const at::Tensor& t, at::ScalarType dtype, const char* name) {
  TORCH_CHECK(t.scalar_type() == dtype,
              name, " must have dtype ", at::toString(dtype), 
              ", got ", at::toString(t.scalar_type()));
}

inline void check_dim(const at::Tensor& t, int64_t dim, const char* name) {
  TORCH_CHECK(t.dim() == dim, name, " must have dim=", dim, ", got ", t.dim());
}

inline void check_contiguous(const at::Tensor& t, const char* name) {
  TORCH_CHECK(t.is_contiguous(), name, " must be contiguous");
}

inline void check_same_device(const at::Tensor& a, const at::Tensor& b, const char* an, const char* bn) {
  TORCH_CHECK(a.get_device() == b.get_device(), an, " and ", bn, " must be on the same device");
}

inline void check_optional_same_device(const at::Tensor& a, const c10::optional<at::Tensor>& b, const char* an, const char* bn) {
  if (b.has_value() && b->defined()) {
    TORCH_CHECK(a.get_device() == b->get_device(), an, " and ", bn, " must be on the same device");
  }
}

inline void check_sm80_plus_or_throw() {
  // Use PyTorch's CUDA context to query current device properties
  auto* prop = at::cuda::getCurrentDeviceProperties();
  TORCH_CHECK(prop != nullptr, "Unable to query CUDA device properties");
  int cc_num = prop->major * 100 + prop->minor * 10;
  TORCH_CHECK(cc_num >= 800, "INT4 GEMM requires sm80+ (A100/H100). Got sm", prop->major, prop->minor);
}

// Shape contract checks for INT4 GEMM path
// A: [M,K] half, row-major contiguous
// B_packed: [N, ceil(K/2)] uint8, last-dim contiguous, stride(0) gives bytes between columns
// scales: [N, G] half, last-dim contiguous, where G = ceil(K/group_size)
// bias: [N] half (optional)
// residual: [M,N] half, row-major contiguous (optional)
inline void check_int4_gemm_inputs(
    const at::Tensor& A,
    const at::Tensor& B_packed,
    const at::Tensor& scales,
    int64_t group_size,
    const c10::optional<at::Tensor>& bias_opt,
    const c10::optional<at::Tensor>& residual_opt) {
  TORCH_CHECK(group_size > 0, "group_size must be positive");

  // Basic dtype/device
  check_cuda_tensor(A, "A");
  check_dtype(A, at::kHalf, "A");
  check_dim(A, 2, "A");
  check_contiguous(A, "A");

  check_cuda_tensor(B_packed, "B_packed");
  check_dtype(B_packed, at::kByte, "B_packed");
  check_dim(B_packed, 2, "B_packed");
  TORCH_CHECK(B_packed.stride(1) == 1, "B_packed must be contiguous along the K-bytes dimension (stride(1) == 1)");

  check_cuda_tensor(scales, "scales");
  check_dtype(scales, at::kHalf, "scales");
  check_dim(scales, 2, "scales");
  TORCH_CHECK(scales.stride(1) == 1, "scales must be contiguous along group dimension (stride(1) == 1)");

  if (bias_opt.has_value() && bias_opt->defined()) {
    const auto& bias = *bias_opt;
    check_cuda_tensor(bias, "bias");
    check_dtype(bias, at::kHalf, "bias");
    TORCH_CHECK(bias.dim() == 1 || (bias.dim() == 2 && bias.size(0) == 1),
                "bias must be 1D of size N (or [1, N])");
  }

  if (residual_opt.has_value() && residual_opt->defined()) {
    const auto& residual = *residual_opt;
    check_cuda_tensor(residual, "residual");
    check_dtype(residual, at::kHalf, "residual");
    check_dim(residual, 2, "residual");
    check_contiguous(residual, "residual");
  }

  // Same device
  check_same_device(A, B_packed, "A", "B_packed");
  check_same_device(A, scales, "A", "scales");
  check_optional_same_device(A, bias_opt, "A", "bias");
  check_optional_same_device(A, residual_opt, "A", "residual");

  // Shape compatibility
  const int64_t M = A.size(0);
  const int64_t K = A.size(1);
  const int64_t N = B_packed.size(0);
  const int64_t K_bytes = ceil_div_i64(K, 2);
  TORCH_CHECK(B_packed.size(1) == K_bytes,
              "B_packed shape mismatch: expected second dim ", K_bytes,
              ", got ", B_packed.size(1));

  const int64_t G = ceil_div_i64(K, group_size);
  TORCH_CHECK(scales.size(0) == N, "scales first dim must be N");
  TORCH_CHECK(scales.size(1) == G, "scales second dim must be ceil(K/group_size) = ", G);

  if (bias_opt.has_value() && bias_opt->defined()) {
    const auto& bias = *bias_opt;
    int64_t biasN = bias.dim() == 1 ? bias.size(0) : bias.size(1);
    TORCH_CHECK(biasN == N, "bias length must be N");
  }

  if (residual_opt.has_value() && residual_opt->defined()) {
    const auto& residual = *residual_opt;
    TORCH_CHECK(residual.size(0) == M && residual.size(1) == N,
                "residual must be [M, N]");
  }

  // Arch check
  check_sm80_plus_or_throw();
}

} // namespace qgemm


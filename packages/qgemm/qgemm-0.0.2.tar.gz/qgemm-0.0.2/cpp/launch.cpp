#include "launch.hpp"
#include "checks.hpp"

#include <ATen/cuda/CUDAContext.h>
#include <cuda_fp16.h>
#include <cuda_runtime_api.h>
#include <c10/cuda/CUDAException.h>

// Forward declarations of CUDA launchers (defined in cuda/int4_gemm.cu)
namespace qgemm {
cudaError_t launch_gemm_int4_bias(
    int M, int N, int K,
    const half* A, int lda,
    const uint8_t* B_packed, int ldb_bytes,
    const half* scales, int lds_groups,
    int group_size,
    const half* bias,
    half* C, int ldc,
    cudaStream_t stream);

cudaError_t launch_gemm_int4_bias_silu(
    int M, int N, int K,
    const half* A, int lda,
    const uint8_t* B_packed, int ldb_bytes,
    const half* scales, int lds_groups,
    int group_size,
    const half* bias,
    half* C, int ldc,
    cudaStream_t stream);

cudaError_t launch_gemm_int4_bias_residual(
    int M, int N, int K,
    const half* A, int lda,
    const uint8_t* B_packed, int ldb_bytes,
    const half* scales, int lds_groups,
    int group_size,
    const half* bias,
    const half* residual, int ldres,
    half* C, int ldc,
    cudaStream_t stream);
} // namespace qgemm

namespace qgemm {

static inline int64_t ceil_div_i64(int64_t a, int64_t b) { return (a + b - 1) / b; }

static inline void check_and_prep_common(
    const at::Tensor& A,
    const at::Tensor& B_packed,
    const at::Tensor& scales,
    int64_t group_size,
    const c10::optional<at::Tensor>& bias,
    const c10::optional<at::Tensor>& residual,
    at::Tensor& C_out,
    // out params
    int& M, int& N, int& K,
    int& lda, int& ldb_bytes, int& lds_groups, int& ldc,
    const half*& A_ptr, const uint8_t*& B_ptr, const half*& S_ptr, const half*& bias_ptr, const half*& residual_ptr,
    half*& C_ptr) {

  check_int4_gemm_inputs(A, B_packed, scales, group_size, bias, residual);

  // Sizes
  M = static_cast<int>(A.size(0));
  K = static_cast<int>(A.size(1));
  N = static_cast<int>(B_packed.size(0));
  const int64_t G = ceil_div_i64(K, static_cast<int>(group_size));

  // Output
  TORCH_CHECK(C_out.is_cuda(), "C_out must be CUDA tensor");
  TORCH_CHECK(C_out.scalar_type() == at::kHalf, "C_out must be half");
  TORCH_CHECK(C_out.sizes() == at::IntArrayRef({A.size(0), static_cast<int64_t>(N)}), "C_out shape must be [M, N]");
  TORCH_CHECK(C_out.is_contiguous(), "C_out must be contiguous");

  // Strides and pointers
  lda = static_cast<int>(A.stride(0));
  ldb_bytes = static_cast<int>(B_packed.stride(0)); // uint8 elements; equals bytes
  lds_groups = static_cast<int>(G);                 // groups per column
  ldc = static_cast<int>(C_out.stride(0));

  A_ptr = reinterpret_cast<const half*>(A.data_ptr<at::Half>());
  B_ptr = B_packed.data_ptr<uint8_t>();
  S_ptr = reinterpret_cast<const half*>(scales.data_ptr<at::Half>());
  bias_ptr = (bias.has_value() && bias->defined()) ? reinterpret_cast<const half*>(bias->data_ptr<at::Half>()) : nullptr;
  residual_ptr = (residual.has_value() && residual->defined()) ? reinterpret_cast<const half*>(residual->data_ptr<at::Half>()) : nullptr;
  C_ptr = reinterpret_cast<half*>(C_out.data_ptr<at::Half>());
}

void gemm_int4_bias(
    const at::Tensor& A,
    const at::Tensor& B_packed,
    const at::Tensor& scales,
    int64_t group_size,
    const c10::optional<at::Tensor>& bias,
    at::Tensor& C_out) {
  int M, N, K, lda, ldb_bytes, lds_groups, ldc;
  const half *A_ptr, *S_ptr, *bias_ptr, *residual_ptr;
  const uint8_t* B_ptr;
  half* C_ptr;
  check_and_prep_common(A, B_packed, scales, group_size, bias, /*residual=*/c10::nullopt,
                        C_out, M, N, K, lda, ldb_bytes, lds_groups, ldc,
                        A_ptr, B_ptr, S_ptr, bias_ptr, residual_ptr, C_ptr);

  auto stream = at::cuda::getCurrentCUDAStream();
  cudaError_t err = launch_gemm_int4_bias(
      M, N, K,
      A_ptr, lda,
      B_ptr, ldb_bytes,
      S_ptr, lds_groups,
      static_cast<int>(group_size),
      bias_ptr,
      C_ptr, ldc,
      stream.stream());
  C10_CUDA_CHECK(err);
}

void gemm_int4_bias_silu(
    const at::Tensor& A,
    const at::Tensor& B_packed,
    const at::Tensor& scales,
    int64_t group_size,
    const c10::optional<at::Tensor>& bias,
    at::Tensor& C_out) {
  int M, N, K, lda, ldb_bytes, lds_groups, ldc;
  const half *A_ptr, *S_ptr, *bias_ptr, *residual_ptr;
  const uint8_t* B_ptr;
  half* C_ptr;
  check_and_prep_common(A, B_packed, scales, group_size, bias, /*residual=*/c10::nullopt,
                        C_out, M, N, K, lda, ldb_bytes, lds_groups, ldc,
                        A_ptr, B_ptr, S_ptr, bias_ptr, residual_ptr, C_ptr);

  auto stream = at::cuda::getCurrentCUDAStream();
  cudaError_t err = launch_gemm_int4_bias_silu(
      M, N, K,
      A_ptr, lda,
      B_ptr, ldb_bytes,
      S_ptr, lds_groups,
      static_cast<int>(group_size),
      bias_ptr,
      C_ptr, ldc,
      stream.stream());
  C10_CUDA_CHECK(err);
}

void gemm_int4_bias_residual(
    const at::Tensor& A,
    const at::Tensor& B_packed,
    const at::Tensor& scales,
    int64_t group_size,
    const c10::optional<at::Tensor>& bias,
    const c10::optional<at::Tensor>& residual,
    at::Tensor& C_out) {
  int M, N, K, lda, ldb_bytes, lds_groups, ldc;
  const half *A_ptr, *S_ptr, *bias_ptr, *residual_ptr;
  const uint8_t* B_ptr;
  half* C_ptr;
  check_and_prep_common(A, B_packed, scales, group_size, bias, residual,
                        C_out, M, N, K, lda, ldb_bytes, lds_groups, ldc,
                        A_ptr, B_ptr, S_ptr, bias_ptr, residual_ptr, C_ptr);

  auto stream = at::cuda::getCurrentCUDAStream();
  int ldres = 0;
  if (residual.has_value() && residual->defined()) {
    ldres = static_cast<int>(residual->stride(0));
  }
  cudaError_t err = launch_gemm_int4_bias_residual(
      M, N, K,
      A_ptr, lda,
      B_ptr, ldb_bytes,
      S_ptr, lds_groups,
      static_cast<int>(group_size),
      bias_ptr,
      residual_ptr, ldres,
      C_ptr, ldc,
      stream.stream());
  C10_CUDA_CHECK(err);
}

} // namespace qgemm

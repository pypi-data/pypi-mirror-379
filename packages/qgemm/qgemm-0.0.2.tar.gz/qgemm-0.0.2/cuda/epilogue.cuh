#pragma once

#include <cuda_fp16.h>
#include <stdint.h>
#include <type_traits>

namespace qgemm {

// ----------------------
// Utility conversions
// ----------------------
template <typename T>
__device__ __forceinline__ float to_float(T x) {
  return static_cast<float>(x);
}

template <>
__device__ __forceinline__ float to_float<half>(half x) {
  return __half2float(x);
}

template <typename T>
__device__ __forceinline__ T from_float(float x);

template <>
__device__ __forceinline__ float from_float<float>(float x) { return x; }

template <>
__device__ __forceinline__ half from_float<half>(float x) { return __float2half_rn(x); }

// Fast SiLU in float32: x / (1 + exp(-x))
__device__ __forceinline__ float silu_f32(float x) {
  return x / (1.0f + __expf(-x));
}

// Half2 helpers for 2-lane vector epilogue
template <typename BiasT>
__device__ __forceinline__ half2 add_bias_cast_half2(float a0, float a1, const BiasT* bias, int n0) {
  float b0 = bias ? to_float<BiasT>(bias[n0 + 0]) : 0.0f;
  float b1 = bias ? to_float<BiasT>(bias[n0 + 1]) : 0.0f;
  return __floats2half2_rn(a0 + b0, a1 + b1);
}

template <typename BiasT>
__device__ __forceinline__ half2 silu_bias_cast_half2(float a0, float a1, const BiasT* bias, int n0) {
  float b0 = bias ? to_float<BiasT>(bias[n0 + 0]) : 0.0f;
  float b1 = bias ? to_float<BiasT>(bias[n0 + 1]) : 0.0f;
  float y0 = silu_f32(a0 + b0);
  float y1 = silu_f32(a1 + b1);
  return __floats2half2_rn(y0, y1);
}

template <typename ResidT>
__device__ __forceinline__ half2 add_bias_residual_cast_half2(float a0, float a1,
                                                              const ResidT* residual, int m, int n0, int ld_res,
                                                              const typename std::remove_const<ResidT>::type* /*tag*/,
                                                              const half* bias) {
  // This overload is not used; specialized below.
  return __floats2half2_rn(a0, a1);
}

template <typename ResidT, typename BiasT>
__device__ __forceinline__ half2 add_bias_residual_cast_half2(float a0, float a1,
                                                              const ResidT* residual, int m, int n0, int ld_res,
                                                              const BiasT* bias) {
  float r0 = residual ? to_float<ResidT>(residual[m * ld_res + (n0 + 0)]) : 0.0f;
  float r1 = residual ? to_float<ResidT>(residual[m * ld_res + (n0 + 1)]) : 0.0f;
  float b0 = bias ? to_float<BiasT>(bias[n0 + 0]) : 0.0f;
  float b1 = bias ? to_float<BiasT>(bias[n0 + 1]) : 0.0f;
  return __floats2half2_rn(a0 + b0 + r0, a1 + b1 + r1);
}

// ----------------------
// Epilogue Functors
// ----------------------

// BiasOnlyEpilogue: y = cast(acc + bias[n])
template <typename OutT = half, typename AccumT = float, typename BiasT = half>
struct BiasOnlyEpilogue {
  const BiasT* bias;  // [N] or nullptr

  __device__ __forceinline__ BiasOnlyEpilogue(const BiasT* bias_ = nullptr) : bias(bias_) {}

  __device__ __forceinline__ OutT operator()(AccumT acc, int /*m*/, int n) const {
    float v = static_cast<float>(acc);
    if (bias) v += to_float<BiasT>(bias[n]);
    return from_float<OutT>(v);
  }

  // Half2 convenience for two consecutive columns n and n+1 (only valid when OutT=half)
  __device__ __forceinline__ half2 apply2(AccumT acc0, AccumT acc1, int /*m*/, int n0) const {
    float a0 = static_cast<float>(acc0);
    float a1 = static_cast<float>(acc1);
    return add_bias_cast_half2<BiasT>(a0, a1, bias, n0);
  }
};

// BiasSiLUEpilogue: y = cast(silu(acc + bias[n]))
template <typename OutT = half, typename AccumT = float, typename BiasT = half>
struct BiasSiLUEpilogue {
  const BiasT* bias;  // [N] or nullptr

  __device__ __forceinline__ BiasSiLUEpilogue(const BiasT* bias_ = nullptr) : bias(bias_) {}

  __device__ __forceinline__ OutT operator()(AccumT acc, int /*m*/, int n) const {
    float v = static_cast<float>(acc);
    if (bias) v += to_float<BiasT>(bias[n]);
    v = silu_f32(v);
    return from_float<OutT>(v);
  }

  __device__ __forceinline__ half2 apply2(AccumT acc0, AccumT acc1, int /*m*/, int n0) const {
    float a0 = static_cast<float>(acc0);
    float a1 = static_cast<float>(acc1);
    return silu_bias_cast_half2<BiasT>(a0, a1, bias, n0);
  }
};

// BiasResidualEpilogue: y = cast(acc + bias[n] + residual[m, n])
template <typename OutT = half, typename AccumT = float, typename BiasT = half, typename ResidT = half>
struct BiasResidualEpilogue {
  const BiasT* bias;        // [N] or nullptr
  const ResidT* residual;   // [M, N] row-major or nullptr
  int ld_res;               // leading dimension of residual (N for row-major)

  __device__ __forceinline__ BiasResidualEpilogue(const BiasT* bias_ = nullptr,
                                                  const ResidT* residual_ = nullptr,
                                                  int ld_res_ = 0)
      : bias(bias_), residual(residual_), ld_res(ld_res_) {}

  __device__ __forceinline__ OutT operator()(AccumT acc, int m, int n) const {
    float v = static_cast<float>(acc);
    if (bias) v += to_float<BiasT>(bias[n]);
    if (residual) v += to_float<ResidT>(residual[m * ld_res + n]);
    return from_float<OutT>(v);
  }

  __device__ __forceinline__ half2 apply2(AccumT acc0, AccumT acc1, int m, int n0) const {
    float a0 = static_cast<float>(acc0);
    float a1 = static_cast<float>(acc1);
    float r0 = residual ? to_float<ResidT>(residual[m * ld_res + (n0 + 0)]) : 0.0f;
    float r1 = residual ? to_float<ResidT>(residual[m * ld_res + (n0 + 1)]) : 0.0f;
    float b0 = bias ? to_float<BiasT>(bias[n0 + 0]) : 0.0f;
    float b1 = bias ? to_float<BiasT>(bias[n0 + 1]) : 0.0f;
    return __floats2half2_rn(a0 + b0 + r0, a1 + b1 + r1);
  }
};

} // namespace qgemm

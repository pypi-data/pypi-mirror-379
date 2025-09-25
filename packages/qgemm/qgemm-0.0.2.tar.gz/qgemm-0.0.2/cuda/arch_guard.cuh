#pragma once

#include <stdint.h>

#if defined(__CUDACC__) || defined(__CUDA_ARCH__) || defined(CUDA_VERSION)
#include <cuda_runtime_api.h>
#endif

namespace qgemm {

// Convert (major, minor) to CUDA arch integer used by __CUDA_ARCH__ (e.g., 8.0 -> 800)
constexpr inline int arch_number(int major, int minor) { return major * 100 + minor * 10; }

// ------------------------
// Compile-time guards
// ------------------------
#if defined(__CUDA_ARCH__)
static constexpr int kCompiledArch = __CUDA_ARCH__;
#else
static constexpr int kCompiledArch = 0; // unknown / host-only compilation unit
#endif

#define QGEMM_COMPILED_ARCH qgemm::kCompiledArch

#define QGEMM_SM80_PLUS ((QGEMM_COMPILED_ARCH) >= 800)
#define QGEMM_SM90_PLUS ((QGEMM_COMPILED_ARCH) >= 900)

template <int Major, int Minor>
struct CompiledArchAtLeast {
  static constexpr bool value = (QGEMM_COMPILED_ARCH >= arch_number(Major, Minor));
};

// Device-available helper to check compiled arch at device side.
__host__ __device__ inline bool compiled_arch_at_least(int major, int minor) {
#if defined(__CUDA_ARCH__)
  return (__CUDA_ARCH__ >= arch_number(major, minor));
#else
  (void)major; (void)minor;
  return false;
#endif
}

// ------------------------
// Runtime guards (host)
// ------------------------

// Return current device compute capability number (e.g., 800 for sm80). Returns 0 on failure.
inline int device_compute_capability_number(int device = -1) {
#if defined(__CUDACC__) || defined(CUDA_VERSION)
  int dev = device;
  if (dev < 0) {
    if (cudaGetDevice(&dev) != cudaSuccess) return 0;
  }
  cudaDeviceProp prop{};
  if (cudaGetDeviceProperties(&prop, dev) != cudaSuccess) return 0;
  return arch_number(prop.major, prop.minor);
#else
  (void)device;
  return 0;
#endif
}

inline bool device_is_sm80_plus(int device = -1) {
  return device_compute_capability_number(device) >= 800;
}

inline bool device_is_sm90_plus(int device = -1) {
  return device_compute_capability_number(device) >= 900;
}

// Returns true if device compute capability is in [lo, hi] inclusive.
inline bool device_cc_in_range(int lo_cc, int hi_cc, int device = -1) {
  int cc = device_compute_capability_number(device);
  return (cc >= lo_cc) && (cc <= hi_cc);
}

} // namespace qgemm


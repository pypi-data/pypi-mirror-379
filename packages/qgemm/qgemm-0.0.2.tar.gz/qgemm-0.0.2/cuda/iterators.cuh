#pragma once

#include <stdint.h>
#include <cuda_fp16.h>

// CUTLASS-style lightweight iterators for operand B (packed INT4) and scales.
// Layout contracts are aligned with docs/weight_format.md and python/quantize.py:
// - B is stored column-major conceptually: each output channel (N-dim) is one column.
// - Along K, two int4 values are packed per byte (little nibbles: low=k, high=k+1).
// - Scales are shaped [N, ceil(K/group_size)] and map contiguously along group index.

namespace qgemm {

// Convert a scale value to float on device; specialized for half
template <typename T>
__device__ __forceinline__ float scale_to_float(T x) {
  return static_cast<float>(x);
}

template <>
__device__ __forceinline__ float scale_to_float<half>(half x) {
  return __half2float(x);
}

// Simple ceil-div helper.
__host__ __device__ __forceinline__ int ceil_div_int(int a, int b) {
  return (a + b - 1) / b;
}

// Combine 4 bytes from an unaligned address into a uint32_t (little endian),
// safe for any alignment. Prefer using this instead of casting to uint32_t*.
__device__ __forceinline__ uint32_t load_u32_unaligned(const uint8_t* ptr) {
  uint32_t v0 = static_cast<uint32_t>(ptr[0]);
  uint32_t v1 = static_cast<uint32_t>(ptr[1]) << 8;
  uint32_t v2 = static_cast<uint32_t>(ptr[2]) << 16;
  uint32_t v3 = static_cast<uint32_t>(ptr[3]) << 24;
  return v0 | v1 | v2 | v3;
}

// Iterator over packed INT4 B operand laid out by columns (N), each column has K elements
// packed along K into ceil(K/2) bytes. Template parameter PackedT is typically uint8_t.
template <typename PackedT = uint8_t>
struct ColMajorBInt4 {
  // Base pointer to packed bytes for B
  const PackedT* base;
  int K;               // number of elements along K (unpacked)
  int N;               // number of columns
  int K_bytes;         // ceil(K/2)
  int stride_col;      // bytes between start of consecutive columns (usually K_bytes)

  // Current logical position
  int n_col;           // current column index
  int k_elem;          // current K element index (even/odd allowed)

  __host__ __device__ ColMajorBInt4()
      : base(nullptr), K(0), N(0), K_bytes(0), stride_col(0), n_col(0), k_elem(0) {}

  __host__ __device__ ColMajorBInt4(const PackedT* base_, int K_, int N_)
      : base(base_), K(K_), N(N_), K_bytes(ceil_div_int(K_, 2)), stride_col(ceil_div_int(K_, 2)), n_col(0), k_elem(0) {}

  __host__ __device__ ColMajorBInt4(const PackedT* base_, int K_, int N_, int stride_col_bytes)
      : base(base_), K(K_), N(N_), K_bytes(ceil_div_int(K_, 2)), stride_col(stride_col_bytes), n_col(0), k_elem(0) {}

  // Set tile origin
  __host__ __device__ inline void set_origin(int k0, int n0) {
    k_elem = k0;
    n_col = n0;
  }

  // Advance along K by delta elements (can be negative)
  __host__ __device__ inline void advance_k(int delta_elems) { k_elem += delta_elems; }
  // Advance along N by delta columns
  __host__ __device__ inline void advance_n(int delta_cols) { n_col += delta_cols; }

  // Compute byte address for current (k_elem, n_col). The starting byte index is floor(k/2).
  __host__ __device__ inline const uint8_t* byte_ptr(int k_offset_elems = 0, int n_offset_cols = 0) const {
    int kb = (k_elem + k_offset_elems) >> 1; // floor division by 2
    int nc = (n_col + n_offset_cols);
    return reinterpret_cast<const uint8_t*>(base) + static_cast<size_t>(nc) * stride_col + kb;
  }

  // Guarded 4-byte load: if the request crosses the end of the column (K_bytes), pad trailing bytes with zero.
  // Returns the 32-bit little-endian word containing up to 8 nibbles.
  __device__ __forceinline__ uint32_t load_u32_guarded(int k_byte_offset = 0, int n_col_offset = 0) const {
    const int kb0 = ((k_elem) >> 1) + k_byte_offset;
    const int nc = n_col + n_col_offset;
    const uint8_t* col_base = reinterpret_cast<const uint8_t*>(base) + static_cast<size_t>(nc) * stride_col;

    // Compute how many bytes are valid starting at kb0 (0..4)
    int remaining = K_bytes - kb0;
    int valid = remaining >= 4 ? 4 : (remaining <= 0 ? 0 : remaining);

    if (valid == 4) {
      // Unaligned-safe load
      return load_u32_unaligned(col_base + kb0);
    }
    uint32_t v = 0u;
    #pragma unroll
    for (int i = 0; i < 4; ++i) {
      uint32_t b = (i < valid) ? static_cast<uint32_t>(col_base[kb0 + i]) : 0u;
      v |= (b << (8 * i));
    }
    return v;
  }
};

// Iterator for per-group scales shaped [N, G], where G = ceil(K / group_size).
// Provides helpers to fetch one scale for a K index, or 8 scales for a block [k, k+7].
template <typename ScaleT = float>
struct ScaleIterator {
  const ScaleT* base;  // pointer to [N, G] row-major w.r.t. G (contiguous groups per column)
  int N;               // columns
  int G;               // groups per column
  int group_size;      // number of K elements per group
  int n_col;           // current column
  int k_elem;          // current K element

  __host__ __device__ ScaleIterator()
      : base(nullptr), N(0), G(0), group_size(1), n_col(0), k_elem(0) {}

  __host__ __device__ ScaleIterator(const ScaleT* base_, int N_, int K_, int group_size_)
      : base(base_), N(N_), G(ceil_div_int(K_, group_size_)), group_size(group_size_), n_col(0), k_elem(0) {}

  __host__ __device__ ScaleIterator(const ScaleT* base_, int N_, int G_, int group_size_, bool precomputed_G)
      : base(base_), N(N_), G(G_), group_size(group_size_), n_col(0), k_elem(0) {
    (void)precomputed_G; // tag overload to distinguish
  }

  __host__ __device__ inline void set_origin(int k0, int n0) { k_elem = k0; n_col = n0; }
  __host__ __device__ inline void advance_k(int delta) { k_elem += delta; }
  __host__ __device__ inline void advance_n(int delta) { n_col += delta; }

  // Return scale for (k_elem + k_off, n_col + n_off)
  __device__ __forceinline__ float load_scale(int k_off = 0, int n_off = 0) const {
    int k = k_elem + k_off;
    int n = n_col + n_off;
    int g = k / group_size; // floor
    g = (g < 0) ? 0 : (g >= G ? (G - 1) : g);
    const ScaleT* col = base + static_cast<size_t>(n) * G;
    return scale_to_float<ScaleT>(col[g]);
  }

  // Whether [k, k+7] resides in the same group
  __host__ __device__ inline bool block8_uniform(int k) const {
    int g0 = k / group_size;
    int g7 = (k + 7) / group_size;
    return g0 == g7;
  }

  // Load 8 per-element scales for [k_elem, k_elem+7] into out8
  __device__ __forceinline__ void load_scales8(float out8[8]) const {
    int k0 = k_elem;
    const ScaleT* col = base + static_cast<size_t>(n_col) * G;
    if (block8_uniform(k0)) {
      int g = k0 / group_size;
      float s = scale_to_float<ScaleT>(col[g]);
      #pragma unroll
      for (int i = 0; i < 8; ++i) out8[i] = s;
      return;
    }
    #pragma unroll
    for (int i = 0; i < 8; ++i) {
      int g = (k0 + i) / group_size;
      g = (g < 0) ? 0 : (g >= G ? (G - 1) : g);
      out8[i] = scale_to_float<ScaleT>(col[g]);
    }
  }
};

} // namespace qgemm

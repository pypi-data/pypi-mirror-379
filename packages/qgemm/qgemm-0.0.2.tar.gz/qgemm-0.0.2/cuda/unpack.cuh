#pragma once

#include <stdint.h>
#include <cuda_fp16.h>

// Lightweight helpers for INT4 unpack + dequant on GPU.
// Matches the Python reference in python/quantize.py and docs/weight_format.md:
// - Little-nibbles packing (low: k, high: k+1)
// - Two's complement 4-bit mapping to [-8, 7]

namespace qgemm {

// Sign-extend a 4-bit two's complement nibble (0..15) to int8 [-8, 7].
__device__ __forceinline__ int8_t sign_extend_4bit(uint8_t nibble) {
  // Branchless map: x in [0..15] -> (x ^ 8) - 8
  // 0..7 -> 0..7, 8..15 -> -8..-1
  return static_cast<int8_t>((static_cast<int>(nibble & 0x0F) ^ 0x8) - 0x8);
}

// Unpack 4 bytes (8 nibbles) into 8 signed int4 values in registers.
// Input layout per byte b: low nibble = element k, high nibble = element k+1.
// Output order: [b0_low, b0_high, b1_low, b1_high, b2_low, b2_high, b3_low, b3_high]
__device__ __forceinline__ void unpack_uint8_to_int8x8(uint32_t bytes4, int8_t out[8]) {
  // Process each byte independently; rely on compiler to keep in registers.
  #pragma unroll
  for (int i = 0; i < 4; ++i) {
    uint8_t byte_i = static_cast<uint8_t>((bytes4 >> (8 * i)) & 0xFFu);
    uint8_t low = byte_i & 0x0Fu;
    uint8_t high = (byte_i >> 4) & 0x0Fu;
    out[2 * i + 0] = sign_extend_4bit(low);
    out[2 * i + 1] = sign_extend_4bit(high);
  }
}

// Dequantize 8x INT4 packed in 4 bytes using a single scale to 8 half values.
// Useful when the group_size is a multiple of 8 and the 8-tuple sits entirely in one group.
__device__ __forceinline__ void dequant_int4_block_to_half(
    uint32_t bytes4,
    float scale,
    half out[8]) {
  int8_t q[8];
  unpack_uint8_to_int8x8(bytes4, q);
  #pragma unroll
  for (int i = 0; i < 8; ++i) {
    out[i] = __float2half(static_cast<float>(q[i]) * scale);
  }
}

// Variant returning half2 vectors for efficient stores/accumulators.
__device__ __forceinline__ void dequant_int4_block_to_half2(
    uint32_t bytes4,
    float scale,
    half2 &h01,
    half2 &h23,
    half2 &h45,
    half2 &h67) {
  int8_t q[8];
  unpack_uint8_to_int8x8(bytes4, q);
  float f0 = static_cast<float>(q[0]) * scale;
  float f1 = static_cast<float>(q[1]) * scale;
  float f2 = static_cast<float>(q[2]) * scale;
  float f3 = static_cast<float>(q[3]) * scale;
  float f4 = static_cast<float>(q[4]) * scale;
  float f5 = static_cast<float>(q[5]) * scale;
  float f6 = static_cast<float>(q[6]) * scale;
  float f7 = static_cast<float>(q[7]) * scale;
  h01 = __floats2half2_rn(f0, f1);
  h23 = __floats2half2_rn(f2, f3);
  h45 = __floats2half2_rn(f4, f5);
  h67 = __floats2half2_rn(f6, f7);
}

// Per-element scale variant: accepts 8 independent scales (float) and outputs 8 halfs.
__device__ __forceinline__ void dequant_int4_block_to_half(
    uint32_t bytes4,
    const float *scales8,
    half out[8]) {
  int8_t q[8];
  unpack_uint8_to_int8x8(bytes4, q);
  #pragma unroll
  for (int i = 0; i < 8; ++i) {
    out[i] = __float2half(static_cast<float>(q[i]) * scales8[i]);
  }
}

} // namespace qgemm


#include <cuda.h>
#include <cuda_fp16.h>
#include <mma.h>

#include "unpack.cuh"
#include "iterators.cuh"
#include "epilogue.cuh"
#include "arch_guard.cuh"

using namespace nvcuda;

namespace qgemm {
    #if defined(__CUDA_ARCH__) && (__CUDA_ARCH__ >= 800)
    #define QGEMM_CP_ASYNC_SUPPORTED 1
    #else
    #define QGEMM_CP_ASYNC_SUPPORTED 0
    #endif 

    #if QGEMM_CP_ASYNC_SUPPORTED
    __device__ __forceinline__ void cp_async_ca(void* smem_ptr, const void * gmem_ptr) {
        // cp.async expects a shared memory address (32-bit) for the destination.
        unsigned smem_addr = static_cast<unsigned>(__cvta_generic_to_shared(smem_ptr));
        asm volatile(
            "cp.async.ca.shared.global [%0], [%1], %2;\n" :: "r"(smem_addr), "l"(gmem_ptr), "n"(16)
        );
    }
    __device__ __forceinline__ void cp_async_commit() {
        asm volatile("cp.async.commit_group;\n" ::);
    }
    __device__ __forceinline__ void cp_async_wait(int groups) {
        asm volatile("cp.async.wait_group %0;\n" :: "n"(groups));
    }
    #endif
    
    // move to a 64x64x32 tile per threadblock with 4 warps.
    // each warp computes a 2x2 array of WMMA tiles (4 tiles per warp) 
    static constexpr int TB_M = 64; // threadblock tile in M
    static constexpr int TB_N = 64; // threadblock tile in N
    static constexpr int TB_K = 32; // threadblock tile in K (iterates in 16‑wide WMMA steps)
    static constexpr int WARPS_PER_BLOCK = 4; // 4 warps
    static constexpr int THREADS = 128;

    // WMMA tile config: 16x16x16 for fp16
    static constexpr int WMMA_M = 16;
    static constexpr int WMMA_N = 16;
    static constexpr int WMMA_K = 16;

    template <typename ScaleT, typename Epilogue>
    __global__ void int4_gemm_kernel_fp16tc(
        // problem sizes
        int M, int N, int K,
        // A: [M, K], row-major
        const half* __restrict__ A, int lda,
        // B (packed): column-major by N, each column has ceil(K/2) bytes
        const uint8_t* __restrict__ B_packed, int ldb_bytes,
        // scales: [N, G], G=ceil(K/group_size)
        const ScaleT* __restrict__ scales, int lds_groups,
        int group_size,
        // output
        half * __restrict__ C, int ldc,
        // epilogue functor
    Epilogue epilogue
    )
    {
        // block origin in output space
        const int block_m0 = blockIdx.y * TB_M;
        const int block_n0 = blockIdx.x * TB_N;

        // warp and lane
        const int warp_id = threadIdx.x / 32;
        const int lane_id = threadIdx.x % 32;

        // shared memory layout (double-buffer A and packed B bytes; single buffer for B half tile)
        // [A0 (TB_M x TB_K half)] [A1 (TB_M x TB_K half)] [Bbytes0 (TB_N x (TB_K/2) bytes)]
        // [Bbytes1 (TB_N x (TB_K/2) bytes)] [Bhalf (TB_K x TB_N half)]
        extern __shared__ uint8_t smem_raw[];
        half* smemA0 = reinterpret_cast<half*>(smem_raw);
        half* smemA1 = smemA0 + TB_M * TB_K;
        uint8_t* smemBbytes0 = reinterpret_cast<uint8_t*>(smemA1 + TB_M * TB_K);
        uint8_t* smemBbytes1 = smemBbytes0 + TB_N * (TB_K / 2);
        half* smemB = reinterpret_cast<half*>(smemBbytes1 + TB_N * (TB_K / 2));
        // B half tile stored as column-major [TB_K x TB_N] so we can load matrix_b as col_major

        // map warp to a 2x2 array of 16x16 tiles inside the 64x64 threadblock tile
        const int warp_group_m = (warp_id >> 1); // 0..1
        const int warp_group_n = (warp_id & 1);  // 0..1
        const int warp_m_base = warp_group_m * 2 * WMMA_M; // 0 or 32
        const int warp_n_base = warp_group_n * 2 * WMMA_N; // 0 or 32

        // initialize WMMA accumulator fragments in fp32 (4 tiles per warp)
        wmma::fragment<wmma::accumulator, WMMA_M, WMMA_N, WMMA_K, float> acc_frag[2][2];
        #pragma unroll
        for (int mi = 0; mi < 2; ++mi) {
            #pragma unroll
            for (int nj = 0; nj < 2; ++nj) {
                wmma::fill_fragment(acc_frag[mi][nj], 0.0f);
            }
        }

        // loop over K in TB_K steps (2-stage pipeline with cp.async for full tiles)
        int stage = 0;
        int k_cur = 0;
        bool async_curr = false;

        // hoist a per-thread ScaleIterator; set origin per dequant block
        ScaleIterator<ScaleT> scale_it(scales, N, lds_groups, group_size, /*precomputed_G=*/true);

        // prologue: preload tile 0
        if (k_cur + TB_K <= K) {
        #if QGEMM_CP_ASYNC_SUPPORTED
            // A tile: TB_M rows, each row has BYTES_PER_A_ROW bytes split into 16B segments
            const int BYTES_PER_A_ROW = TB_K * int(sizeof(half));
            const int A_SEGS_PER_ROW = BYTES_PER_A_ROW / 16; // 4 for TB_K=32
            const int A_TOTAL_SEGS = TB_M * A_SEGS_PER_ROW;
            uint8_t* smemA_bytes = reinterpret_cast<uint8_t*>(smemA0);
            const uint8_t* gA_base = reinterpret_cast<const uint8_t*>(A + block_m0 * lda + k_cur);
            for (int seg = threadIdx.x; seg < A_TOTAL_SEGS; seg += blockDim.x) {
                int i = seg / A_SEGS_PER_ROW;
                int t = seg % A_SEGS_PER_ROW;
                int global_m = block_m0 + i;
                if (global_m < M) {
                    const uint8_t* g_row = reinterpret_cast<const uint8_t*>(A + global_m * lda + k_cur);
                    cp_async_ca(smemA_bytes + (i * BYTES_PER_A_ROW + t * 16), g_row + t * 16);
                }
            }

            // B packed bytes tile: TB_N columns x (TB_K/2) bytes per column (16 B)
            const int KB0 = (k_cur >> 1);
            const int BYTES_PER_COL = (TB_K / 2);
            for (int j = threadIdx.x; j < TB_N; j += blockDim.x) {
                int global_n = block_n0 + j;
                if (global_n < N) {
                    const uint8_t* col_base = B_packed + static_cast<size_t>(global_n) * ldb_bytes + KB0;
                    cp_async_ca(smemBbytes0 + j * BYTES_PER_COL, col_base);
                }
            }
            cp_async_commit();
            async_curr = true;
        #else
            async_curr = false;
        #endif
        }

        while (k_cur < K) {
            // if current tile was prefetched asynchronously, wait for the copies to complete.
            if (async_curr) {
            #if QGEMM_CP_ASYNC_SUPPORTED
                cp_async_wait(0);
            #endif
            }
            __syncthreads();

            // if not prefetched (partial tail or arch), fill A tile and B bytes synchronously now.
            if (!async_curr) {
                // A tile synchronous fill
                for (int idx = threadIdx.x; idx < TB_M * TB_K; idx += blockDim.x) {
                    int i = idx / TB_K; // [0, TB_M)
                    int kk = idx % TB_K; // [0, TB_K)
                    int global_m = block_m0 + i;
                    int global_k = k_cur + kk;
                    half val = __float2half(0.0f);
                    if (global_m < M && global_k < K) {
                        val = A[global_m * lda + global_k];
                    }
                    (stage == 0 ? smemA0 : smemA1)[i * TB_K + kk] = val;
                }
                // B bytes synchronous fill with guard
                const int KB0_sync = (k_cur >> 1);
                const int BYTES_PER_COL = (TB_K / 2);
                for (int j = threadIdx.x; j < TB_N; j += blockDim.x) {
                    int global_n = block_n0 + j;
                    uint8_t* dst_col = (stage == 0 ? smemBbytes0 : smemBbytes1) + j * BYTES_PER_COL;
                    if (global_n < N) {
                        const uint8_t* col_base = B_packed + static_cast<size_t>(global_n) * ldb_bytes + KB0_sync;
                        // copy up to BYTES_PER_COL within bounds of column
                        #pragma unroll
                        for (int b = 0; b < BYTES_PER_COL; ++b) {
                            int kb = KB0_sync + b;
                            dst_col[b] = (kb < (ldb_bytes)) ? col_base[b] : 0u;
                        }
                    } else {
                        #pragma unroll
                        for (int b = 0; b < BYTES_PER_COL; ++b) dst_col[b] = 0u;
                    }
                }
                __syncthreads();
            }

            // build B half tile from packed bytes in shared
            const int K_BLOCKS8 = (TB_K + 7) / 8; // TB_K is multiple of 8
            const int KB0_tile = (k_cur >> 1);
            const uint8_t* sbbytes = (stage == 0 ? smemBbytes0 : smemBbytes1);
            for (int idx = threadIdx.x; idx < TB_N * K_BLOCKS8; idx += blockDim.x) {
                int j = idx / K_BLOCKS8;          // [0, TB_N)
                int kk8 = (idx % K_BLOCKS8) * 8;  // [0, TB_K) in steps of 8
                int global_n = block_n0 + j;
                int global_k0 = k_cur + kk8;

                // default zeros if out of range
                if (global_n >= N || global_k0 >= K) {
                    #pragma unroll
                    for (int t = 0; t < 8; ++t) smemB[j * TB_K + (kk8 + t)] = __float2half(0.0f);
                    continue;
                }

                // read 4 bytes from smem packed bytes for this column at relative offset
                const uint8_t* col_bytes = sbbytes + j * (TB_K / 2);
                int rel_kb = ((global_k0 >> 1) - KB0_tile);
                uint32_t bytes4 = 0u;
                // construct little-endian 4 bytes
                #pragma unroll
                for (int b = 0; b < 4; ++b) {
                    uint32_t byte_v = static_cast<uint32_t>(col_bytes[rel_kb + b]);
                    bytes4 |= (byte_v << (8 * b));
                }

                // iterate scales
                scale_it.set_origin(global_k0, global_n);
                if (scale_it.block8_uniform(global_k0)) {
                    float s = scale_it.load_scale();
                    half2 h01, h23, h45, h67;
                    dequant_int4_block_to_half2(bytes4, s, h01, h23, h45, h67);
                    half2* dst = reinterpret_cast<half2*>(smemB + j * TB_K + kk8);
                    dst[0] = h01; dst[1] = h23; dst[2] = h45; dst[3] = h67;
                } else {
                    float s8[8];
                    scale_it.load_scales8(s8);
                    half h8[8];
                    dequant_int4_block_to_half(bytes4, s8, h8);
                    #pragma unroll
                    for (int t = 0; t < 8; ++t) smemB[j * TB_K + (kk8 + t)] = h8[t];
                }
            }
            __syncthreads();

            // iterate over K-subtiles in WMMA_K=16 increments for current stage
            for (int kk = 0; kk < TB_K; kk += WMMA_K) {
                wmma::fragment<wmma::matrix_a, WMMA_M, WMMA_N, WMMA_K, half, wmma::row_major> a_frag[2];
                wmma::fragment<wmma::matrix_b, WMMA_M, WMMA_N, WMMA_K, half, wmma::col_major> b_frag[2];

                #pragma unroll
                for (int mi = 0; mi < 2; ++mi) {
                    const int a_row0 = warp_m_base + mi * WMMA_M;
                    const half* a_ptr = (stage == 0 ? smemA0 : smemA1) + a_row0 * TB_K + kk;
                    wmma::load_matrix_sync(a_frag[mi], a_ptr, TB_K);
                }
                #pragma unroll
                for (int nj = 0; nj < 2; ++nj) {
                    const int b_col0 = warp_n_base + nj * WMMA_N;
                    const half* b_ptr = smemB + b_col0 * TB_K + kk;
                    wmma::load_matrix_sync(b_frag[nj], b_ptr, TB_K);
                }

                #pragma unroll
                for (int mi = 0; mi < 2; ++mi) {
                    #pragma unroll
                    for (int nj = 0; nj < 2; ++nj) {
                        wmma::mma_sync(acc_frag[mi][nj], a_frag[mi], b_frag[nj], acc_frag[mi][nj]);
                    }
                }
            }

            // prefetch next tile asynchronously if a full tile remains
            int k_next = k_cur + TB_K;
            bool next_async = false;
            if (k_next + TB_K <= K) {
            #if QGEMM_CP_ASYNC_SUPPORTED
                int next_stage = stage ^ 1;
                // A next tile
                const int BYTES_PER_A_ROW = TB_K * int(sizeof(half));
                const int A_SEGS_PER_ROW = BYTES_PER_A_ROW / 16;
                const int A_TOTAL_SEGS = TB_M * A_SEGS_PER_ROW;
                uint8_t* smemA_bytes_next = reinterpret_cast<uint8_t*>(next_stage == 0 ? smemA0 : smemA1);
                for (int seg = threadIdx.x; seg < A_TOTAL_SEGS; seg += blockDim.x) {
                    int i = seg / A_SEGS_PER_ROW;
                    int t = seg % A_SEGS_PER_ROW;
                    int global_m = block_m0 + i;
                    if (global_m < M) {
                        const uint8_t* g_row = reinterpret_cast<const uint8_t*>(A + global_m * lda + k_next);
                        cp_async_ca(smemA_bytes_next + (i * BYTES_PER_A_ROW + t * 16), g_row + t * 16);
                    }
                }
                // B next tile bytes
                const int KB1 = (k_next >> 1);
                const int BYTES_PER_COL = (TB_K / 2);
                uint8_t* sbbytes_next = (next_stage == 0 ? smemBbytes0 : smemBbytes1);
                for (int j = threadIdx.x; j < TB_N; j += blockDim.x) {
                    int global_n = block_n0 + j;
                    if (global_n < N) {
                        const uint8_t* col_base = B_packed + static_cast<size_t>(global_n) * ldb_bytes + KB1;
                        cp_async_ca(sbbytes_next + j * BYTES_PER_COL, col_base);
                    }
                }
                cp_async_commit();
                next_async = true;
            #endif
            }

            // advance to next tile
            stage ^= 1;
            k_cur = k_next;
            async_curr = next_async;
        }

        // epilogue: write out 4x 16x16 tiles per warp with fusion
        #pragma unroll
        for (int mi = 0; mi < 2; ++mi) {
            #pragma unroll
            for (int nj = 0; nj < 2; ++nj) {
                const int c_row0 = block_m0 + warp_m_base + mi * WMMA_M;
                const int c_col0 = block_n0 + warp_n_base + nj * WMMA_N;

                float acc_buf[WMMA_M * WMMA_N];
                wmma::store_matrix_sync(acc_buf, acc_frag[mi][nj], WMMA_N, wmma::mem_row_major);

                for (int i = 0; i < WMMA_M; ++i) {
                    int m = c_row0 + i;
                    if (m >= M) continue;
                    int n0 = c_col0;
                    // store two columns at a time via epilogue.apply2
                    for (int j = 0; j < WMMA_N; j += 2) {
                        int n_pair0 = n0 + j;
                        if (n_pair0 >= N) break;
                        float a0 = acc_buf[i * WMMA_N + (j + 0)];
                        float a1 = (n_pair0 + 1 < N) ? acc_buf[i * WMMA_N + (j + 1)] : 0.0f;
                        half2 out2 = epilogue.apply2(a0, a1, m, n_pair0);
                        // conservative scalar stores to avoid alignment constraints
                        half out_h0 = __low2half(out2);
                        C[m * ldc + (n_pair0 + 0)] = out_h0;
                        if (n_pair0 + 1 < N) {
                            half out_h1 = __high2half(out2);
                            C[m * ldc + (n_pair0 + 1)] = out_h1;
                        }
                    }
                }
            }
        }
    }
    
    inline dim3 compute_grid(int M, int N) {
        return dim3((N + TB_N - 1) / TB_N, (M + TB_M -1) / TB_M, 1);
    } 
    
    inline dim3 compute_block() {
        return dim3(THREADS, 1, 1);
    }
    
    inline size_t shared_mem_bytes() {
        // [A0 half] [A1 half] [Bbytes0 u8] [Bbytes1 u8] [Bhalf half]
        size_t a_bytes = TB_M * TB_K * sizeof(half);            // one A tile
        size_t bb_bytes = TB_N * (TB_K / 2) * sizeof(uint8_t);  // one packed B tile (bytes)
        size_t bhalf_bytes = TB_K * TB_N * sizeof(half);        // one B half tile
        return (2 * a_bytes) + (2 * bb_bytes) + bhalf_bytes;
    }

    template <typename ScaleT, typename Epilogue>
    static cudaError_t launch_impl(
        int M, int N, int K,
        const half* A, int lda,
        const uint8_t* B_packed, int ldb_bytes,
        const ScaleT* scales, int lds_groups,
        int group_size,
        half* C, int ldc,
        Epilogue epilogue,
        cudaStream_t stream
    )
    {
        if (!device_is_sm80_plus()) {
            return cudaErrorNotSupported;
        }
        dim3 grid = compute_grid(M, N);
        dim3 block = compute_block();
        size_t smem = shared_mem_bytes();

        int4_gemm_kernel_fp16tc<ScaleT, Epilogue><<<grid, block, smem, stream>>>(
            M, N, K,
            A, lda,
            B_packed, ldb_bytes,
            scales, lds_groups,
            group_size,
            C, ldc, 
            epilogue
        );

        return cudaGetLastError();
    }

    // public apis

    cudaError_t launch_gemm_int4_bias(
        // sizes
        int M, int N, int K,
        // A [M,K]  row-major
        const half* A, int lda,
        // B_packed [N, ceil(K/2)] column-major by N; stride in bytes between columns
        const uint8_t* B_packed, int ldb_bytes,
        // Scales [N, G], G=ceil(K/group_size)
        const half* scales, int lds_groups,
        int group_size,
        // bias [N] or nullptr
        const half* bias,
        // output [M,N] row-major
        half* C, int ldc,
        // cuda stream
        cudaStream_t stream
    )
    {
        using ScaleT = half;
        using Epilogue = BiasOnlyEpilogue<half, float, half>;
        Epilogue epi(bias);
        return launch_impl<ScaleT, Epilogue>(
            M, N, K,
            A, lda,
            B_packed, ldb_bytes,
            scales, lds_groups,
            group_size,
            C, ldc,
            epi, 
            stream
        );
    }
    
  cudaError_t launch_gemm_int4_bias_silu(
      int M, int N, int K,
      const half* A, int lda,
      const uint8_t* B_packed, int ldb_bytes,
      const half* scales, int lds_groups,
      int group_size,
      const half* bias,
      half* C, int ldc,
      cudaStream_t stream)
  {
    using ScaleT = half;
    using Epilogue = BiasSiLUEpilogue<half, float, half>;
    Epilogue epi(bias);
    return launch_impl<ScaleT, Epilogue>(
        M, N, K,
        A, lda,
        B_packed, ldb_bytes,
        scales, lds_groups,
        group_size,
        C, ldc,
        epi,
        stream);
  }
  
  cudaError_t launch_gemm_int4_bias_residual(
      int M, int N, int K,
      const half* A, int lda,
      const uint8_t* B_packed, int ldb_bytes,
      const half* scales, int lds_groups,
      int group_size,
      const half* bias,
      const half* residual, int ldres,
      half* C, int ldc,
      cudaStream_t stream)
  {
    using ScaleT = half;
    using Epilogue = BiasResidualEpilogue<half, float, half, half>;
    Epilogue epi(bias, residual, ldres);
    return launch_impl<ScaleT, Epilogue>(
        M, N, K,
        A, lda,
        B_packed, ldb_bytes,
        scales, lds_groups,
        group_size,
        C, ldc,
        epi,
        stream);
  }
  
} // namespace qgemm
cmake_minimum_required(VERSION 3.18)
project(qgemm_ops LANGUAGES CXX CUDA)

# Require C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Default CUDA architectures: sm_80 unless overridden by -DCMAKE_CUDA_ARCHITECTURES
if (NOT CMAKE_CUDA_ARCHITECTURES)
  set(CMAKE_CUDA_ARCHITECTURES 80)
endif()

find_package(Torch REQUIRED)

add_library(qgemm_ops SHARED
  cpp/bindings.cpp
  cpp/launch.cpp
  cuda/int4_gemm.cu
)

target_include_directories(qgemm_ops PRIVATE
  ${TORCH_INCLUDE_DIRS}
  ${CMAKE_CURRENT_SOURCE_DIR}/cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/cuda
)

target_compile_options(qgemm_ops PRIVATE
  $<$<COMPILE_LANGUAGE:CUDA>:
    -O3
    -U__CUDA_NO_HALF_OPERATORS__
    -U__CUDA_NO_HALF_CONVERSIONS__
    -U__CUDA_NO_BFLOAT16_CONVERSIONS__
  >
  $<$<COMPILE_LANGUAGE:CXX>:-O3>
)

target_link_libraries(qgemm_ops PRIVATE ${TORCH_LIBRARIES})

set_target_properties(qgemm_ops PROPERTIES
  CUDA_SEPARABLE_COMPILATION ON
  POSITION_INDEPENDENT_CODE ON
)

message(STATUS "Building qgemm_ops for CUDA archs: ${CMAKE_CUDA_ARCHITECTURES}")


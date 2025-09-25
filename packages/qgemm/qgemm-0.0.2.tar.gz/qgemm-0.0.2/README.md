qgemm
=====

Scaffold for INT4 weight quantization utilities and future CUDA/C++ extensions.

- CPU/Python quantization utilities in `python/quantize.py`
- LLaMA converter to INT4 safetensors in `python/convert_llama.py`
- Weight format documented in `docs/weight_format.md`
- Packaging via `pyproject.toml` and wired CUDA extension in `setup.py`

Build the CUDA/C++ extension (Phase 3)
- Prereqs: PyTorch with CUDA, a CUDA toolkit (nvcc), a GPU with sm80+.
- Via pip/setuptools (in-place build):
  - `QGEMM_BUILD_EXT=1 TORCH_CUDA_ARCH_LIST=80 pip install -e .`
  - or set custom arches: `QGEMM_CUDA_ARCHS="80,90" pip install -e .`
- After install, importing `qgemm` will auto-register `torch.ops.qgemm.*`.

Build with CMake
- `cmake -S . -B build -DCMAKE_CUDA_ARCHITECTURES=80`
- `cmake --build build -j`
- Load the produced `libqgemm_ops.so` using `torch.ops.load_library` if using outside the package.

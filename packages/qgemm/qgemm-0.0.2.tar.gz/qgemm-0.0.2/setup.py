from setuptools import setup
import os


def _parse_arch_list(val: str):
    # Accept forms like "80,90" or "8.0,9.0" and return ["80", "90"]
    out = []
    for p in val.replace(";", ",").split(","):
        p = p.strip()
        if not p:
            continue
        if "." in p:
            major = p.split(".")[0]
            out.append(major + "0")
        else:
            out.append(p)
    return out


CMDCLASS = {}


def build_extensions():
    # Build the C++/CUDA extension when requested. Default: build if torch + CUDA toolchain available
    want_build = os.environ.get("QGEMM_BUILD_EXT", None)
    try:
        import torch  # noqa: F401
        from torch.utils.cpp_extension import CUDAExtension, BuildExtension, CUDA_HOME
        torch_available = True
        cuda_home = CUDA_HOME
    except Exception:
        torch_available = False
        cuda_home = None

    if want_build is None:
        # Auto-enable if torch is present; users can export QGEMM_BUILD_EXT=0 to skip
        want_build = "1" if torch_available else "0"

    if str(want_build) != "1":
        return []

    if not torch_available or (cuda_home is None):
        return []

    # Archs: prefer env QGEMM_CUDA_ARCHS (e.g., "80,90"). Fallback to TORCH_CUDA_ARCH_LIST. Default: 80.
    arch_env = os.environ.get("QGEMM_CUDA_ARCHS") or os.environ.get("TORCH_CUDA_ARCH_LIST") or "80"
    arch_list = _parse_arch_list(arch_env)
    nvcc_arch_flags = []
    for a in arch_list:
        nvcc_arch_flags += [f"-gencode=arch=compute_{a},code=sm_{a}"]

    extra_compile_args = {
        "cxx": ["-O3"],
        "nvcc": [
            "-O3",
            "-U__CUDA_NO_HALF_OPERATORS__",
            "-U__CUDA_NO_HALF_CONVERSIONS__",
            "-U__CUDA_NO_BFLOAT16_CONVERSIONS__",
        ] + nvcc_arch_flags,
    }

    ext_modules = [
        CUDAExtension(
            name="qgemm._C",
            sources=[
                "cpp/bindings.cpp",
                "cpp/launch.cpp",
                "cuda/int4_gemm.cu",
            ],
            extra_compile_args=extra_compile_args,
            include_dirs=[
                os.path.abspath("cpp"),
                os.path.abspath("cuda"),
            ],
        )
    ]

    global CMDCLASS
    CMDCLASS = {"build_ext": BuildExtension}

    return ext_modules


setup(
    name="qgemm",
    version="0.0.2",
    description="INT4 quantization tooling and CUDA extension",
    ext_modules=build_extensions(),
    cmdclass=CMDCLASS,
)

# core/cuda_libraries.py
import pathlib

from torchfetch.model.info import CudaLibraryInfo


def find_libs(base: str, patterns: list[str], lib_names: list[str]) -> dict[str, str]:
    base_path = pathlib.Path(base)
    results = {}
    for name in lib_names:
        found = set()
        for pattern in patterns:
            for p in base_path.glob(f"{pattern}/**/lib{name}.so*"):
                if p.is_file():
                    found.add(str(p.resolve()))
        results[name] = ", ".join(found) if found else "Not Found"
    return results


def get_system_cuda_libs() -> CudaLibraryInfo:
    patterns = [
        "usr/lib",
        "usr/lib64",
        "usr/local/cuda*/lib",
        "usr/local/cuda*/lib64",
        "opt/cuda*/lib",
    ]
    libs = find_libs("/", patterns, ["cudart", "cudnn", "nvidia-ml", "cuda"])
    return CudaLibraryInfo(
        runtime=libs["cudart"],
        cudnn=libs["cudnn"],
        nvidia_ml=libs["nvidia-ml"],
        driver=libs["cuda"],
    )


def get_env_cuda_libs(env_type: str, base_path: str) -> CudaLibraryInfo:
    if env_type == "system":
        return get_system_cuda_libs()

    patterns = ["lib", "lib64"]
    libs = find_libs(base_path, patterns, ["cudart", "cudnn"])
    return CudaLibraryInfo(
        runtime=libs["cudart"],
        cudnn=libs["cudnn"],
        nvidia_ml=None,
        driver=None,
    )

# model/info.py
from dataclasses import dataclass


@dataclass(frozen=True)
class SystemInfo:
    python: str
    os: str
    arch: str


@dataclass(frozen=True)
class EnvironmentInfo:
    type: str  # system, venv, conda
    name: str


@dataclass(frozen=True)
class TorchInfo:
    version: str
    cuda_version: str
    cudnn_version: str
    cuda_available: bool


@dataclass(frozen=True)
class CudaLibraryInfo:
    runtime: str
    cudnn: str
    nvidia_ml: str | None = None
    driver: str | None = None


@dataclass(frozen=True)
class GPUDeviceInfo:
    device: int
    name: str
    compute: str
    memory: str
    cuda: str
    driver: str


@dataclass(frozen=True)
class FullSystemReport:
    system: SystemInfo
    environment: EnvironmentInfo
    torch: TorchInfo | None
    cuda_libs_system: CudaLibraryInfo
    cuda_libs_env: CudaLibraryInfo | None
    gpus: list[GPUDeviceInfo] | None

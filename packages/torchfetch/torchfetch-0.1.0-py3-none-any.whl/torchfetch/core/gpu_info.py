# core/gpu_info.py
from typing import Any

from torchfetch.model.info import GPUDeviceInfo


def get_gpu_info(torch_module: Any) -> list[GPUDeviceInfo]:
    if (
        torch_module is None
        or not getattr(torch_module, "cuda", None)
        or not torch_module.cuda.is_available()
    ):
        return []

    gpus = []
    for i in range(torch_module.cuda.device_count()):
        props = torch_module.cuda.get_device_properties(i)
        cc = torch_module.cuda.get_device_capability(i)
        driver_ver = "N/A"
        if hasattr(torch_module.cuda, "get_driver_version"):
            try:
                raw = torch_module.cuda.get_driver_version()
                if isinstance(raw, int):
                    driver_ver = f"{raw // 1000}.{(raw % 1000) // 10:02d}"
                else:
                    driver_ver = str(raw)
            except Exception:
                pass

        gpus.append(
            GPUDeviceInfo(
                device=i,
                name=torch_module.cuda.get_device_name(i),
                compute=f"{cc[0]}.{cc[1]}",
                memory=f"{props.total_memory / (1024**2):.2f} MB",
                cuda=torch_module.version.cuda or "N/A",
                driver=driver_ver,
            )
        )
    return gpus

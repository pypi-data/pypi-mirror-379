# cli.py
import typer

from torchfetch.core.cuda_libraries import get_env_cuda_libs, get_system_cuda_libs
from torchfetch.core.environment import EnvironmentType, detect_current_environment
from torchfetch.core.gpu_info import get_gpu_info
from torchfetch.core.system_info import get_system_info
from torchfetch.core.torch_info import get_torch_info
from torchfetch.display.renderer import InfoRenderer
from torchfetch.model.info import EnvironmentInfo, FullSystemReport


def main():
    # 1. 探测环境
    env_type, base_path, env_name = detect_current_environment()

    # 2. 收集所有信息
    system_info = get_system_info()
    gpus = None
    torch_info = None
    try:
        import torch  # type: ignore

        torch_info = get_torch_info()
        gpus = get_gpu_info(torch if torch_info.version != "N/A" else None)
    except ImportError:
        torch = None

    cuda_libs_system = get_system_cuda_libs()
    cuda_libs_env = (
        get_env_cuda_libs(env_type.value, base_path)
        if env_type != EnvironmentType.SYSTEM
        else None
    )

    # 3. 构建完整报告
    report = FullSystemReport(
        system=system_info,
        environment=EnvironmentInfo(
            type=env_type.value,
            name=f"{'System' if env_type == EnvironmentType.SYSTEM else env_type.value.title()}: {env_name}",
        ),
        torch=torch_info,
        cuda_libs_system=cuda_libs_system,
        cuda_libs_env=cuda_libs_env,
        gpus=gpus,
    )

    # 4. 渲染输出
    renderer = InfoRenderer(report)
    renderer.render()


if __name__ == "__main__":
    typer.run(main)

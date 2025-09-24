# display/renderer.py
from rich.columns import Columns
from rich.console import Console
from rich.table import Table
from rich.text import Text

from torchfetch.model.info import FullSystemReport

TORCH_ART = r"""
         ./^
       ./@@^
     ./@@@/. ./@\
   ./@@@/    .@@/.
  /@@@/.         ./@^
.@@@/            ,@@@\
/@@^              .@@@^
@@@.               =@@@
@@@.               =@@@
\@@^               /@@^
.@@@\            ./@@/.
 .\@@@\.       ,/@@@/
   ,\@@@@@@@@@@@@@/.
      .[\@@@@@/[.
"""


class InfoRenderer:
    def __init__(self, report: FullSystemReport):
        self.report = report

    def render(self):
        left = Text(TORCH_ART, style="bold red")
        right = self._create_info_table()
        cols = Columns([left, right], column_first=True, padding=(2, 4))
        Console().print(cols)

    def _create_info_table(self):
        table = Table.grid(padding=(0, 1))
        table.add_column(style="white")

        env = self.report.environment
        env_icon = (
            "🌐" if env.type == "system" else "🐍" if env.type == "venv" else "📦"
        )
        table.add_row(Text(f"{env_icon} Environment: {env.name}", style="bold cyan"))

        if self.report.torch is not None:
            table.add_row(
                Text(f"🧠 PyTorch: {self.report.torch.version}", style="bold magenta")
            )

            cuda_status = (
                "Available" if self.report.torch.cuda_available else "Not Available"
            )
            table.add_row(
                Text(
                    f"🔥 CUDA: {self.report.torch.cuda_version} ({cuda_status})",
                    style="bold yellow",
                )
            )
            table.add_row(
                Text(f"🧪 CuDNN: {self.report.torch.cudnn_version}", style="bold green")
            )

        # CUDA Libraries (System)
        table.add_row(Text("📁 CUDA Libraries (System):", style="bold white"))
        sys_libs = self.report.cuda_libs_system
        table.add_row(Text(f"  • CUDA Runtime: {sys_libs.runtime}", style="dim"))
        table.add_row(Text(f"  • cuDNN: {sys_libs.cudnn}", style="dim"))
        if sys_libs.nvidia_ml:
            table.add_row(Text(f"  • NVML: {sys_libs.nvidia_ml}", style="dim"))
        if sys_libs.driver:
            table.add_row(Text(f"  • Driver: {sys_libs.driver}", style="dim"))

        # Env Libraries
        if self.report.cuda_libs_env:
            env_libs = self.report.cuda_libs_env
            env_name = self.report.environment.type
            table.add_row(Text(f"📁 CUDA Libraries ({env_name}):", style="bold white"))
            table.add_row(Text(f"  • CUDA Runtime: {env_libs.runtime}", style="dim"))
            table.add_row(Text(f"  • cuDNN: {env_libs.cudnn}", style="dim"))

        # GPUs
        if self.report.gpus:
            table.add_row(Text("🖥️  GPU(s):", style="bold blue"))
            for gpu in self.report.gpus:
                table.add_row(
                    Text(f"  • Device {gpu.device}: {gpu.name}", style="bold cyan")
                )
                table.add_row(
                    Text(
                        f"    Compute: {gpu.compute} | Memory: {gpu.memory}",
                        style="dim",
                    )
                )
                table.add_row(
                    Text(f"    CUDA: {gpu.cuda} | Driver: {gpu.driver}", style="dim")
                )

        # System
        sys = self.report.system
        table.add_row(Text("💻 System:", style="bold white"))
        table.add_row(Text(f"  • Python: {sys.python}", style="bold yellow"))
        table.add_row(Text(f"  • OS: {sys.os}", style="bold green"))
        table.add_row(Text(f"  • Arch: {sys.arch}", style="bold cyan"))

        return table

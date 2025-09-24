# torchfetch

[English | 中文说明见下方]

A modern, neofetch-style CLI tool to display detailed information about your PyTorch, CUDA, cuDNN, Python, and NVIDIA driver environment. Beautifully formatted with `rich`, supports both system and Python package checks, and is especially useful for debugging deep learning environments.

## Features

- Neofetch-inspired, colorful CLI output with ASCII logo
- Detects PyTorch, CUDA, cuDNN, Python versions and their compatibility
- Checks if PyTorch is built with CUDA, and if `pytorch-cuda` is available
- Lists system and Python package CUDA/cuDNN `.so` files
- Detects NVIDIA driver (`libcuda.so`, `libnvidia-ml.so`)
- Shows GPU details (name, memory, compute capability)
- Detects and displays virtual environment (venv/conda) info
- Bilingual output (English/Chinese) planned for future

## Quick Start

```bash
pip install torchfetch  # (if available on PyPI)
# or clone and run
python -m torchfetch
```

## Example Output

![screenshot](./screenshot.png)

## Usage

```bash
python -m torchfetch [--venv /path/to/venv]
```

- `--venv`: Manually specify a virtual/conda environment path (overrides autodetect)

## Requirements

- Python 3.8+
- [rich](https://github.com/Textualize/rich)
- torch (optional, for full features)

## Project Structure

- `main.py` : CLI entry
- `src/torchfetch/` : Core logic, display, utils
- `tests/` : Test cases

## License

MIT

---

# torchfetch

一个现代化、neofetch 风格的命令行工具，优雅展示你的 PyTorch、CUDA、cuDNN、Python 及 NVIDIA 驱动环境信息。基于 `rich` 美化输出，支持系统与 Python 包多重检测，深度学习环境调试利器。

## 功能特性

- neofetch 风格彩色 CLI 输出，带 ASCII logo
- 检测 PyTorch、CUDA、cuDNN、Python 版本及兼容性
- 检查 PyTorch 是否自带 CUDA，`pytorch-cuda` 是否可用
- 列出系统和 Python 包内 CUDA/cuDNN `.so` 文件
- 检测 NVIDIA 驱动（`libcuda.so`, `libnvidia-ml.so`）
- 展示 GPU 详情（型号、显存、算力）
- 检测并展示虚拟环境（venv/conda）信息
- 未来计划支持中英文双语输出

## 快速开始

```bash
pip install torchfetch  # （如已上传 PyPI）
# 或源码运行
python -m torchfetch
```

## 示例输出

![screenshot](./screenshot.png)

## 用法

```bash
python -m torchfetch [--venv /path/to/venv]
```

- `--venv`：手动指定虚拟/conda 环境路径（优先生效）

## 依赖要求

- Python 3.8+
- [rich](https://github.com/Textualize/rich)
- torch（可选，启用全部功能）

## 项目结构

- `main.py` ：命令行入口
- `src/torchfetch/` ：核心逻辑、显示、美化、工具
- `tests/` ：测试用例

## 许可证

MIT

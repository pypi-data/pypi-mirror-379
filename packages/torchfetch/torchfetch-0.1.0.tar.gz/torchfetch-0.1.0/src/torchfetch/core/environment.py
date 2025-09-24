# core/environment.py
import os
import pathlib
from enum import Enum


class EnvironmentType(Enum):
    SYSTEM = "system"
    VENV = "venv"
    CONDA = "conda"


def detect_current_environment() -> tuple[EnvironmentType, str, str]:
    """返回 (类型, 基路径, 名称)"""
    if "CONDA_PREFIX" in os.environ:
        path = os.environ["CONDA_PREFIX"]
        return EnvironmentType.CONDA, path, pathlib.Path(path).name
    elif "VIRTUAL_ENV" in os.environ:
        path = os.environ["VIRTUAL_ENV"]
        return EnvironmentType.VENV, path, pathlib.Path(path).name
    else:
        return EnvironmentType.SYSTEM, "/", "system"

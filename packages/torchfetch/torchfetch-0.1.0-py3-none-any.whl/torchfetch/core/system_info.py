# core/system_info.py
import os
import sys

from torchfetch.model.info import SystemInfo


def get_system_info() -> SystemInfo:
    return SystemInfo(
        python=f"{sys.version.split()[0]} ({sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})",
        os=f"{os.name} ({os.uname().sysname} {os.uname().release})",
        arch=os.uname().machine,
    )

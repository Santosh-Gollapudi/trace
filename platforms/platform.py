import platform
from platforms.windows.network import WindowsNetwork
from platforms.linux.network import LinuxNetwork
from platforms.windows.system import WindowsSystem
from platforms.windows.filesystem import WindowsFileSystem
from platforms.linux.system import LinuxSystem
from platforms.linux.filesystem import LinuxFileSystem


def get_system():
    system = platform.system()

    if system == "Windows":
        return WindowsSystem()

    if system == "Linux":
        return LinuxSystem()

    raise RuntimeError(f"Unsupported platform: {system}")

def get_filesystem():
    system = platform.system()

    if system == "Windows":
        return WindowsFileSystem()

    if system == "Linux":
        return LinuxFileSystem()

    raise RuntimeError(f"Unsupported platform: {system}")

def get_network():
    system = platform.system()

    if system == "Windows":
        return WindowsNetwork()

    if system == "Linux":
        return LinuxNetwork()

    raise RuntimeError(f"Unsupported platform: {system}")
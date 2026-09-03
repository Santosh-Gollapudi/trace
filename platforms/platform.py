import platform

from platforms.windows.system import WindowsSystem
from platforms.windows.filesystem import WindowsFileSystem
from platforms.windows.network import WindowsNetwork
from platforms.windows.process import WindowsProcess
from platforms.windows.power import WindowsPower
from platforms.windows.package import WindowsPackage
from platforms.linux.system import LinuxSystem
from platforms.linux.filesystem import LinuxFileSystem
from platforms.linux.network import LinuxNetwork
from platforms.linux.process import LinuxProcess
from platforms.linux.power import LinuxPower
from platforms.linux.package import LinuxPackage


PLATFORM_ADAPTERS = {
    "Windows": {
        "system": WindowsSystem,
        "filesystem": WindowsFileSystem,
        "network": WindowsNetwork,
        "process": WindowsProcess,
        "power": WindowsPower,
        "package": WindowsPackage,
    },
    "Linux": {
        "system": LinuxSystem,
        "filesystem": LinuxFileSystem,
        "network": LinuxNetwork,
        "process": LinuxProcess,
        "power": LinuxPower,
        "package": LinuxPackage,
    },
}


def get_platform():
    system = platform.system()

    if system not in PLATFORM_ADAPTERS:
        raise RuntimeError(f"Unsupported platform: {system}")

    return PLATFORM_ADAPTERS[system]


def _get_adapter(component):
    adapters = get_platform()

    try:
        adapter = adapters[component]
    except KeyError:
        raise RuntimeError(
            f"Unsupported platform component: {component}"
        )

    return adapter()


def get_system():
    return _get_adapter("system")


def get_filesystem():
    return _get_adapter("filesystem")


def get_network():
    return _get_adapter("network")


def get_process():
    return _get_adapter("process")


def get_power():
    return _get_adapter("power")


def get_package():
    return _get_adapter("package")
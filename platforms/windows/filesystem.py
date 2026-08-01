from pathlib import Path
from interfaces.filesystem import FileSystemInterface


class WindowsFileSystem(FileSystemInterface):

    def list_directory(self, path):
        return list(Path(path).iterdir())

    def exists(self, path):
        return Path(path).exists()
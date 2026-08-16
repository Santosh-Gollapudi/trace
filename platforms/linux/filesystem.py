from pathlib import Path
from interfaces.filesystem import FileSystemInterface


class LinuxFileSystem(FileSystemInterface):

    def list_directory(self, path):
        return list(Path(path).iterdir())

    def exists(self, path):
        return Path(path).exists()

    def mkdir(self, path):
        Path(path).mkdir(exist_ok=True)

    def touch(self, path):
        Path(path).touch(exist_ok=True)

    def read(self, path):
        file = Path(path)

        if not file.exists():
            return None

        return file.read_text(encoding="utf-8")

    def write(self, path, text):
        Path(path).write_text(text, encoding="utf-8")

    def append(self, path, text):
        with open(path, "a", encoding="utf-8") as f:
            f.write(text + "\n")
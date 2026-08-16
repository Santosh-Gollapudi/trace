from pathlib import Path
from interfaces.system import SystemInterface


class LinuxSystem(SystemInterface):

    def __init__(self):
        self.current_directory = Path.cwd()

    def pwd(self):
        return self.current_directory

    def ls(self):
        return list(self.current_directory.iterdir())

    def exists(self, name):
        return (self.current_directory / name).exists()

    def cd(self, path):
        new_path = (self.current_directory / path).resolve()

        if new_path.exists() and new_path.is_dir():
            self.current_directory = new_path
            return True

        return False

    def mkdir(self, name):
        path = self.current_directory / name
        path.mkdir(exist_ok=True)

    def touch(self, name):
        path = self.current_directory / name
        path.touch(exist_ok=True)

    def cat(self, name):
        path = self.current_directory / name

        if not path.exists():
            return None

        return path.read_text(encoding="utf-8")

    def write(self, filename, text):
        file = self.current_directory / filename
        file.write_text(text, encoding="utf-8")

    def append(self, filename, text):
        file = self.current_directory / filename

        with open(file, "a", encoding="utf-8") as f:
            f.write(text + "\n")
from core.jarvis_core import JarvisCore
from shell.shell import Shell


def main():
    core = JarvisCore()
    core.start()

    shell = Shell(core)
    shell.run()


if __name__ == "__main__":
    main()
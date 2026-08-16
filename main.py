from core.trace_core import TraceCore
from shell.shell import Shell


def main():
    core = TraceCore()
    core.start()

    shell = Shell(core)
    shell.run()


if __name__ == "__main__":
    main()
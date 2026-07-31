from dataclasses import dataclass


@dataclass
class Command:
    name: str
    args: list[str]


def parse(text: str) -> Command:
    parts = text.strip().split()

    if not parts:
        return Command("", [])

    return Command(
        name=parts[0].lower(),
        args=parts[1:]
    )
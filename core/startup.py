"""
JARVIS AI Assistant
-------------------
Startup screen.
"""

from rich.console import Console

console = Console()


class StartupScreen:
    """Displays startup information."""

    def show_banner(self):
        console.rule("[bold cyan]JARVIS AI[/bold cyan]")

    def status(self, component: str):
        console.print(f"[green]✓[/green] {component}")

    def info(self, key: str, value: str):
        console.print(f"[cyan]{key:<8}[/cyan]: {value}")
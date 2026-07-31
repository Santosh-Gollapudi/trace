"""
JARVIS AI Assistant
-------------------
Event bus.
"""


class EventBus:
    """Simple publish/subscribe event system."""

    def publish(self, event: str):
        print(f"[EVENT] {event}")
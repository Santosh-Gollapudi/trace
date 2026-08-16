"""
TRACE AI Assistant
-------------------
Logging configuration.
"""

from loguru import logger
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logger.add(
    "logs/trace.log",
    rotation="5 MB",
    retention="10 days",
    level="INFO",
)

__all__ = ["logger"]
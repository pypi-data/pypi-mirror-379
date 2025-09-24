"""Simple logging utilities for Turnwise."""

import logging
import sys


def get_logger(name: str) -> logging.Logger:
    """Get a logger for a specific module.

    Args:
        name: Logger name (usually __name__)

    Returns:
        Logger instance
    """
    return logging.getLogger(f"turnwise.{name}")


def setup_logging(level: str = "INFO") -> None:
    """Set up basic logging for Turnwise.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

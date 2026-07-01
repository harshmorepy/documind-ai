"""
Application Logging Configuration

This module configures the application's logger.

Every module in DocuMind AI should import the logger
from this file instead of creating its own.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("documind_ai")
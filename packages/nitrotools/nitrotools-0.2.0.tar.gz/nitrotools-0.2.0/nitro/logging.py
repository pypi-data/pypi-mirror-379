"""Simple logging utilities for nitrotools."""

import logging
import os
from typing import Optional

def get_logger(name: str, level: Optional[str] = None) -> logging.Logger:
    """Get a configured logger.
    
    Args:
        name: Logger name (usually __name__).
        level: Optional log level (DEBUG, INFO, etc.). Defaults to INFO or from LOG_LEVEL env var.
    
    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger(name)
    
    if logger.handlers:
        return logger  # Already configured
    
    # Set level
    log_level = level or os.getenv("LOG_LEVEL", "INFO").upper()
    logger.setLevel(getattr(logging, log_level, logging.INFO))
    
    # Handler
    handler = logging.StreamHandler()
    handler.setLevel(logger.level)
    
    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

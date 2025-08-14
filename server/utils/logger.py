"""
File: utils/logger.py
Creation Time: Aug 13th 2025, 11:39 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2025 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
"""

import logging
from typing import Optional
import json
import sys


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Returns a configured logger instance.
    If name is None, returns the root logger.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)
        # Color codes for log levels
        COLOR_MAP = {
            "DEBUG": "\033[36m",  # Cyan
            "INFO": "\033[32m",  # Green
            "WARNING": "\033[33m",  # Yellow
            "ERROR": "\033[31m",  # Red
            "CRITICAL": "\033[41m",  # Red background
        }
        RESET = "\033[0m"

        class ColorFormatter(logging.Formatter):
            def format(self, record):
                levelname = record.levelname
                color = COLOR_MAP.get(levelname, "")
                record.levelname = f"{color}{levelname}{RESET}"
                return super().format(record)

        formatter = ColorFormatter(
            "[%(asctime)s] %(levelname)s %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


# Helper for pretty-printing dict/JSON results in logs
def pretty_log(logger, msg, data=None, level="info"):
    if data is not None:
        if isinstance(data, (dict, list)):
            msg = f"{msg}\n{json.dumps(data, indent=2, ensure_ascii=False)}"
        else:
            msg = f"{msg}: {data}"
    getattr(logger, level)(msg)

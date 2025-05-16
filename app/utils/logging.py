"""
Logging configuration for the application.
"""

import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get log level from environment or use default
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

# Ensure logs directory exists
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Configure logging
def setup_logging(logger_name=None):
    """Configure logging for the application."""
    logger = logging.getLogger(logger_name)
    logger.setLevel(LOG_LEVEL)
    
    # Create formatters
    simple_formatter = logging.Formatter('%(levelname)s - %(message)s')
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    # Create file handler
    file_handler = RotatingFileHandler(
        logs_dir / "aihackathon.log",
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG if DEBUG else logging.INFO)
    file_handler.setFormatter(detailed_formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Create application logger
logger = setup_logging("aihackathon")

# Example usage:
# from app.utils.logging import logger
# logger.info("Application started")
# logger.error("An error occurred", exc_info=True)

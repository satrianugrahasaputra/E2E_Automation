import os
import sys
from loguru import logger

# Ensure reports directory exists
os.makedirs("reports", exist_ok=True)

# Configure Loguru
logger.remove()  # Remove default handler

# Log to console with nice formatting
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
)

# Log to file for history/archiving
logger.add(
    "reports/test_run.log",
    rotation="10 MB",
    retention="5 days",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
)

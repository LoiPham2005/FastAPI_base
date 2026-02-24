import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

from app.config import settings

# Define log directory
LOG_DIR = Path(settings.LOG_FILES_DIR)
LOG_DIR.mkdir(exist_ok=True)

# Define formats
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def setup_logging():
    # Root logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))

    # Formatter
    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Info File Handler
    info_file_handler = RotatingFileHandler(
        LOG_DIR / "info.log", maxBytes=10*1024*1024, backupCount=5, encoding="utf-8"
    )
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(formatter)
    logger.addHandler(info_file_handler)

    # Error File Handler
    error_file_handler = RotatingFileHandler(
        LOG_DIR / "error.log", maxBytes=10*1024*1024, backupCount=5, encoding="utf-8"
    )
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    logger.addHandler(error_file_handler)

    # Intercept Uvicorn logs
    for logger_name in ("uvicorn", "uvicorn.access", "uvicorn.error"):
        log = logging.getLogger(logger_name)
        log.handlers = logger.handlers
        log.propagate = False

    logging.info("Logging system initialized.")

# Create a logger for the app
logger = logging.getLogger("app")

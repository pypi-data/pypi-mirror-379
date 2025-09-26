import logging
import os
from datetime import datetime
from pathlib import Path

def setup_logging():
    """Set up logging configuration for the application."""
    # Create logs directory if it doesn't exist - use Path for cross-platform compatibility
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)
    
    # Create log filename with timestamp
    log_filename = f"mx2_manager_{datetime.now().strftime('%Y%m%d')}.log"
    log_filepath = log_dir / log_filename
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler()  # Also log to console
        ]
    )
    
    return logging.getLogger(__name__)

def log_error(message, exception=None):
    """Log error messages with optional exception details."""
    logger = logging.getLogger(__name__)
    if exception:
        logger.error(f"{message}: {str(exception)}", exc_info=True)
    else:
        logger.error(message)

def log_info(message):
    """Log info messages."""
    logger = logging.getLogger(__name__)
    logger.info(message)

def log_warning(message):
    """Log warning messages."""
    logger = logging.getLogger(__name__)
    logger.warning(message)
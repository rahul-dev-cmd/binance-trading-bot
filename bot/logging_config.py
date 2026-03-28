"""
Configuration module for the unified logging system.

Sets up a logger to output to both the console (standard output) and
to a rotating log file. Both outputs use a rigorous format including
timestamps and log levels.
"""

import logging
import sys


def setup_logger() -> logging.Logger:
    """
    Initialize and configure the 'binance_cli' logger.
    
    The logger writes DEBUG level logs and above to 'binance_cli.log'.
    It writes INFO level logs and above to the console. Both formats
    include the timestamp, log level, logger name, and message.
    
    Returns:
        logging.Logger: The configured logger instance.
    """
    logger = logging.getLogger("binance_cli")
    logger.setLevel(logging.DEBUG)

    # Formatter with timestamp and log levels
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    # File handler for local logging
    log_file = "binance_cli.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Console handler for terminal
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Avoid adding handlers multiple times if instantiated elsewhere
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Globally accessible logger instance
logger = setup_logger()

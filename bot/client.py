"""
Client initialization module for Binance API.

Fetches necessary authorization details from environment variables
and establishes an authenticated Client session to the Binance Futures Testnet.
"""

import os
from dotenv import load_dotenv 
from binance.client import Client
from .logging_config import logger

load_dotenv()


def get_client() -> Client:
    """
    Initialize and return a Binance Client configured for the Testnet.
    
    Requires BINANCE_API_KEY and BINANCE_API_SECRET to be present as 
    environment variables in the system.
    
    Returns:
        Client: An authenticated `python-binance` Client connected to the testnet.
        
    Raises:
        EnvironmentError: If required API keys are not found in the environment.
    """
    api_key = os.environ.get("BINANCE_API_KEY")
    api_secret = os.environ.get("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        logger.error("Missing BINANCE_API_KEY or BINANCE_API_SECRET environment variables")
        raise EnvironmentError(
            "Please set the BINANCE_API_KEY and BINANCE_API_SECRET environment variables."
        )

    # Initialize client for Testnet futures
    client = Client(api_key, api_secret, testnet=True)
    logger.debug("Binance client successfully authenticated and initialized for testnet.")
    
    return client

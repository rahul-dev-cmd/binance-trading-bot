"""
Input validation module for Binance orders.

Provides logic to ensure command-line arguments adhere to the strict requirements
of the Binance Testnet Futures API before the requests are sent.
"""

from typing import Tuple, Optional
from .logging_config import logger


def validate_order_params(
    symbol: str, 
    side: str, 
    order_type: str, 
    quantity: float, 
    price: Optional[float] = None
) -> Tuple[str, str, str, float, Optional[float]]:
    """
    Validates formatting and values for order inputs.
    
    Args:
        symbol (str): The trading pair symbol (must be alphanumeric and end with USDT).
        side (str): The order side ('BUY' or 'SELL').
        order_type (str): The order type ('MARKET' or 'LIMIT').
        quantity (float): The amount to order (must be positive).
        price (float, optional): The price per unit. Required if order_type is 'LIMIT'.
    
    Returns:
        tuple: Cleaned, uppercased variables (symbol, side, order_type, quantity, price).
        
    Raises:
        ValueError: If any parameter does not meet the specified criteria.
    """
    # Validate Symbol format
    if not symbol.endswith("USDT") or not symbol.isalnum():
        logger.error(f"Validation failed: Invalid symbol format '{symbol}'.")
        raise ValueError(f"Invalid symbol: {symbol}. Expected a valid USDT pair, e.g., BTCUSDT.")

    # Validate Side
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        logger.error(f"Validation failed: Invalid side '{side}'.")
        raise ValueError("Side must be either 'BUY' or 'SELL'.")

    # Validate Order Type
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        logger.error(f"Validation failed: Invalid order type '{order_type}'.")
        raise ValueError("Type must be either 'MARKET' or 'LIMIT'.")

    # Validate Quantity
    if quantity <= 0:
        logger.error(f"Validation failed: Invalid quantity '{quantity}'.")
        raise ValueError("Quantity must be a positive float.")

    # Validate Price based on Order Type
    if order_type == "LIMIT":
        if price is None or price <= 0:
            logger.error(f"Validation failed: Invalid price '{price}' for LIMIT order.")
            raise ValueError("Price is required and must be a positive float for a LIMIT order.")

    return symbol, side, order_type, quantity, price

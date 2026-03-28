"""
Order execution module for Binance API.

Handles communication with the `python-binance` library to execute
LIMIT or MARKET orders on the Futures testnet. Traps expected network
or API exceptions and safely propagates them to the logger.
"""

from typing import Dict, Any, Optional
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from .logging_config import logger


def place_order(
    client: Client, 
    symbol: str, 
    side: str, 
    order_type: str, 
    quantity: float, 
    price: Optional[float] = None
) -> Dict[str, Any]:
    """
    Place a futures order on Binance with the given specifications.
    
    Args:
        client (Client): The authenticated Binance Testnet Client.
        symbol (str): The trading pair symbol.
        side (str): The order side ('BUY' or 'SELL').
        order_type (str): The order type ('MARKET' or 'LIMIT').
        quantity (float): The amount to order.
        price (float, optional): The price per unit. Used only if order_type is 'LIMIT'.
    
    Returns:
        dict: A simplified summary dictionary containing:
            - orderId: ID of the placed order.
            - status: Execution status of the order.
            - executedQty: Total executed quantity.
            - avgPrice: Average fill price.
            
    Raises:
        Exception: Wrapped wrapper for API or Network errors encountered during transmission.
    """
    try:
        logger.info(f"Preparing to place {side} {order_type} order for {quantity} {symbol}...")
        
        # Base parameters required for all order types
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity,
        }

        # Parameters required exclusively for LIMIT orders
        if order_type == "LIMIT":
            params['timeInForce'] = 'GTC'
            params['price'] = price

        logger.debug(f"API Request params for futures_create_order: {params}")
        
        # Execute the trade specifically on the Futures USDT-M Testnet
        response = client.futures_create_order(**params)
        
        logger.info(f"Order {response.get('orderId')} successfully placed on Binance Testnet.")
        logger.debug(f"API Full Response: {response}")
        
        return {
            'orderId': response.get('orderId'),
            'status': response.get('status'),
            'executedQty': response.get('executedQty'),
            'avgPrice': response.get('avgPrice', 0.0)
        }

    except BinanceAPIException as e:
        logger.error(f"Binance API Exception: {e.status_code} - {e.message}")
        raise Exception(f"Binance API Error: {e.message}")
    except BinanceRequestException as e:
        logger.error(f"Binance Request Exception (Network issue): {e}")
        raise Exception("Failed to connect to Binance API. Check your network connection.")
    except Exception as e:
        logger.exception(f"Unexpected error while placing the order: {str(e)}")
        raise

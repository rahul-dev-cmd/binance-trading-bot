"""
CLI application entry point for the Binance Futures Testnet CLI Order Tool.

This script parses command-line arguments to place orders on the Binance Futures Testnet.
It supports MARKET and LIMIT orders for BUY and SELL sides, passing the arguments
to the validation and order execution logic.
"""

import argparse
import sys

from bot.logging_config import logger
from bot.validators import validate_order_params
from bot.client import get_client
from bot.orders import place_order


def main() -> None:
    """
    Main entry point for placing an order via CLI.
    
    Parses arguments, validates them, initializes the Binance client,
    and places the specified order. Prints a summary upon completion.
    """
    parser = argparse.ArgumentParser(description="Binance Futures Testnet CLI Order Tool")
    parser.add_argument(
        "--symbol", required=True, help="Trading pair symbol (e.g., BTCUSDT)"
    )
    parser.add_argument(
        "--side", required=True, choices=["BUY", "SELL", "buy", "sell"], help="Order side (BUY/SELL)"
    )
    parser.add_argument(
        "--type", required=True, choices=["MARKET", "LIMIT", "market", "limit"], dest="order_type", help="Order type (MARKET/LIMIT)"
    )
    parser.add_argument(
        "--quantity", required=True, type=float, help="Order quantity"
    )
    parser.add_argument(
        "--price", type=float, help="Order price (required for LIMIT orders)"
    )

    args = parser.parse_args()

    try:
        # Validate inputs
        symbol, side, order_type, quantity, price = validate_order_params(
            args.symbol, args.side, args.order_type, args.quantity, args.price
        )

        # Get the initialized Binance client
        client = get_client()

        # Place the order
        result = place_order(client, symbol, side, order_type, quantity, price)

        # Print Output Summary
        print("\n--- Order Summary ---")
        print(f"OrderId:     {result['orderId']}")
        print(f"Status:      {result['status']}")
        print(f"ExecutedQty: {result['executedQty']}")
        print(f"AvgPrice:    {result['avgPrice']}")
        print("---------------------\n")

    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
        print(f"\n[Validation Error] {ve}\n", file=sys.stderr)
        sys.exit(1)
    except EnvironmentError as ee:
        logger.critical(f"Configuration Error: {ee}")
        print(f"\n[Configuration Error] {ee}\n", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        print(f"\n[Error] {e}\n", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

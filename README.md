# Binance Futures CLI Order Tool

A Python CLI application for placing orders on the Binance Futures Testnet (USDT-M) using `python-binance`.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Binance Testnet API keys as environment variables:
   - `BINANCE_API_KEY`
   - `BINANCE_API_SECRET`

## Usage

```bash
# Place a LIMIT order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000.0

# Place a MARKET order
python cli.py --symbol ETHUSDT --side SELL --type MARKET --quantity 0.1
```

## Features
- Validates all user inputs.
- Places `MARKET` and `LIMIT` orders on the Testnet.
- Prints order summary including orderId, status, executedQty, avgPrice.
- Logs requests, responses, and errors to `binance_cli.log`.

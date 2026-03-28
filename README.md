
# Binance Futures Testnet CLI Trading Bot

A lightweight Python CLI application to place **MARKET** and **LIMIT** orders on the **Binance Futures USDT-M Testnet**. Built with clean, modular architecture, structured logging, and robust error handling.

---

## Project Structure

```
Binance/
  bot/
    __init__.py          # Package initializer
    client.py            # Binance API client setup
    orders.py            # Order placement logic
    validators.py        # Input validation
    logging_config.py    # Logging configuration
  cli.py                 # CLI entry point
  requirements.txt       # Python dependencies
  README.md              # This file
  binance_cli.log        # Auto-generated log file
  .env                   # API keys (never commit this)
```

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rahul-dev-cmd/binance-trading-bot.git
cd binance-trading-bot
```

### 2. Create and Activate a Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get Testnet API Keys

1. Go to [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
2. Register and log in
3. Navigate to **API Management**
4. Generate your **API Key** and **Secret Key**

### 5. Create a `.env` File

In the root project folder, create a file named `.env`:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
```

> ⚠️ No quotes. No spaces around `=`. Never commit this file to GitHub.

---

## How to Run

### Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003
```

### Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.003 --price 60000
```

### Place a SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.003
```

---

## CLI Arguments

| Argument     | Required | Description                              |
|--------------|----------|------------------------------------------|
| `--symbol`   | ✅ Yes   | Trading pair e.g. `BTCUSDT`, `ETHUSDT`  |
| `--side`     | ✅ Yes   | `BUY` or `SELL`                          |
| `--type`     | ✅ Yes   | `MARKET` or `LIMIT`                      |
| `--quantity` | ✅ Yes   | Amount to trade (must be positive)       |
| `--price`    | ⚠️ LIMIT only | Required only for LIMIT orders      |

---

## Sample Output

```
2026-03-28 11:53:21 - INFO - Preparing to place BUY MARKET order for 0.003 BTCUSDT...
2026-03-28 11:53:22 - INFO - Order 13001411824 successfully placed on Binance Testnet.

--- Order Summary ---
OrderId:     13001411824
Status:      NEW
ExecutedQty: 0.000
AvgPrice:    0.00
---------------------
```

---

## Logging

All activity is logged to `binance_cli.log` automatically:

- **INFO** level → printed to terminal and log file
- **DEBUG** level → written to log file only (full API request/response)
- **ERROR** level → captured and logged with full context

---

## Error Handling

The bot gracefully handles:

| Error Type | Example | Behavior |
|---|---|---|
| Invalid symbol | `BTCEUR` | Validation error before API call |
| Invalid side | `--side BULLISH` | Validation error with clear message |
| Missing price | `LIMIT` without `--price` | Validation error |
| API error | Wrong API key | Logged and shown to user |
| Network error | No internet | Caught and shown to user |

---

## Assumptions

- Only supports **Binance Futures USDT-M Testnet** (not real Binance)
- Minimum order value is **100 USDT** (Binance testnet restriction)
- For LIMIT orders, price must be **below current testnet market price**
- API keys must be from `testnet.binancefuture.com`, not real Binance

---

## Requirements

```
python-binance>=1.0.19
python-dotenv
requests
```

---

## Author

**Rahul** — [GitHub](https://github.com/rahul-dev-cmd) · [LinkedIn](https://linkedin.com/in/rahul-s-dev)

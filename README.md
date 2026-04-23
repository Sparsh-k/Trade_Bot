# Binance Futures Trading Bot
## Overview

This project is a simplified Python-based trading bot that places orders on the Binance Futures Testnet (USDT-M).
It is built with a clean, modular structure and includes proper logging, validation, and CLI-based interaction.

## Features
1. Place MARKET and LIMIT orders
2. Supports both BUY and SELL sides
3. Command Line Interface (CLI) for user input
4. Input validation with clear error messages
5. Structured logging of requests, responses, and errors
6. Clean and modular code structure

## Setup Instructions
1. Clone the repository
git clone https://github.com/Sparsh-k/Trade_Bot.git
cd Trade_Bot
2. Create virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Setup environment variables

Create a .env file in the root directory:

API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key

## Usage
1. MARKET Order

python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
2. LIMIT Order

python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 30000

## Example Output
Order Response:
{
  "orderId": 13064222840,
  "symbol": "BTCUSDT",
  "status": "NEW",
  "type": "MARKET",
  "side": "BUY",
  "executedQty": "0.0010"
}

## Logging

All API requests, responses, and errors are logged to a file:

bot.log
Example log:
2026-04-23 INFO REQUEST → BTCUSDT BUY MARKET qty=0.001
2026-04-23 INFO RESPONSE → {...}
2026-04-23 ERROR → Invalid input

## Validation
Ensures valid BUY/SELL input
Ensures correct order type
Requires price for LIMIT orders
Prevents invalid quantity values

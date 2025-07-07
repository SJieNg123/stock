# US stock backtest prototype

This is a Python-based stock trading prototype that fetches stock data, calculates technical indicators, generates buy/sell signals, simulates trades, and visualizes results.

---

## Features
- Fetch stock data using Yahoo Finance.
- Calculate RSI and MACD indicators.
- Generate buy/sell signals based on thresholds.
- Simulate trades with a simple strategy.
- Plot RSI, MACD, equity curve, and price with signals.

---

## How to Use

### 1. Install Dependencies
Make sure you have Python installed. Then, install the required libraries:
```bash
pip install yfinance pandas ta matplotlib
```

### 2. Run the Bot
Run the main script:
```bash
python main.py
```

### 3. Provide Inputs
The bot will ask for:
- Stock symbol (e.g., `AAPL`, `TSLA`).
- Time period (e.g., `1mo`, `1y`).
- RSI buy and sell thresholds (default: `30` and `70`).
- Starting cash (default: `$10,000`).

---

## Project Files
- **`main.py`**: Coordinates the workflow.
- **`user_inputs.py`**: Handles user input.
- **`data_handler.py`**: Fetches stock data and calculates indicators.
- **`signal_logics.py`**: Generates buy/sell signals.
- **`simulation.py`**: Simulates trades.
- **`plot_utils.py`**: Creates plots.

---

## Requirements
- Python 3.7+
- Libraries: `yfinance`, `pandas`, `ta`, `matplotlib`

---

## Future Plans
- Add more indicators.
- Support multi-strategy backtesting.
- Build a web interface.

---

## Contact
Feel free to reach out for questions or suggestions!

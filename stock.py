# pip install yfinance pandas ta matplotlib

import yfinance as yf
import ta
import matplotlib.pyplot as plt

# User-defined stock ticker
stock_symbol = input("Enter stock ticker (e.g., NVDA, TSLA, AAPL): ").upper()

data = yf.download(stock_symbol, period="1y", interval="1d")
print(data.tail())

# Add indicators
data["RSI"] = ta.momentum.RSIIndicator(close=data[("Close", stock_symbol)]).rsi()

macd = ta.trend.MACD(close=data[("Close", stock_symbol)])
data["MACD"] = macd.macd()
data["MACD_signal"] = macd.macd_signal()

print(data[["Close", "RSI", "MACD", "MACD_signal"]].tail(10))

def generate_signals(df):
    df = df.copy()

    df["Buy_Signal"] = (
        (df["RSI"] < 30) &
        (df["MACD"] > df["MACD_signal"]) &
        (df["MACD"].shift(1) <= df["MACD_signal"].shift(1))
    )

    df["Sell_Signal"] = (
        (df["RSI"] > 70) &
        (df["MACD"] < df["MACD_signal"]) &
        (df["MACD"].shift(1) >= df["MACD_signal"].shift(1))
    )

    return df

# Apply to stock data
data = generate_signals(data)
print(data[["Close", "RSI", "MACD", "MACD_signal", "Buy_Signal", "Sell_Signal"]].tail(15))

def simulate_trades(df, starting_cash=10000):
    df = df.copy()
    cash = starting_cash
    position = 0
    buy_price = 0
    equity_curve = []
    df["Action"] = None # Initialize Action column

    for i in range(len(df)):
        row = df.iloc[i]

        # Buy
        if row["Buy_Signal"].item() and position == 0:
            position = cash / row["Close"].item() # Access scalar value using .item()
            buy_price = row["Close"].item() # Access scalar value using .item()
            cash = 0  # all-in
            df.at[df.index[i], "Action"] = f"BUY @ {buy_price:.2f}"

        # Sell
        elif row["Sell_Signal"].item() and position > 0:
            sell_price = row["Close"].item() # Access scalar value using .item()
            cash = position * sell_price
            df.at[df.index[i], "Action"] = f"SELL @ {sell_price:.2f} | PnL: {(sell_price - buy_price):.2f}"
            position = 0
            buy_price = 0

        # Track total equity
        if position > 0:
            equity = position * row["Close"].item() # Access scalar value using .item()
        else:
            equity = cash
        equity_curve.append(equity)

    df["Equity"] = equity_curve
    return df

data = simulate_trades(data)
# Extract trade actions
result = data[["Close", "Buy_Signal", "Sell_Signal", "Action", "Equity"]][data["Action"].notna()]

# Check if there were any trades
if result.empty:
    print("📉 No buy/sell signals were triggered during the selected time period.")
else:
    print("✅ Trade Summary:")
    print(result)

"""Plot RSI graph"""

def plot_rsi(df):
    plt.figure(figsize=(12, 3))
    plt.plot(df.index, df["RSI"], label="RSI", color="purple")
    plt.axhline(30, linestyle="--", color="green", label="Oversold (30)")
    plt.axhline(70, linestyle="--", color="red", label="Overbought (70)")
    plt.title("RSI Over Time")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

"""Plot MACD graph"""

def plot_macd(df):
    plt.figure(figsize=(12, 3))
    plt.plot(df.index, df["MACD"], label="MACD", color="blue")
    plt.plot(df.index, df["MACD_signal"], label="Signal Line", color="orange")
    plt.axhline(0, linestyle="--", color="gray")
    plt.title("MACD & Signal Line")
    plt.xlabel("Date")
    plt.ylabel("MACD Value")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

"""Plot equity graph"""

def plot_equity_curve(df):
    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df["Equity"], label="Equity Curve", color='blue')
    plt.title("Portfolio Equity Over Time")
    plt.xlabel("Date")
    plt.ylabel("Equity ($)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_price_with_signals(df):
    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df["Close"], label=f"{stock_symbol} Close Price", color="black")

    # Mark Buy Signals
    plt.plot(df[df["Buy_Signal"]].index, df["Close"][df["Buy_Signal"]],
             marker="^", color="green", label="Buy Signal", linestyle="None")

    # Mark Sell Signals
    plt.plot(df[df["Sell_Signal"]].index, df["Close"][df["Sell_Signal"]],
             marker="v", color="red", label="Sell Signal", linestyle="None")

    plt.title(f"{stock_symbol} Price with Buy/Sell Signals")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

plot_rsi(data)
plot_macd(data)
plot_equity_curve(data)
plot_price_with_signals(data)
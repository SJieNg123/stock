# plot_utils.py

import matplotlib.pyplot as plt

def plot_rsi(df, rsi_buy, rsi_sell):
    plt.figure(figsize=(12, 3))
    plt.plot(df.index, df["RSI"], label="RSI", color="purple")
    plt.axhline(rsi_buy, linestyle="--", color="green", label=f"Oversold ({rsi_buy})")
    plt.axhline(rsi_sell, linestyle="--", color="red", label=f"Overbought ({rsi_sell})")
    plt.title("RSI Over Time")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

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

def plot_price_with_signals(df, stock_symbol):
    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df["Close"], label=f"{stock_symbol} Close Price", color="black")

    # Buy signals
    plt.plot(df[df["Buy_Signal"]].index, df["Close"][df["Buy_Signal"]],
             marker="^", color="green", label="Buy Signal", linestyle="None")

    # Sell signals
    plt.plot(df[df["Sell_Signal"]].index, df["Close"][df["Sell_Signal"]],
             marker="v", color="red", label="Sell Signal", linestyle="None")

    plt.title(f"{stock_symbol} Price with Buy/Sell Signals")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Test the function exists
if __name__ == "__main__":
    print("plot_utils.py loaded successfully")
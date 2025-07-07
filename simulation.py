# simulation.py

def simulate_trades(df, starting_cash):
    """
    Simulates a simple long-only strategy:
    - Buys full position on Buy_Signal
    - Sells entire position on Sell_Signal
    - Tracks equity over time
    """
    df = df.copy()
    cash = starting_cash
    position = 0
    buy_price = 0
    equity_curve = []
    df["Action"] = None  # Initialize Action column

    for i in range(len(df)):
        row = df.iloc[i]

        # Buy
        if row["Buy_Signal"] and position == 0:
            position = cash / row["Close"]
            buy_price = row["Close"]
            cash = 0
            df.at[df.index[i], "Action"] = f"BUY @ {buy_price:.2f}"

        # Sell
        elif row["Sell_Signal"] and position > 0:
            sell_price = row["Close"]
            cash = position * sell_price
            df.at[df.index[i], "Action"] = f"SELL @ {sell_price:.2f} | PnL: {(sell_price - buy_price):.2f}"
            position = 0
            buy_price = 0

        # Track equity
        equity = cash if position == 0 else position * row["Close"]
        equity_curve.append(equity)

    df["Equity"] = equity_curve
    return df

# Test the function exists
if __name__ == "__main__":
    print("simulation.py loaded successfully")
    # print("simulate_trades function is available")
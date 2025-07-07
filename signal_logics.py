# signal_logics.py

def generate_signals(df, rsi_buy, rsi_sell):
    """
    Generates Buy and Sell signals based on:
    - RSI threshold
    - MACD crossover
    """
    df = df.copy()

    df["Buy_Signal"] = (
        (df["RSI"] < rsi_buy) &
        (df["MACD"] > df["MACD_signal"]) &
        (df["MACD"].shift(1) <= df["MACD_signal"].shift(1))
    )

    df["Sell_Signal"] = (
        (df["RSI"] > rsi_sell) &
        (df["MACD"] < df["MACD_signal"]) &
        (df["MACD"].shift(1) >= df["MACD_signal"].shift(1))
    )

    return df

# Test the function exists
if __name__ == "__main__":
    print("signal_logic.py loaded successfully")
    # print("generate_signals function is available")
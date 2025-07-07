# data_handler.py

import yfinance as yf
import ta
import pandas as pd

def fetch_data(stock_symbol, time_period="1y"):
    """
    Download stock data using yfinance with specified time period.
    """
    try:
        print(f"📊 Fetching {time_period} data for {stock_symbol}...")
        df = yf.download(stock_symbol, period=time_period, interval="1d")
        if df.empty:
            raise ValueError(f"No data found for symbol '{stock_symbol}'")
        
        # Handle multi-level columns (if yfinance returns hierarchical columns)
        if isinstance(df.columns, pd.MultiIndex):
            df = df.droplevel(1, axis=1)  # Remove the second level (stock symbol)
        
        print(f"✅ Successfully fetched {len(df)} days of data")
        return df
    except Exception as e:
        print(f"❌ Error fetching data for {stock_symbol}: {e}")
        return None

def calculate_indicators(df):
    """
    Adds RSI and MACD indicators to the dataframe.
    """
    if df is None:
        return None
    
    df = df.copy()
    
    # Ensure df["Close"] is a 1-dimensional Series
    close_series = df["Close"].squeeze()  # Convert to 1D if it's 2D
    
    # Calculate RSI
    df["RSI"] = ta.momentum.RSIIndicator(close=close_series).rsi()
    
    # Calculate MACD
    macd = ta.trend.MACD(close=close_series)
    df["MACD"] = macd.macd()
    df["MACD_signal"] = macd.macd_signal()
    
    print("✅ Technical indicators calculated")
    return df

# Test the function exists
if __name__ == "__main__":
    print("data_handler.py loaded successfully")
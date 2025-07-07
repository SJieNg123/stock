# main.py

import yfinance as yf
import matplotlib.pyplot as plt

from user_inputs import get_all_inputs, display_configuration
from data_handler import fetch_data, calculate_indicators
from signal_logics import generate_signals
from simulation import simulate_trades
from plot_utils import (
    plot_rsi,
    plot_macd,
    plot_equity_curve,
    plot_price_with_signals
)

def main():
    # Get all user inputs
    config = get_all_inputs()
    display_configuration(config)
    
    # Extract configuration
    stock_symbol = config['stock_symbol']
    rsi_buy = config['rsi_buy']
    rsi_sell = config['rsi_sell']
    starting_cash = config['starting_cash']
    time_period = config['time_period']
    
    # --- Core Logic ---
    
    print("📊 Fetching data...")
    data = fetch_data(stock_symbol, time_period)  # Pass time_period
    if data is None:
        print("❌ Failed to fetch data. Exiting...")
        return
    
    print("📈 Calculating indicators...")
    data = calculate_indicators(data)
    if data is None:
        print("❌ Failed to calculate indicators. Exiting...")
        return
    
    # Display recent data
    print("\n📊 Recent Technical Indicators:")
    print(data[["Close", "RSI", "MACD", "MACD_signal"]].tail(10).round(2))
    
    print("🎯 Generating signals...")
    data = generate_signals(data, rsi_buy, rsi_sell)
    
    # Display signals
    print("\n🎯 Recent Signals:")
    print(data[["Close", "RSI", "MACD", "MACD_signal", "Buy_Signal", "Sell_Signal"]].tail(15))
    
    print("💰 Simulating trades...")
    data = simulate_trades(data, starting_cash)
    
    # --- Output Section ---
    
    result = data[["Close", "Buy_Signal", "Sell_Signal", "Action", "Equity"]][data["Action"].notna()]
    if result.empty:
        print("📉 No buy/sell signals were triggered during the selected time period.")
    else:
        print("\n✅ Trade Summary:")
        print(result.round(2))
    
    # --- Plotting ---
    
    print("📊 Generating plots...")
    plot_rsi(data, rsi_buy, rsi_sell)
    plot_macd(data)
    plot_equity_curve(data)
    plot_price_with_signals(data, stock_symbol)
    print("✅ All plots generated successfully!")

if __name__ == "__main__":
    main()
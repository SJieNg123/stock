# user_inputs.py

import yfinance as yf

def get_stock_symbol():
    """Get and validate stock symbol from user"""
    while True:
        stock_symbol = input("Enter stock ticker (e.g., NVDA, TSLA, AAPL): ").upper().strip()
        if not stock_symbol:
            print("❌ Please enter a valid stock ticker.")
            continue
        try:
            print(f"🔍 Validating symbol: {stock_symbol}...")
            test_data = yf.download(stock_symbol, period="5d", interval="1d")
            if test_data.empty:
                print(f"❌ No data found for stock '{stock_symbol}'. Please try another stock")
                continue
            print(f"✅ Valid symbol: {stock_symbol}")
            return stock_symbol
        except Exception as e:
            print(f"❌ Error fetching data for stock '{stock_symbol}': {e}. Please try again with a valid symbol.")

def get_rsi_thresholds():
    """Get and validate RSI buy/sell thresholds"""
    while True:
        try:
            rsi_buy = float(input("Enter RSI buy threshold (0-100, default 30): ") or 30)
            rsi_sell = float(input("Enter RSI sell threshold (0-100, default 70): ") or 70)
            
            if not (0 <= rsi_buy <= 100) or not (0 <= rsi_sell <= 100):
                print("❌ Please enter valid RSI thresholds between 0 and 100.")
                continue
                
            if rsi_buy >= rsi_sell:
                print("❌ Buy threshold must be less than Sell threshold.")
                continue
                
            return rsi_buy, rsi_sell
        except ValueError:
            print("❌ Invalid input. Please enter numeric values for RSI thresholds.")

def get_macd_parameters():
    """Get MACD parameters (for future expansion)"""
    while True:
        try:
            print("\n📈 MACD Parameters (press Enter for defaults):")
            fast_period = int(input("Fast EMA period (default 12): ") or 12)
            slow_period = int(input("Slow EMA period (default 26): ") or 26)
            signal_period = int(input("Signal line period (default 9): ") or 9)
            
            if fast_period >= slow_period:
                print("❌ Fast period must be less than slow period.")
                continue
                
            if any(x <= 0 for x in [fast_period, slow_period, signal_period]):
                print("❌ All periods must be positive numbers.")
                continue
                
            return fast_period, slow_period, signal_period
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")

def get_bollinger_bands_parameters():
    """Get Bollinger Bands parameters (for future expansion)"""
    while True:
        try:
            print("\n📊 Bollinger Bands Parameters:")
            bb_period = int(input("Moving average period (default 20): ") or 20)
            bb_std = float(input("Standard deviation multiplier (default 2.0): ") or 2.0)
            
            if bb_period <= 0 or bb_std <= 0:
                print("❌ Parameters must be positive numbers.")
                continue
                
            return bb_period, bb_std
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")

def get_starting_cash():
    """Get and validate starting cash amount"""
    while True:
        try:
            starting_cash = float(input("Enter starting cash amount (default $10,000): ") or 10000)
            if starting_cash <= 0:
                print("❌ Starting cash must be a positive number.")
                continue
            return starting_cash
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value for starting cash.")

def get_time_period():
    """Get data time period (for future expansion)"""
    periods = {
        '1': '1mo',
        '2': '3mo', 
        '3': '6mo',
        '4': '1y',
        '5': '2y',
        '6': '5y'
    }
    
    while True:
        print("\n📅 Select time period:")
        print("1. 1 Month")
        print("2. 3 Months") 
        print("3. 6 Months")
        print("4. 1 Year (default)")
        print("5. 2 Years")
        print("6. 5 Years")
        
        choice = input("Enter choice (1-6, default 4): ") or '4'
        
        if choice in periods:
            return periods[choice]
        else:
            print("❌ Invalid choice. Please select 1-6.")

def get_all_inputs():
    """Get all user inputs in one function"""
    print("🚀 Stock Trading Bot Configuration\n")
    
    # Basic inputs
    stock_symbol = get_stock_symbol()
    time_period = get_time_period()
    starting_cash = get_starting_cash()
    
    # Technical indicator parameters
    rsi_buy, rsi_sell = get_rsi_thresholds()
    
    # Future indicators (commented out for now)
    # macd_fast, macd_slow, macd_signal = get_macd_parameters()
    # bb_period, bb_std = get_bollinger_bands_parameters()
    
    # Return configuration dictionary
    config = {
        'stock_symbol': stock_symbol,
        'time_period': time_period,
        'starting_cash': starting_cash,
        'rsi_buy': rsi_buy,
        'rsi_sell': rsi_sell,
        # 'macd_fast': macd_fast,
        # 'macd_slow': macd_slow, 
        # 'macd_signal': macd_signal,
        # 'bb_period': bb_period,
        # 'bb_std': bb_std
    }
    
    return config

def display_configuration(config):
    """Display the current configuration"""
    print("\n" + "="*50)
    print("📋 TRADING CONFIGURATION")
    print("="*50)
    print(f"Stock Symbol: {config['stock_symbol']}")
    print(f"Time Period: {config['time_period']}")
    print(f"Starting Cash: ${config['starting_cash']:,.2f}")
    print(f"RSI Buy Threshold: {config['rsi_buy']}")
    print(f"RSI Sell Threshold: {config['rsi_sell']}")
    print("="*50 + "\n")

# Test the module
if __name__ == "__main__":
    config = get_all_inputs()
    display_configuration(config)
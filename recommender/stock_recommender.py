import yfinance as yf
import pandas as pd
import ta

def get_stock_data(ticker):
    """Fetch historical data for a stock ticker"""
    df = yf.download(ticker, period="1mo", interval="1d")
    df.dropna(inplace=True)
    return df

def analyze_stock(ticker):
    df = get_stock_data(ticker)
    
    # Extract the Close price as a proper Series
    close = df['Close'].iloc[:, 0]
    
    # Calculate RSI and MACD using ta
    rsi_indicator = ta.momentum.RSIIndicator(close)
    df['rsi'] = rsi_indicator.rsi()
    
    macd = ta.trend.MACD(close)
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    
    # Latest values - using the recommended approach
    latest = df.iloc[-1]
    rsi = float(latest['rsi'].iloc[0]) if isinstance(latest['rsi'], pd.Series) else latest['rsi']
    macd_val = float(latest['macd'].iloc[0]) if isinstance(latest['macd'], pd.Series) else latest['macd']
    signal_val = float(latest['macd_signal'].iloc[0]) if isinstance(latest['macd_signal'], pd.Series) else latest['macd_signal']
    
    # Bullish condition
    is_bullish = (30 < rsi < 70) and (macd_val > signal_val)
    return is_bullish, round(rsi, 2), round(macd_val - signal_val, 2)


def recommend_stocks(stock_list):
    """Loop through stocks and return bullish ones"""
    recommendations = []
    for ticker in stock_list:
        try:
            bullish, rsi, macd_diff = analyze_stock(ticker)
            if bullish:
                recommendations.append({
                    'ticker': ticker,
                    'rsi': rsi,
                    'macd_diff': macd_diff
                })
        except Exception as e:
            print(f"Error analyzing {ticker}: {e}")
    return recommendations

def format_recommendation_text(recommendations):
    if not recommendations:
        return "No bullish stock signals detected today."

    text = "📈 Top Stock Picks Based on RSI & MACD:\n\n"
    for rec in recommendations:
        text += f"• {rec['ticker']}: RSI={rec['rsi']}, MACD-Δ={rec['macd_diff']}\n"
    return text

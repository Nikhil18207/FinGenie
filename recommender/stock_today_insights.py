# recommender/stock_today_insights.py

import yfinance as yf
import pandas as pd

def get_today_stock_update(ticker):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d", interval="1d")

        if hist.shape[0] < 2:
            return None

        today = hist.iloc[-1]
        yesterday = hist.iloc[-2]

        open_price = today['Open']
        close_price = today['Close']
        change = ((close_price - open_price) / open_price) * 100
        volume = today['Volume']
        avg_volume = hist['Volume'].mean()

        # Classify
        if change > 2 and volume > avg_volume * 1.2:
            verdict = "✅ Invest"
        elif change < -2:
            verdict = "🚫 Avoid"
        else:
            verdict = "🤔 Hold"

        return {
            'ticker': ticker,
            'open': round(open_price, 2),
            'close': round(close_price, 2),
            'change': round(change, 2),
            'volume': int(volume),
            'verdict': verdict
        }

    except Exception as e:
        print(f"Error with {ticker}: {e}")
        return None


def get_today_insights(watchlist):
    insights = []
    for ticker in watchlist:
        info = get_today_stock_update(ticker)
        if info:
            insights.append(info)
    return insights


def format_today_summary(insights):
    if not insights:
        return "📉 No data available for today's market update."

    summary = "📊 Today's Market Insights:\n\n"
    for stock in insights:
        summary += (
            f"{stock['ticker']}: {stock['verdict']}\n"
            f"  - Open: ${stock['open']} → Close: ${stock['close']} ({stock['change']}%)\n"
            f"  - Volume: {stock['volume']}\n\n"
        )
    return summary

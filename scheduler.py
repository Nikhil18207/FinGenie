import schedule
import time
from recommender.stock_recommender import recommend_stocks, format_recommendation_text
from utils.email_notifier import send_stock_email

def run_daily_alert():
    print("⏰ Running scheduled stock check...")

    watchlist = ['AAPL', 'GOOGL', 'MSFT', 'NVDA', 'TSLA']
    recommendations = recommend_stocks(watchlist)
    summary = format_recommendation_text(recommendations)

    print(summary)
    send_stock_email("📈 FinGenie – Daily Stock Recommendations", summary)

# Test: run every 10 seconds
schedule.every(10).seconds.do(run_daily_alert)

print("✅ FinGenie scheduler started. Running every 10 seconds...")

while True:
    schedule.run_pending()
    print("⏳ Waiting...")
    time.sleep(10)

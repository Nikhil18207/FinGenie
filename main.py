# main.py

from recommender.stock_recommender import recommend_stocks, format_recommendation_text
from recommender.stock_today_insights import get_today_insights, format_today_summary
from recommender.news_summarizer import get_stock_news_summary  # 🧠 New
from utils.email_notifier import send_stock_email
from voice.voice_input import listen_to_user
from voice.voice_output import speak_response

# Your stock watchlist
my_watchlist = ['AAPL', 'GOOGL', 'MSFT', 'NVDA', 'TSLA']

# 👂 Voice Command
command = listen_to_user()

if "recommend" in command or "stock" in command:
    recommendations = recommend_stocks(my_watchlist)
    summary = format_recommendation_text(recommendations)

    print(summary)
    speak_response(summary)
    send_stock_email("📈 FinGenie – Today's Stock Recommendations", summary)

elif "market" in command or "update" in command or "today" in command:
    insights = get_today_insights(my_watchlist)
    insight_summary = format_today_summary(insights)

    print(insight_summary)
    speak_response(insight_summary)
    send_stock_email("📊 FinGenie – Today's Market Insights", insight_summary)

# 🧠 NEW: Ask about a specific company in the watchlist
elif any(stock.lower() in command.lower() for stock in my_watchlist):
    company = next((stock for stock in my_watchlist if stock.lower() in command.lower()), None)
    if company:
        summary = get_stock_news_summary(company)
        print(summary)
        speak_response(summary)
        send_stock_email(f"📰 FinGenie – News Summary for {company}", summary)

else:
    speak_response("You can ask me to recommend stocks, get today's market update, or ask about a specific company.")

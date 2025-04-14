# recommender/news_summarizer.py

import feedparser
import openai
from utils.helpers import get_env_var

# ✅ Initialize OpenAI client correctly for v1.x
openai.api_key = get_env_var("OPENAI_API_KEY")


def fetch_news_headlines(company):
    url = f"https://news.google.com/rss/search?q={company}+stock+when:1d&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries[:5]]
    return headlines


def summarize_with_gpt(company, headlines):
    if not headlines:
        return f"No recent news found for {company}."

    prompt = (
        f"You're a financial assistant. Summarize these news headlines about {company} stock "
        f"into a brief update explaining any price movement, investor sentiment, or key events:\n\n"
        + "\n".join(f"- {hl}" for hl in headlines)
        + "\n\nGive a clear, short explanation (2-4 sentences)."
    )

    try:
        # ✅ Use new v1.x compatible OpenAI call
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Failed to summarize news: {e}"


def get_stock_news_summary(company):
    headlines = fetch_news_headlines(company)
    summary = summarize_with_gpt(company, headlines)
    return summary


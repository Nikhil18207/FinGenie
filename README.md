# 🧞‍♂️ FinGenie – Your AI-Powered Stock Assistant

FinGenie is your intelligent stock market companion that combines **GPT-powered insights**, **real-time market data**, **technical recommendations**, **portfolio tracking**, and even **voice support** — all in one sleek Streamlit dashboard.

---

## 🚀 Features

### 🗣 Voice-Driven Assistant
- Interact with FinGenie using your voice
- Ask for market updates, recommendations, or specific stock news

### 📈 Real-Time Market Insights
- View live updates for your watchlist
- AI suggests whether to **Buy**, **Sell**, or **Hold**

### 🧠 GPT-Powered Stock News Summaries
- Summarizes latest news headlines for any stock using OpenAI
- Explains price changes, market sentiment, or key events

### 📉 Candlestick Charts with Volume
- Beautiful interactive charts powered by Plotly
- Analyzes past trends over 1-month intervals

### 💼 Portfolio Tracker (CSV + Manual Entry)
- Upload a CSV file (columns: `Ticker`, `Shares`) to track investments
- Or add stocks manually with real-time valuation

### ⚙️ Watchlist Management
- Add/remove tickers from your personal watchlist
- All actions update dynamically

---

## 🛠 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io)
- **Market Data**: [yfinance](https://pypi.org/project/yfinance/)
- **Technical Analysis**: [ta-lib](https://github.com/bukosabino/ta)
- **Voice Input**: [streamlit-mic-recorder](https://github.com/B4PT0R/streamlit-mic-recorder), [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- **AI Summarizer**: [OpenAI GPT-3.5 API](https://openai.com/)
- **Charts**: [Plotly](https://plotly.com/python/)
- **Scheduling (for alerts)**: `schedule` + `email_notifier`

---

## 📦 Installation (Local)

```bash
# 1. Clone the repository
git clone https://github.com/Nikhil18207/FinGenie.git
cd FinGenie

# 2. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your .env file
touch .env
# Add your OpenAI API key in it:
# OPENAI_API_KEY=sk-xxxxxxxxxxxx

# 5. Run the app
streamlit run dashboard.py


📊 Portfolio CSV Format
csv
Copy
Edit
Ticker,Shares
AAPL,10
MSFT,5
GOOGL,3
You can upload this from the dashboard or add entries manually.

🧪 Example Commands (Voice)
“What’s today’s market update?”

“Recommend some stocks to invest in”

“Tell me about AAPL stock news”

🌐 Try It Live
🔗 FinGenie on Streamlit Cloud
(Demo link — replace with your deployed URL once live)

📁 Project Structure
bash
Copy
Edit
├── dashboard.py                  # Main Streamlit UI
├── scheduler.py                  # Background scheduler for alerts
├── recommender/
│   ├── stock_recommender.py
│   ├── stock_today_insights.py
│   ├── stock_charts.py
│   └── news_summarizer.py
├── utils/
│   ├── email_notifier.py
│   ├── helpers.py
│   └── watchlist_manager.py
├── portfolio/
│   └── portfolio_tracker.py
├── voice/
│   ├── voice_input.py
│   └── voice_output.py
├── requirements.txt
└── .env (not tracked)
🙋‍♂️ Author
Built with ❤️ by Nikhil Kumar

📧 nikhil18207@gmail.com

🐦 @nikhil18207

💼 LinkedIn

⚠️ Disclaimer
This app is built for educational/research/demo purposes only. It should not be used for actual financial trading decisions.

⭐ Star this repo if you like it!
bash
Copy
Edit
git commit -m "⭐ Added AI stock assistant with GPT, charts, and voice!"


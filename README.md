# 🧞‍♂️ FinGenie – Your AI-Powered Stock Assistant

FinGenie is your intelligent stock market companion that combines **GPT-powered insights**, **real-time market data**, **technical recommendations**, **portfolio tracking**, and even **voice support** — all in one sleek Streamlit dashboard.

![FinGenie Banner](https://github.com/Nikhil18207/FinGenie/assets/banner.png) <!-- Add a banner image if you'd like -->

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

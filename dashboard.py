import streamlit as st
from recommender.stock_recommender import recommend_stocks, format_recommendation_text
from recommender.stock_today_insights import get_today_insights, format_today_summary
from recommender.news_summarizer import get_stock_news_summary
from recommender.stock_charts import get_candlestick_chart
from utils.email_notifier import send_stock_email
from streamlit_mic_recorder import mic_recorder  
import speech_recognition as sr
import tempfile
from utils.watchlist_manager import load_watchlist, add_stock, remove_stock
from pydub import AudioSegment
from portfolio.portfolio_tracker import load_portfolio_csv, calculate_portfolio
import pandas as pd


# Set page config with a vibrant theme
st.set_page_config(
    page_title="📊 FinGenie – AI Stock Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for colorful and stylish design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    /* Global styles */
    body {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: #ffffff;
    }

    /* Main container */
    .main {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

    /* Title */
    h1 {
        color: #00d4ff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        font-weight: 600;
        text-align: center;
        animation: fadeIn 1s ease-in;
    }

    /* Subheaders */
    h2 {
        color: #ff6f91;
        font-weight: 400;
        margin-top: 20px;
    }

    /* Selectbox and inputs */
    .stSelectbox, .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.15);
        color: #ffffff;
        border-radius: 10px;
        border: 1px solid #00d4ff;
        padding: 10px;
        transition: all 0.3s ease;
    }

    .stSelectbox:hover, .stTextInput > div > div > input:hover {
        border-color: #ff6f91;
        box-shadow: 0 0 10px rgba(255, 105, 145, 0.5);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #00d4ff, #ff6f91);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-weight: 600;
        transition: transform 0.2s, box-shadow 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 212, 255, 0.4);
    }

    /* Expander */
    .streamlit-expander {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        border: 1px solid #00d4ff;
        margin-bottom: 15px;
    }

    .streamlit-expanderHeader {
        color: #ffffff !important;
        font-weight: 600;
        background: linear-gradient(45deg, #2a5298, #1e3c72);
        border-radius: 10px;
        padding: 10px;
    }

    /* Markdown and text */
    .stMarkdown, .stSuccess, .stWarning, .stError {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #00d4ff;
    }

    .stSuccess {
        border-left-color: #00ff88;
    }

    .stWarning {
        border-left-color: #ffaa00;
    }

    .stError {
        border-left-color: #ff4d4d;
    }

    /* Chart container */
    .stPlotlyChart {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Audio player */
    audio {
        width: 100%;
        border-radius: 10px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title with emoji
st.markdown("<h1>🧞‍♂️ FinGenie – Your AI-Powered Stock Assistant</h1>", unsafe_allow_html=True)

# Watchlist
watchlist = load_watchlist()
if not watchlist:
    st.warning("⚠️ Your watchlist is empty. Add at least one stock to continue.")
    st.stop()


# Main container
with st.container():
    selected_stock = st.selectbox("🔎 Select a Company to Analyze", watchlist, help="Choose a stock from your watchlist")

    # Stock Chart
    with st.expander("📉 Candlestick Chart (1 Month)", expanded=True):
        chart = get_candlestick_chart(selected_stock)
        st.plotly_chart(chart, use_container_width=True)

    # Watchlist Editor
    with st.expander("⚙️ Manage Your Watchlist", expanded=False):
        st.write("Add or remove stocks from your FinGenie watchlist.")
        new_stock = st.text_input("➕ Add New Stock Ticker (e.g., META)", "")
        if st.button("Add Stock"):
            if new_stock.strip():
                add_stock(new_stock.strip())
                st.success(f"Added {new_stock.upper()} to watchlist. Please refresh.")
        
        remove_stock_option = st.selectbox("❌ Remove a Stock", watchlist)
        if st.button("Remove Selected Stock"):
            remove_stock(remove_stock_option)
            st.success(f"Removed {remove_stock_option} from watchlist. Please refresh.")

    # Market Insights
    with st.expander("📊 Today's Market Insights", expanded=True):
        insights = get_today_insights(watchlist)
        summary = format_today_summary(insights)
        st.markdown(f"```\n{summary}\n```")
        if st.button("📬 Email Market Insights"):
            send_stock_email("📊 FinGenie – Today's Market Insights", summary)
            st.success("Market insights sent!")

    # Stock Recommendations
    with st.expander("📈 Technical Recommendations", expanded=True):
        recos = recommend_stocks(watchlist)
        rec_summary = format_recommendation_text(recos)
        st.markdown(f"```\n{rec_summary}\n```")
        if st.button("📬 Email Stock Recommendations"):
            send_stock_email("📈 FinGenie – Stock Recommendations", rec_summary)
            st.success("Recommendations emailed!")

    # GPT News Summary
    with st.expander("🧠 GPT News Summary for Selected Stock", expanded=True):
        if st.button("📰 Generate Summary"):
            news = get_stock_news_summary(selected_stock)
            st.markdown(f"```\n{news}\n```")
            if st.button("📬 Email This Summary"):
                send_stock_email(f"🧠 GPT Summary for {selected_stock}", news)
                st.success("GPT summary emailed!")

    # Voice Assistant
    st.subheader("🎤 Voice Assistant")
    audio = mic_recorder(start_prompt="🎙️ Click to Speak", stop_prompt="✅ Done", key="mic")

    if audio:
        st.audio(audio['bytes'], format='audio/wav')
        try:
            # Save mic-recorder audio to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
                tmp.write(audio['bytes'])
                raw_audio_path = tmp.name

            # Convert to PCM WAV using pydub
            pcm_path = raw_audio_path.replace(".webm", "_converted.wav")
            sound = AudioSegment.from_file(raw_audio_path)
            sound.export(pcm_path, format="wav")

            # Transcribe using speech recognition
            recognizer = sr.Recognizer()
            with sr.AudioFile(pcm_path) as source:
                audio_data = recognizer.record(source)

            command = recognizer.recognize_google(audio_data)
            st.success(f"🗣️ You said: {command}")

            # Process voice command
            if any(ticker.lower() in command.lower() for ticker in watchlist):
                stock = next((ticker for ticker in watchlist if ticker.lower() in command.lower()), None)
                summary = get_stock_news_summary(stock)
                st.markdown(f"🧠 GPT Summary for **{stock}**:\n\n```\n{summary}\n```")

            elif "recommend" in command.lower():
                recommendations = recommend_stocks(watchlist)
                reco_summary = format_recommendation_text(recommendations)
                st.markdown(f"📈 Recommendations:\n\n```\n{reco_summary}\n```")

            elif "market" in command.lower() or "update" in command.lower():
                market_summary = format_today_summary(get_today_insights(watchlist))
                st.markdown(f"📊 Market Insight:\n\n```\n{market_summary}\n```")

            else:
                st.warning("🤔 I heard you, but didn't match it to any stock or command.")

        except sr.UnknownValueError:
            st.warning("🤷 Sorry, couldn't understand your voice.")
        except sr.RequestError:
            st.error("⚠️ Error connecting to voice recognition service.")
        except Exception as e:
            st.error(f"❌ Voice processing failed: {e}")
            
# --- 💼 Portfolio Tracker ---
with st.expander("💼 Portfolio Tracker", expanded=False):
    st.write("Upload your portfolio or manually add stocks to analyze your holdings in real-time.")

    # --- 📁 CSV Upload ---
    uploaded_file = st.file_uploader("📁 Upload CSV with columns: Ticker, Shares", type=["csv"])

    if uploaded_file:
        try:
            portfolio_df = load_portfolio_csv(uploaded_file)
            result_df = calculate_portfolio(portfolio_df)

            st.subheader("📊 Portfolio Summary from CSV")
            st.dataframe(result_df.style.format({"Current Price": "₹{:.2f}", "Value": "₹{:.2f}"}))

            total_value = result_df["Value"].sum()
            st.success(f"💰 **Total Portfolio Value: ₹{round(total_value, 2)}**")

        except Exception as e:
            st.error(f"❌ Failed to process file: {e}")

    st.divider()

    # --- ✍️ Manual Entry ---
    st.markdown("### 📝 Or Add a Stock Manually")

    with st.form("manual_entry_form"):
        manual_ticker = st.text_input("📈 Stock Ticker (e.g., AAPL)", max_chars=10)
        manual_shares = st.number_input("🔢 Number of Shares", min_value=0, step=1)
        submit_manual = st.form_submit_button("➕ Add to Portfolio")

    # Session state to store manual entries
    if "manual_portfolio" not in st.session_state:
        st.session_state.manual_portfolio = []

    if submit_manual and manual_ticker and manual_shares > 0:
        st.session_state.manual_portfolio.append({
            "Ticker": manual_ticker.upper(),
            "Shares": manual_shares
        })
        st.success(f"✅ Added {manual_ticker.upper()} – {manual_shares} shares")

    if st.session_state.manual_portfolio:
        manual_df = pd.DataFrame(st.session_state.manual_portfolio)
        result_df_manual = calculate_portfolio(manual_df)

        st.subheader("🧾 Manual Entry Summary")
        st.dataframe(result_df_manual.style.format({"Current Price": "₹{:.2f}", "Value": "₹{:.2f}"}))

        total_manual = result_df_manual["Value"].sum()
        st.success(f"💼 **Manual Portfolio Value: ₹{round(total_manual, 2)}**")

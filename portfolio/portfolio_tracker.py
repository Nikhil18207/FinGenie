import pandas as pd
import yfinance as yf

def load_portfolio_csv(file) -> pd.DataFrame:
    df = pd.read_csv(file)
    df.columns = [col.strip().capitalize() for col in df.columns]
    return df[df["Ticker"].notna() & df["Shares"].notna()]

def fetch_current_prices(tickers: list) -> dict:
    prices = {}
    for ticker in tickers:
        try:
            data = yf.Ticker(ticker).history(period="1d")
            prices[ticker] = data["Close"].iloc[-1]
        except:
            prices[ticker] = 0
    return prices

def calculate_portfolio(df: pd.DataFrame) -> pd.DataFrame:
    prices = fetch_current_prices(df["Ticker"].tolist())
    df["Current Price"] = df["Ticker"].map(prices)
    df["Value"] = df["Shares"] * df["Current Price"]
    return df

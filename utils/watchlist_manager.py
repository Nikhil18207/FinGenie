# utils/watchlist_manager.py

import json
import os

WATCHLIST_FILE = "watchlist.json"

def load_watchlist():
    if not os.path.exists(WATCHLIST_FILE):
        save_watchlist(["AAPL", "GOOGL", "MSFT", "NVDA", "TSLA"])
    with open(WATCHLIST_FILE, "r") as f:
        data = json.load(f)
        if not data:  # empty list
            save_watchlist(["AAPL"])  # re-seed
            return ["AAPL"]
        return data

def save_watchlist(watchlist):
    with open(WATCHLIST_FILE, "w") as f:
        json.dump(watchlist, f)

def add_stock(ticker):
    watchlist = load_watchlist()
    ticker = ticker.upper()
    if ticker not in watchlist:
        watchlist.append(ticker)
        save_watchlist(watchlist)

def remove_stock(ticker):
    watchlist = load_watchlist()
    ticker = ticker.upper()
    if ticker in watchlist:
        watchlist.remove(ticker)
        save_watchlist(watchlist)

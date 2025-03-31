# Fetch financial data from APIs

# Fetch financial data from APIs

import yfinance as yf
import requests

def get_stock_data(symbol, period="1y", interval="1d"):
    """Fetches historical stock data from Yahoo Finance."""
    stock = yf.Ticker(symbol)
    data = stock.history(period=period, interval=interval)
    return data


def get_risk_data(symbol, api_key, debug=False):
    """Fetches risk metrics and volatility data from Alpha Vantage."""
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key  # uses dynamic API key
    }
    
    response = requests.get(url, params=params)

    if debug:
        print(f"[DEBUG] Response Status: {response.status_code}")
        print(f"[DEBUG] Raw API Response: {response.text}")  

    data = response.json()
    
    if "Time Series (Daily)" in data:
        return data["Time Series (Daily)"]
    elif "Note" in data:
        return {"error": "API Limit Exceeded: " + data["Note"]}
    elif "Error Message" in data:
        return {"error": "Invalid API Call: " + data["Error Message"]}
    else:
        return {"error": "Failed to fetch data. Check API key, symbol, or limits."}

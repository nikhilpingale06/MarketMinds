# Technical Analysis

import matplotlib.pyplot as plt

def add_technical_indicators(data):
    """Adds Moving Averages and RSI to stock data."""
    data["SMA_50"] = data["Close"].rolling(window=50).mean()  # 50-day SMA
    data["SMA_200"] = data["Close"].rolling(window=200).mean()  # 200-day SMA

    # RSI Calculation
    delta = data["Close"].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data["RSI"] = 100 - (100 / (1 + rs))

    return data

def plot_stock_trends(data, title="Stock Trends"):
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data["Close"], label="Close Price", color="blue")
    plt.plot(data.index, data["SMA_50"], label="50-Day SMA", color="green", linestyle="dashed")
    plt.plot(data.index, data["SMA_200"], label="200-Day SMA", color="red", linestyle="dashed")
    plt.legend()
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid()
    plt.show()
from crewai import Task

def create_market_analysis_task(agent, symbol):
    return Task(
        description=f"Conduct complete technical analysis of {symbol}",
        agent=agent,
        input_variables=["symbol"],
        expected_output="""Concise report containing:
        1. Current price and key moving averages (50/200-day)
        2. RSI value and interpretation
        3. Basic trend classification"""
    )

def create_sentiment_task(agent, symbol):
    return Task(
        description=f"""
        Analyze sentiment for {symbol}'s stock from latest news headlines.
        Use SerperSearchTool to find recent articles and provide a concise analysis.
        Include sentiment direction and key reason for the assessment.
        """,
        agent=agent,
        input_variables=["symbol"],
        expected_output=f"""
        {symbol} SENTIMENT: [Positive/Negative/Neutral]
        Strength: [Strong/Moderate/Weak]
        Key Point: [Brief reason in 10-15 words]
        Headline: "[Most significant recent headline]"
        """
    )


def create_risk_task(agent, symbol):
    return Task(
        description="Fetch stock market data and risk assessment for the given stock symbol.",
        expected_output="A risk assessment report with stock price data and risk score.",
        agent=agent,
        input_variables=["symbol"]
    )


def create_report_task(agent):
    return Task(
        description=(
            "Compile insights from the Market Analyst, Sentiment Analysis, and Risk Assessment agents. "
            "Generate a structured investment report including market sentiment, technical indicators, "
            "risk assessment, and a buy/sell recommendation. Format the response in a professional financial report style."
        ),
        expected_output=(
            "A structured financial report containing: \n"
            "- Asset name (e.g., AAPL, BTC) \n"
            "- Market sentiment (Bullish, Bearish, Neutral) \n"
            "- Technical indicators (RSI, MACD, SMA, etc.) \n"
            "- Price prediction or trend analysis \n"
            "- Risk level assessment (Low, Medium, High) \n"
            "- Key risk factors affecting investment \n"
            "- Final investment recommendation (Buy/Sell/Hold) \n"
            "- Supporting insights from market trends and risk analysis"
        ),
        agent=agent
    )



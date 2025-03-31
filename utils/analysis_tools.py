from crewai.tools import tool  
from utils.data_fetcher import get_stock_data, get_risk_data
from utils.technical_analysis import add_technical_indicators
from typing import Dict, Any
import pandas as pd
import requests

# Custom Tool for Market Analysis Agent
@tool("StockAnalysisTool")
def stock_analysis_tool(symbol: str) -> dict:
    """Performs technical analysis using:
    - 50/200-day SMAs 
    - 14-day RSI"""
    try:
        data = get_stock_data(symbol)  

        if len(data) < 200:
            return {"error": f"Need 200 trading days (got {len(data)})"}
        if data.empty or "Close" not in data.columns:
            return {"error": "Invalid/missing price data"}
        
        analyzed = add_technical_indicators(data.copy())
        latest = analyzed.iloc[-1]  
        
        return {
            "symbol": symbol,
            "current_price": round(float(latest["Close"]), 2),
            "moving_averages": {
                "SMA_50": round(float(latest["SMA_50"]), 2),
                "SMA_200": round(float(latest["SMA_200"]), 2),
                "position": "Above 200DMA" if latest["Close"] > latest["SMA_200"] else "Below"
            },
            "momentum": {
                "RSI": round(float(latest["RSI"]), 1),
                "status": "Overbought (>70)" if latest["RSI"] > 70 
                          else "Oversold (<30)" if latest["RSI"] < 30 
                          else "Neutral"
            },
            "analysis_period": f"{analyzed.index[0].date()} to {analyzed.index[-1].date()}"
        }
        
    except Exception as e:
        return {"error": f"Analysis failed: {str(e)}"}
    

    
# Custom Tool for Sentiment Analysis Agent
@tool("SerperSearchTool")
def serper_search_tool(query: str, api_key: str) -> Dict[str, Any]:
    """Searches the web using Serper API for the latest information.
    
    Args:
        query: The search query to look up
        api_key: API Key for Serper Search
    """
    try:
        if not api_key:
            return {"error": "Serper API key not provided"}
            
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }
        
        payload = {
            "q": query,
            "num": 1  
        }
        
        response = requests.post(
            "https://google.serper.dev/search",
            headers=headers,
            json=payload
        )
        
        search_results = response.json()
        
        formatted_results = {
            "query": query,
            "results": []
        }
        
        if "organic" in search_results:
            for result in search_results["organic"][:2]:
                formatted_results["results"].append({
                    "title": result.get("title"),
                    "link": result.get("link"),
                    "snippet": result.get("snippet")
                })
            
        return formatted_results
        
    except Exception as e:
        return {"error": f"Search failed: {str(e)}"}
    



# Custom Tool for Risk Assessment Agent
@tool("RiskAssessmentTool")
def risk_assessment_tool(symbol: str) -> dict:
    """Calculates stock risk metrics from Alpha Vantage data."""
    try:
        risk_data = get_risk_data(symbol)
        
        if isinstance(risk_data, dict) and "error" in risk_data:
            return risk_data
            
        df = pd.DataFrame(risk_data).T
        if df.empty:
            return {"error": "No price data available"}
            
        close_col = next((col for col in ["4. close", "close", "Close"] if col in df), None)
        if not close_col:
            return {"error": "Could not find closing prices"}
            
        close_prices = pd.to_numeric(df[close_col], errors='coerce').dropna()
        if len(close_prices) < 2:  
            return {"error": "Insufficient data points"}
            
        latest_close = round(float(close_prices.iloc[0]), 2)
        volatility = round(close_prices.pct_change().std(), 4)
        
        return {
            "symbol": symbol,
            "latest_price": latest_close,
            "volatility": volatility,
            "risk_level": "High" if volatility > 0.02 else "Medium" if volatility > 0.01 else "Low",
            "data_points": len(close_prices)
        }
        
    except Exception as e:
        return {"error": f"Risk assessment failed: {str(e)}"}

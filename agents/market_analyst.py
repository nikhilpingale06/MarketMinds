# Market Analyst Agent

from crewai import Agent
from utils.analysis_tools import stock_analysis_tool

from dotenv import load_dotenv
load_dotenv()

def create_market_analyst(Llm):
    return Agent(
    role="Market Analyst",
    goal="Analyze stock and crypto market trends based on real-time and historical data.",
    backstory="A highly skilled financial analyst with expertise in stock market trends, economic indicators, and technical analysis.",  
    llm=Llm,
    tools=[stock_analysis_tool],
    verbose=False
    )

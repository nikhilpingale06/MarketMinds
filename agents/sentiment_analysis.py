# Sentiment Analysis Agent

from crewai import Agent  
from utils.analysis_tools import serper_search_tool
from dotenv import load_dotenv
load_dotenv()

def create_sentiment_analyst(Llm):
    return Agent(
        role="Sentiment Analyst",
        goal="Analyze stock sentiment from latest news headlines",
        backstory="Expert AI analyst that quickly assesses market sentiment",
        llm=Llm,
        verbose=False,
        tools=[serper_search_tool]
    )

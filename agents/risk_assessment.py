# Risk Assessment Agent

from crewai import Agent
from utils.analysis_tools import risk_assessment_tool 
from dotenv import load_dotenv
load_dotenv()

def create_risk_assessor(Llm):
    return Agent(
        role="Risk Analyst",
        goal="Assess financial risks based on market data and risk metrics.",
        backstory="A financial expert specializing in risk management, volatility analysis, and financial stability assessment.",
        llm=Llm,
        tools=[risk_assessment_tool],
        verbose=False
    )



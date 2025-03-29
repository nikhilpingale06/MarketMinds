# Investment Report Generator

from crewai import Agent
from dotenv import load_dotenv
load_dotenv()

def create_report_generator(Llm):
    return Agent(
        role="Investment Report Generator",
        goal="Generate structured investment reports based on market and sentiment analysis",
        backstory=(
            "An AI-powered financial analyst who synthesizes stock and crypto insights into "
            "clear, actionable investment reports."
        ),
        llm=Llm,
        verbose=False
    )


# Entry point for running the full AI crew

from crewai import Crew, LLM
from agents.market_analyst import *
from agents.sentiment_analysis import *
from agents.risk_assessment import *
from agents.report_generator import *
from tasks.agent_tasks import *
from utils.api_keys import *

from dotenv import load_dotenv
load_dotenv()


def main():
    # Initialize LLMs
    groq_llm1 = LLM(model="groq/llama3-70b-8192", max_tokens=500)
    groq_llm2 = LLM(model="groq/gemma2-9b-it", max_tokens=700)
    groq_llm3 = LLM(model="groq/llama-3.1-8b-instant", max_tokens=1000)

    # Create agents
    market_analyst = create_market_analyst(groq_llm1)
    sentiment_analyst = create_sentiment_analyst(groq_llm2)
    risk_assessor = create_risk_assessor(groq_llm3)
    report_generator = create_report_generator(groq_llm1)

    # Create tasks
    market_task = create_market_analysis_task(market_analyst)
    sentiment_task = create_sentiment_task(sentiment_analyst)
    risk_task = create_risk_task(risk_assessor)
    report_task = create_report_task(report_generator)

    # run crew
    crew = Crew(
        agents=[market_analyst, sentiment_analyst,risk_assessor, report_generator],
        tasks=[market_task, sentiment_task,risk_task,report_task]
    )
    
    result = crew.kickoff()
    print("📊 Investment Report:\n", result)

if __name__ == "__main__":
    main()
# MarketMinds: AI-Powered Investment Research Crew


MarketMinds is an **Agentic AI**-powered project built with **crewAI**, designed to analyze financial markets using multiple intelligent agents. This system performs technical and sentiment analysis, assesses risks, and generates structured investment reports.

## 🔹 Features
MarketMinds consists of four specialized AI agents working together:

1. **Market Analysis Agent**
   - Performs **technical analysis** using:
     - 50-day and 200-day Simple Moving Averages (SMAs)
     - 14-day Relative Strength Index (RSI)

2. **Sentiment Analysis Agent**
   - Analyzes **stock sentiment** from the latest news headlines
   - Uses **Serper API** custom tool to fetch data and perform sentiment analysis

3. **Risk Assessment Agent**
   - Assesses **financial risks** based on market data and risk metrics
   - Utilizes a custom **risk assessment tool** to calculate stock risk metrics using **Alpha Vantage** data

4. **Report Generator Agent**
   - Generates **structured investment reports**
   - Consolidates output from Market Analysis, Sentiment Analysis, and Risk Assessment agents

## 🧠 LLMs Used
MarketMinds leverages multiple **Groq LLMs** for various tasks:
- **groq_llm1**: `groq/llama3-70b-8192` (Max tokens: 500)
- **groq_llm2**: `groq/gemma2-9b-it` (Max tokens: 700)
- **groq_llm3**: `groq/deepseek-r1-distill-qwen-32b` (Max tokens: 800)


## 🛠 Technologies Used
- **crewAI** (Agentic AI framework)
- **Python** (Backend & logic)
- **Serper API** (Stock sentiment analysis)
- **Alpha Vantage API** (Market data retrieval)
- **Groq LLMs** (AI-powered analysis and reporting)
- **Streamlit** (To create UI)

## 📜 License
This project is licensed under the **MIT License**.


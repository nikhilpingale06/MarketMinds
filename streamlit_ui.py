import streamlit as st
import os
from crewai import Crew, LLM
from agents.market_analyst import *
from agents.sentiment_analysis import *
from agents.risk_assessment import *
from agents.report_generator import *
from tasks.agent_tasks import *
from utils.api_keys import *


st.markdown("""
    <style>
        body { background-color: #0e1117; color: white; }
        .stTextInput, .stPassword, .stButton>button { border-radius: 8px; }
        
        /* Glowing Header Effect */
        @keyframes glow {
            0% { text-shadow: 0 0 10px #03DAC6; }
            50% { text-shadow: 0 0 20px #BB86FC; }
            100% { text-shadow: 0 0 10px #03DAC6; }
        }
        
        .title {
            text-align: center; 
            font-size: 42px; 
            font-weight: bold; 
            color: #03DAC6;
            animation: glow 2s infinite alternate;
            padding-bottom: 5px;
        }
        
        .subtitle {
            text-align: center; 
            font-size: 20px; 
            font-weight: lighter; 
            color: #BB86FC; 
            padding-bottom: 20px;
        }

        /* Stock Ticker Animation */
        @keyframes ticker {
            0% { opacity: 0.6; transform: translateX(-5px); }
            50% { opacity: 1; transform: translateX(5px); }
            100% { opacity: 0.6; transform: translateX(-5px); }
        }
        
        .stock-ticker { 
            color: #FFD700; 
            font-weight: bold; 
            text-align: center; 
            font-size: 22px; 
            animation: ticker 2s infinite alternate; 
        }
        
        /* Sidebar Customization */
        .sidebar .sidebar-content { background: #1e1e2e; color: white; border-radius: 10px; }

        /* Card Styling */
        .stock-card {
            padding: 15px; 
            border-radius: 10px; 
            background: linear-gradient(135deg, #1e293b, #2a3a53);
            color: white; 
            box-shadow: 0px 0px 10px rgba(0, 255, 255, 0.3);
            text-align: center;
            font-size: 18px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<p class="title">📊 MarketMinds: AI Stock Analysis</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🚀 Your AI-powered investment assistant</p>', unsafe_allow_html=True)


st.sidebar.header("🔑 API Configuration")
with st.sidebar.expander("🔽 Set API Keys"):
    alpha_vantage_key = st.text_input("Alpha Vantage API Key", type="password")
    serper_api_key = st.text_input("Serper API Key", type="password")
    groq_api_key = st.text_input("Groq API Key", type="password")

st.sidebar.header("📈 Stock Selection")
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL, TSLA)")
start_analysis = st.sidebar.button("🚀 Start Analysis")

if stock_symbol:
    st.markdown(f'<p class="stock-ticker">Analyzing Stock: {stock_symbol} 📊</p>', unsafe_allow_html=True)

if start_analysis:
    if not (alpha_vantage_key and serper_api_key and groq_api_key):
        st.sidebar.error("❌ Please provide all API keys!")
    else:
        st.sidebar.success("✅ API Keys Set Successfully")

        os.environ["ALPHA_VANTAGE_API_KEY"] = alpha_vantage_key
        os.environ["SERPER_API_KEY"] = serper_api_key
        os.environ["GROQ_API_KEY"] = groq_api_key

        st.markdown("🤖 **AI Processing... Please Wait** ⏳")


        groq_llm1 = LLM(model="groq/llama3-70b-8192", max_tokens=700)
        groq_llm2 = LLM(model="groq/gemma2-9b-it", max_tokens=700)
        groq_llm3 = LLM(model="groq/llama-3.3-70b-versatile", max_tokens=800)

        market_analyst = create_market_analyst(groq_llm1)
        sentiment_analyst = create_sentiment_analyst(groq_llm2)
        risk_assessor = create_risk_assessor(groq_llm3)
        report_generator = create_report_generator(groq_llm1)

        market_task = create_market_analysis_task(market_analyst, stock_symbol)
        sentiment_task = create_sentiment_task(sentiment_analyst, stock_symbol)
        risk_task = create_risk_task(risk_assessor, stock_symbol)
        report_task = create_report_task(report_generator)

        # Run 
        crew = Crew(
            agents=[market_analyst, sentiment_analyst, risk_assessor, report_generator],
            tasks=[market_task, sentiment_task, risk_task, report_task]
        )
        result = crew.kickoff()

        st.success("✅ Analysis Complete!")
        st.subheader("📄 Investment Report")

        col1, col2 = st.columns(2)

        col1.markdown('<div class="stock-card"><h4>📊 Market Insights</h4></div>', unsafe_allow_html=True)

        # Display Analysis
        if hasattr(result, "dict"):
            result_dict = result.dict()
        elif hasattr(result, "__dict__"):
            result_dict = vars(result)
        else:
            result_dict = result

        if isinstance(result_dict, dict) and "raw" in result_dict:
            st.markdown(result_dict["raw"])
        else:
            st.warning("⚠️ No structured report found. Debugging output:")
            st.write(result_dict)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #BB86FC;'>💡 *Developed with CrewAI – Smarter Investment Decisions, Powered by AI!*</p>", unsafe_allow_html=True)

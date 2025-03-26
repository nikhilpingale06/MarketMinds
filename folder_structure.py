import os

# Define the folder structure
folders = [
    "agents",
    "data",
    "data/stock_data",
    "data/sentiment_logs",
    "models",
    "utils",
    "app",
    "tests"
]

# Define the files to be created
files = {
    "agents/market_analyst.py": "# Market Analyst Agent",
    "agents/sentiment_analysis.py": "# Sentiment Analysis Agent",
    "agents/ml_predictor.py": "# Machine Learning Predictor",
    "agents/risk_assessment.py": "# Risk Assessment Agent",
    "agents/report_generator.py": "# Investment Report Generator",

    "models/lstm_model.py": "# LSTM-based Market Trend Prediction",
    "models/xgboost_model.py": "# XGBoost Model for Price Forecasting",

    "utils/data_fetcher.py": "# Fetch financial data from APIs",
    "utils/api_keys.py": "# Store API keys (Do not commit to GitHub)",
    "utils/logger.py": "# Logging utilities",

    "app/api.py": "# FastAPI backend for investment reports",
    "app/streamlit_ui.py": "# Streamlit web UI for financial insights",

    "tests/test_agents.py": "# Unit tests for CrewAI agents",
    "tests/test_models.py": "# Unit tests for ML models",
    
    ".gitignore": "env/\n__pycache__/\ndata/\nlogs/\n",
    "requirements.txt": "crewai\nlangchain\nopenai\nyfinance\nalpha_vantage\nnewsapi-python\nfastapi\nstreamlit\nscikit-learn\ntensorflow\npandas\nnumpy\nmatplotlib\n",
    "README.md": "# QuantCrew: AI-Powered Investment Research Crew",
    "main.py": "# Entry point for running the full AI crew",
    ".env": "# Store environment variables (API keys, config)"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with initial content
for file, content in files.items():
    with open(file, "w") as f:
        f.write(content)

print("✅ Project structure created successfully!")

# Store API keys (Do not commit to GitHub)

import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

STOCK_SYMBOL = 'TSLA'  
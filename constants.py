import os
from dotenv import load_dotenv

load_dotenv()

SYMBOL_COMPANY = {
    "TSLA": "Tesla Inc",
    "AAPL": "Apple Inc",
    "NVDA": "NVIDIA Corporation",
}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.getenv("FROM_NUMBER")
TO_NUMBER = os.getenv("TO_NUMBER")
EMOJI_UP = "🔺"
EMOJI_DOWN = "🔻"

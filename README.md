# stock-news-alert

## About The Project

This Python application is designed to deliver stock market updates and news alerts via SMS for selected companies. It integrates with several APIs: Alpha Vantage API for fetching stock data, News API for retrieving headlines and Twilio API for sending SMS notifications.

## Built With

- Python
- requests
- Alpha Vantage API
- News API
- Twilio API

## Getting Started

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/fsosn/stock-news-alert.git
   ```
2. Create a virtual environment and install dependencies

   ```sh
   python -m venv .venv
   .venv/Scripts/activate
   pip install -r requirements.txt
   ```

3. Create .env file in the root directory and set up environmental variables
   ```sh
   STOCK_API_KEY = ""
   NEWS_API_KEY = ""
   TWILIO_ACCOUNT_SID = ""
   TWILIO_AUTH_TOKEN = ""
   FROM_NUMBER= ""
   TO_NUMBER= ""
   ```
4. Run the program
   ```sh
   python main.py
   ```

## Example message
```
TSLA: 🔻 4.02%
• Can Tesla Inc (NASDAQ:TSLA) Become the Best AI Value Stock?
• Is Tesla Inc (NASDAQ:TSLA) an Overbought AI Stock in 2024?
• Can Tesla Inc (NASDAQ:TSLA) Shares Rise After the Robotaxi Event?

AAPL: 🔺 0.06%
• Is Apple Inc (NASDAQ:AAPL) Aswath Damodaran’s Best AI Stock Pick?
• Hedge Funds Are Crazy About Apple Inc. (AAPL)
• Is Apple Inc. (NASDAQ:AAPL) The Most Undervalued AI Stock to Buy Now?

NVDA: 🔻 2.61%
• NYU’s Aswath Damodaran Calls NVIDIA Corporation (NASDAQ:NVDA) a ‘Money Machine’
• AI Boom Lifted NVIDIA Corporation (NVDA) by 345%
• NVIDIA Corporation (NVDA) Jumped on Booming Demand for AI Products
```

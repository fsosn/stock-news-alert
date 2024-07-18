# stock-news-alert

## About The Project

This Python application is designed to deliver stock market updates and news alerts via SMS for selected companies. It integrates with several APIs: Alpha Vantage for fetching stock data, News API for retrieving headlines, and Twilio for sending SMS notifications.

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

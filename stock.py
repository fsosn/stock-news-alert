import requests
from constants import STOCK_API_KEY, STOCK_ENDPOINT


def get_stock_change_percent(stock_symbol: str):
    data = _fetch_stock_data(stock_symbol)

    time_series_dict = data["Time Series (Daily)"]
    last_two_days = [value for (_, value) in time_series_dict.items()][:2]
    (close_today, close_yesterday) = (float(day["4. close"]) for day in last_two_days)

    change_percent = _calculate_change_percent(close_today, close_yesterday)

    return change_percent


def _fetch_stock_data(stock_symbol: str):
    request_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": STOCK_API_KEY,
    }
    response = requests.get(STOCK_ENDPOINT, params=request_params)

    return response.json()


def _calculate_change_percent(close_today: float, close_yesterday: float):
    return round(((close_today - close_yesterday) / close_yesterday) * 100, 2)

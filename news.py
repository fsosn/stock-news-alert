import requests
from constants import NEWS_API_KEY, NEWS_ENDPOINT


def get_news(company_name: str):
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": company_name,
        "searchIn": "title",
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"][:3]

    return [article["title"] for article in articles]

import os
import json
import requests
from app.config import NEWS_API_KEY


def fetch_news():
    url = "https://newsdata.io/api/1/news"
    params = {"apikey": NEWS_API_KEY, "q": "technology", "language": "en"}

    response = requests.get(url, params=params)
    data = response.json()

    os.makedirs("data", exist_ok=True)
    with open("data/news_response.json", "w") as f:
        json.dump(data, f, indent=2)

    return data

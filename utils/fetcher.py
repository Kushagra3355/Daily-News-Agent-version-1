import os
import json
import requests
from app.config import NEWS_API_KEY


def fetch_news():
    url = "https://newsdata.io/api/1/news"
    params = {"apikey": NEWS_API_KEY, "q": "technology", "language": "en"}

    all_results = []

    for _ in range(3):
        response = requests.get(url, params=params)
        data = response.json()

        all_results.extend(data.get("results", []))

        next_page = data.get("nextPage")
        if not next_page:
            break
        params["page"] = next_page

    combined_data = {
        "status": "ok",
        "totalResults": len(all_results),
        "results": all_results,
    }

    os.makedirs("data", exist_ok=True)
    with open("data/news_response.json", "w") as f:
        json.dump(combined_data, f, indent=2)

    return combined_data

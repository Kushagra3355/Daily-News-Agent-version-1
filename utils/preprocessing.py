def preprocess_news(api_response: dict):
    articles = api_response.get("results", [])

    cleaned = []
    for a in articles:
        cleaned.append(
            {
                "title": a.get("title"),
                "description": a.get("description"),
                "category": a.get("category"),
                "source": a.get("source_name"),
                "date": a.get("pubDate"),
                "url": a.get("link"),
            }
        )

    return cleaned

def preprocess_news(api_response: dict, limit: int = 5):
    articles = api_response.get("results", [])[:limit]

    cleaned = []
    for a in articles:
        cleaned.append({
            "title": a.get("title"),
            "description": a.get("description"),
            "category": a.get("category"),
            "source": a.get("source_name"),
            "date": a.get("pubDate"),
            "url": a.get("link")
        })

    return cleaned

def filter_news_by_category(news_json: dict, category: str) -> dict:
    """
    Filters summarized news based on category.
    """

    filtered = [
        article
        for article in news_json.get("summaries", [])
        if category in article.get("category", [])
    ]

    return {
        "category": category,
        "total_articles": len(filtered),
        "summaries": filtered,
    }

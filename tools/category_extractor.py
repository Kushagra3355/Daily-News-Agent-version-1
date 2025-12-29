def get_all_categories(news_json: dict) -> dict:
    categories = set()

    for article in news_json.get("summaries", []):
        for cat in article.get("category", []):
            categories.add(cat.lower())

    return {"total_categories": len(categories), "categories": sorted(list(categories))}

from utils.fetcher import fetch_news
from utils.preprocessing import preprocess_news
from agents.summerizer_agent import run_summarizer
import json, os


def run_daily_job():

    print("Getting the News from API...")
    api_resp = fetch_news()
    print("Proprocessing the data...")
    news_data = preprocess_news(api_response=api_resp)
    print("Summarizing the data...")
    summary = run_summarizer(news_data=news_data)

    # Save summary to JSON
    os.makedirs("data", exist_ok=True)
    with open("data/news_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("Saved to JSON format.")

    return summary

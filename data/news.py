import requests
from config import NEWS_API_KEY

def get_top_headlines():
    try:
        url = f"https://newsapi.org/v2/top-headlines?category=business&language=en&pageSize=3&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])
        return [{"title": a["title"], "url": a["url"]} for a in articles]
    except Exception as e:
        print("News API error:", e)
        return []

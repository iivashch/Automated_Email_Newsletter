import requests
try:
    from config import NEWS_API_KEY
except ImportError:
    from config_remote import NEWS_API_KEY

# Function to fetch the latest business news headlines
def get_top_business_headlines():
    try:
        url = f"https://newsapi.org/v2/top-headlines?category=business&language=en&pageSize=3&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])
        return [{
            "title": a["title"], 
            "description": a.get("description", ""), 
            "url": a["url"], 
            } for a in articles]
    except Exception as e:
        print("News API error:", e)
        return []

# Function to fetch the latest general news headlines
def get_top_general_headlines():
    try:
        url = f"https://newsapi.org/v2/top-headlines?category=general&language=en&pageSize=3&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])
        return [{
            "title": a["title"], 
            "description": a.get("description", ""), 
            "url": a["url"], 
            } for a in articles]
    except Exception as e:
        print("News API error:", e)
        return []
    
def get_top_technology_headlines():
    try:
        url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&pageSize=3&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])
        return [{
            "title": a["title"], 
            "description": a.get("description", ""), 
            "url": a["url"], 
            } for a in articles]
    except Exception as e:
        print("News API error:", e)
        return []
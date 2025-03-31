import requests

def get_quote_of_the_day():
    try:
        response = requests.get("https://zenquotes.io/api/today")
        if response.status_code == 200:
            data = response.json()
            quote = f"{data[0]['q']} — {data[0]['a']}"
            return quote
    except Exception as e:
        print("Quote API error:", e)
    return "In the middle of difficulty lies opportunity. — Albert Einstein"

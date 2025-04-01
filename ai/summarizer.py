from openai import OpenAI
try:
    from config import OPENAI_API_KEY
except ImportError:
    from config_remote import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_changes(economic_data, news_articles):
    
    #economic indicators are combined together for chat gpt to summarize
    econ_summary = ""
    for name, df in economic_data.items():
        try:
            value = df.iloc[-1].values[0]
            econ_summary += f"{name}: {value:.2f}\n"
        except Exception:
            econ_summary += f"{name}: unavailable\n"
    
    # the three types of news articles are combined together for chat gpt to summarize
    news_summary = ""
    for n in ["business", "general", "technology"]:
        for article in news_articles[n]:
            news_summary += f"{article['title']}: {article['description']}\n"

    prompt = (
        "Summarize the following economic indicators and news headlines in a short, professional "
        "daily update about the state of the economy.\n\n"
        f"Economic Data:\n{econ_summary}\n"
        f"News:\n{news_summary}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("🔴 OpenAI API Error:", e)
        return "Summary unavailable."

from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_changes(economic_data, news_articles):
    econ_summary = ""
    for name, df in economic_data.items():
        try:
            value = df.iloc[-1].values[0]
            econ_summary += f"{name}: {value:.2f}\n"
        except Exception:
            econ_summary += f"{name}: unavailable\n"

    news_summary = "\n".join([f"{article['title']}" for article in news_articles])

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

# config_template.py
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
YOUR_EMAIL = "you@example.com"
YOUR_APP_PASSWORD = "your_app_password"
MAIN_RECIPIENT = "recipient@example.com"
RECIPIENT_EMAILS = [
    "person1@example.com",
    "person2@example.com",
    "person3@example.com"
    ]


STOCKS = ["AAPL", "MSFT", "TSLA", "^GSPC", "^IXIC"]

FRED_INDICATORS = {
    'Inflation Rate (CPI)': 'CPIAUCSL',
    'Interest Rate (Fed Funds)': 'DFF',
    'EUR/USD Exchange Rate': 'DEXUSEU'
}

NEWS_API_KEY = "your_news_api_key_here"
OPENAI_API_KEY = "your_openai_api_key_here"

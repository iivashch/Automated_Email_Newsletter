import os

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
YOUR_EMAIL = os.getenv("YOUR_EMAIL")
YOUR_APP_PASSWORD = os.getenv("YOUR_APP_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

STOCKS = ["AAPL", "MSFT", "TSLA", "^GSPC", "^IXIC"]

FRED_INDICATORS = {
    'Inflation Rate (CPI)': 'CPIAUCSL',
    'Interest Rate (Fed Funds)': 'DFF',
    'EUR/USD Exchange Rate': 'DEXUSEU'
}

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

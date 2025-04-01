import yfinance as yf
try:
    from config import STOCKS
except ImportError:
    from config_remote import STOCKS

def get_stock_data():
    results = []
    for ticker in STOCKS:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d")
        info = stock.info

        if hist.empty:
            continue

        latest = hist['Close'].iloc[-1]
        previous = hist['Close'].iloc[-2]
        change = latest - previous
        pct_change = (change / previous) * 100

        volume = info.get('volume')
        volume_str = f"{volume:,}" if isinstance(volume, (int, float)) else "N/A"

        pe_ratio = info.get('trailingPE', 'N/A')
        market_cap = info.get('marketCap')
        market_cap_str = f"{market_cap:,}" if isinstance(market_cap, (int, float)) else "N/A"

        results.append({
            "ticker": ticker,
            "price": latest,
            "change": change,
            "percent": pct_change,
            "volume": volume_str,
            "pe": pe_ratio,
            "market_cap": market_cap_str
        })
    return results

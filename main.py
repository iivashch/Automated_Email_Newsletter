from data.stock_data import get_stock_data
from data.economic_data import get_economic_data, calculate_percent_changes
from data.quote import get_quote_of_the_day
from data.news import get_top_headlines
from ai.summarizer import summarize_changes
from dashboard_builder import build_html_dashboard
from emailer import send_html_email
from data.chart_plotter import plot_economic_data

def main():
    stock_data = get_stock_data()
    econ_data = get_economic_data()
    econ_changes, econ_values = calculate_percent_changes(econ_data)
    plot_economic_data(econ_data)
    quote = get_quote_of_the_day()
    news_articles = get_top_headlines()
    summary = summarize_changes(econ_data, news_articles)

    html_body = build_html_dashboard(stock_data, econ_changes, econ_values, quote, news_articles, summary)
    send_html_email("📤 Daily Financial Dashboard", html_body, "output/economic_indicators.png")

if __name__ == "__main__":
    main()

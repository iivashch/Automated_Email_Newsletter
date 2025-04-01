import markdown

def build_html_dashboard(stock_data, econ_changes, econ_values, quote, news_articles, summary, style='gs'):
    base_css = """
    <style>
        @media only screen and (max-width: 600px) {
            body { padding: 10px !important; }
            .container { padding: 15px !important; }
            table { font-size: 12px !important; }
            h2, h3 { font-size: 18px !important; text-align: center !important; }
            td, th { padding: 6px !important; }
        }
    </style>
    """

    quote_html = f"""
    <div style='background-color:#f9f9f9; padding:15px 20px; border-left:5px solid #c4a000; margin:30px 0; font-style:italic; color:#003366;'>
        {quote}
    </div>
    """

    stock_rows = ""
    for entry in stock_data:
        color = "green" if entry['change'] >= 0 else "red"
        stock_rows += f"""
        <tr style='border-bottom:1px solid #ddd;'>
            <td style='padding:8px;'>{entry['ticker']}</td>
            <td style='text-align:right;'>${entry['price']:.2f}</td>
            <td style='text-align:right; color:{color};'>{entry['change']:+.2f} ({entry['percent']:+.2f}%)</td>
            <td style='text-align:right;'>{entry['volume']}</td>
            <td style='text-align:right;'>{entry['pe']}</td>
            <td style='text-align:right;'>{entry['market_cap']}</td>
        </tr>
        """

    stock_table = f"""
    <table style='width:100%; border-collapse:collapse; font-size:14px;'>
        <tr style='background-color:#1a1a1a; color:white;'>
            <th style='padding:8px;'>Stock</th><th>Price</th><th>Change</th><th>Volume</th><th>P/E</th><th>Market Cap</th>
        </tr>
        {stock_rows}
    </table>
    """

    econ_rows = ""
    for name in econ_changes:
        current = econ_values.get(name, "N/A")
        change = econ_changes.get(name, 0.0)

        if "Fed Funds" in name or "Interest" in name:
            current_str = f"{current:.2f}%"
        elif "Exchange" in name:
            current_str = f"{current:.4f} USD"
        elif "Inflation" in name or "CPI" in name:
            current_str = f"{current:.2f}"
        else:
            current_str = f"{current:.2f}"

        econ_rows += f"""
        <tr style='border-bottom:1px solid #ddd;'>
            <td style='padding:8px;'>{name}</td>
            <td style='text-align:right;'>{current_str}</td>
            <td style='text-align:right;'>{change:+.2f}%</td>
        </tr>
        """

    econ_table = f"""
    <table style='width:100%; border-collapse:collapse; font-size:14px; margin-top:20px;'>
        <tr style='background-color:#1a1a1a; color:white;'>
            <th style='padding:8px;'>Indicator</th><th>Current Value</th><th>1-Year Change</th>
        </tr>
        {econ_rows}
    </table>
    """
    #business news articles
    business_news_html = "<ul>"
    for article in news_articles["business"]:
        business_news_html += f"""
        <li style='margin-bottom:10px;'>
            <strong><a href='{article['url']}' style='color:#003366;'>{article['title']}</a></strong><br>
            <span style='font-size:13px; color:#444;'>{article.get('description', '')}</span>
        </li>
        """
    business_news_html += "</ul>"

    #general news articles
    general_news_html = "<ul>"
    for article in news_articles["general"]:
        general_news_html += f"""
        <li style='margin-bottom:10px;'>
            <strong><a href='{article['url']}' style='color:#003366;'>{article['title']}</a></strong><br>
            <span style='font-size:13px; color:#444;'>{article.get('description', '')}</span>
        </li>
        """
    general_news_html += "</ul>"

    #technology news articles
    technology_news_html = "<ul>"
    for article in news_articles["technology"]:
        technology_news_html += f"""
        <li style='margin-bottom:10px;'>
            <strong><a href='{article['url']}' style='color:#003366;'>{article['title']}</a></strong><br>
            <span style='font-size:13px; color:#444;'>{article.get('description', '')}</span>
        </li>
        """
    technology_news_html += "</ul>"

    html = f"""
    <html>
    <head>{base_css}</head>
    <body style='background-color:#f5f5f5; padding:40px; font-family:"Helvetica Neue", Arial, sans-serif; color:#333;'>
        <div class='container' style='max-width:800px; margin:auto; background:white; padding:30px; box-shadow:0 0 10px rgba(0,0,0,0.1);'>
            <h2 style='color:#003366; text-align:center;'>📈 Daily Financial Dashboard</h2>
            {quote_html}
            <h3 style='color:#003366;'>📊 Stock Summary</h3>
            {stock_table}
            <h3 style='color:#003366; margin-top:40px;'>🏛️ Key Economic Indicators</h3>
            {econ_table}
            <h3 style='color:#003366; margin-top:40px;'>📰 Business News</h3>
            {business_news_html}
            <h3 style='color:#003366; margin-top:40px;'>🌎 General News</h3>
            {general_news_html}
            <h3 style='color:#003366; margin-top:40px;'>🖥️ Technology News</h3>
            {technology_news_html}
            <h3 style='color:#003366; margin-top:40px;'>🧠 Summary</h3>
            <div style='margin-top:10px;'>{markdown.markdown(summary)}</div>
            <h3 style='color:#003366; margin-top:40px;'>📉 Economic Trend Chart</h3>
            <div style='text-align:center;'>
                <img src="cid:chart" width="600" style="border:1px solid #ccc; padding:5px; margin-top:10px; max-width:100%; height:auto;">
            </div>
        </div>
    </body>
    </html>
    """
    return html
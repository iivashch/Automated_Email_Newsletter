import markdown

def build_html_dashboard(stock_data, econ_changes, econ_values, quote, news_articles, summary, style='gs'):
    base_css = """<style>
    body {
      font-family: "Helvetica Neue", Arial, sans-serif;
      background-color: #f5f5f5;
      color: #333;
      padding: 40px;
      margin: 0;
    }
    .container {
      max-width: 800px;
      margin: auto;
      background: white;
      padding: 30px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    h2, h3 {
      text-align: center;
      color: #003366;
    }
    .quote {
      background-color: #f9f9f9;
      padding: 15px 20px;
      border-left: 5px solid #c4a000;
      margin: 30px 0;
      font-style: italic;
      color: #003366;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
      margin-top: 20px;
    }
    th, td {
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: #1a1a1a;
      color: white;
    }
    tr:nth-child(even) {
      background-color: #f9f9f9;
    }
    .positive { color: green; }
    .negative { color: red; }
    img.chart {
      display: block;
      max-width: 100%;
      height: auto;
      margin: 20px auto;
      border: none;
    }
    ul {
      padding-left: 20px;
    }
    li {
      margin-bottom: 10px;
    }
    li a {
      color: #003366;
      font-weight: bold;
      text-decoration: none;
    }
    li span {
      font-size: 13px;
      color: #444;
    }
    @media only screen and (max-width: 600px) {
      body { padding: 10px !important; }
      .container { padding: 15px !important; }
      table { font-size: 12px !important; }
      h2, h3 { font-size: 18px !important; }
      td, th { padding: 6px !important; }
    }
    </style>"""

    quote_html = f"<div class='quote'>{quote}</div>"

    stock_rows = ""
    for entry in stock_data:
        change_class = "positive" if entry['change'] >= 0 else "negative"
        stock_rows += f"""
        <tr>
            <td>{entry['ticker']}</td>
            <td style='text-align:right;'>${entry['price']:.2f}</td>
            <td style='text-align:right;' class='{change_class}'>{entry['change']:+.2f} ({entry['percent']:+.2f}%)</td>
            <td style='text-align:right;'>{entry['volume']}</td>
            <td style='text-align:right;'>{entry['pe']}</td>
            <td style='text-align:right;'>{entry['market_cap']}</td>
        </tr>
        """

    stock_table = f"""
    <table>
        <tr><th>Stock</th><th>Price</th><th>Change</th><th>Volume</th><th>P/E</th><th>Market Cap</th></tr>
        {stock_rows}
    </table>
    """

    econ_rows = ""
    for name in econ_changes:
        current = econ_values.get(name, "N/A")
        change = econ_changes.get(name, 0.0)

        # Format current value
        if "Fed Funds" in name or "Interest" in name:
            current_str = f"{current:.2f}%"
        elif "Exchange" in name:
            current_str = f"{current:.4f} USD"
        elif "Inflation" in name or "CPI" in name:
            current_str = f"{current:.2f}"
        else:
            current_str = f"{current:.2f}"

        # Determine color class
        change_class = "positive" if change > 0 else "negative" if change < 0 else ""

        econ_rows += f"""
        <tr>
            <td>{name}</td>
            <td style='text-align:right;'>{current_str}</td>
            <td style='text-align:right;' class='{change_class}'>{change:+.2f}%</td>
        </tr>
        """

    econ_table = f"""
    <table>
        <tr><th>Indicator</th><th>Current Value</th><th>1-Year Change</th></tr>
        {econ_rows}
    </table>
    """

    def format_news_list(articles):
        html = "<ul>"
        for article in articles:
            html += f"""
            <li>
                <a href='{article['url']}'>{article['title']}</a><br>
                <span>{article.get('description', '')}</span>
            </li>"""
        html += "</ul>"
        return html

    business_news_html = format_news_list(news_articles["business"])
    general_news_html = format_news_list(news_articles["general"])
    technology_news_html = format_news_list(news_articles["technology"])

    summary_html = markdown.markdown(summary)

    html = f"""
    <html>
    <head>{base_css}</head>
    <body>
        <div class="container">
            <h2>📈 Daily Dashboard</h2>
            {quote_html}
            <h3>📊 Stock Summary</h3>
            {stock_table}
            <h3>🏛️ Key Economic Indicators</h3>
            {econ_table}
            <h3>📰 Business News</h3>
            {business_news_html}
            <h3>🌎 General News</h3>
            {general_news_html}
            <h3>🖥️ Technology News</h3>
            {technology_news_html}
            <h3>🧠 Summary</h3>
            <div>{summary_html}</div>
            <h3>📉 Economic Trend Chart</h3>
            <div style='text-align:center;'>
                <img src="cid:chart" class="chart" alt="Economic Trends Chart">
            </div>
        </div>
    </body>
    </html>
    """
    return html

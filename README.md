# Modulated Automated Email

[![Dashboard Status](https://github.com/iivashch/Automated_Email_Newsletter/actions/workflows/daily.yml/badge.svg)](https://github.com/iivashch/Automated_Email_Newsletter/actions)



Automate custom newsletter for every morning, including relevant financial indicators, stocks, and news, as well as get a summary of the above.

API Calls:
* Quote of the day is taken from [ZenQuotes](https://zenquotes.io/) which does not require API key.
* Stock data is obtained using *yfinance* python library.
* Economic data is received from a [FRED](https://fred.stlouisfed.org/) using python's *datareader* library.
* Financial (or any other category of) news are obtained using [NewsAPI](https://newsapi.org/), via their free Developer API; consult their pricing page for details.
* Summary is done using an API call to chat [GPT 4o-mini](https://openai.com/api/).
* Economic Trend charts are built using FRED data, as well.

Python Dependencies List: yfinance pandas matplotlib requests markdown openai pandas_datareader


Example:

<img width="860" alt="Screenshot 2025-03-31 at 17 45 53" src="https://github.com/user-attachments/assets/596d2d7a-9e81-4040-ae34-a160dc13dd82" />

<img width="851" alt="Screenshot 2025-03-31 at 17 46 04" src="https://github.com/user-attachments/assets/3217f581-de13-4886-97de-f021a6dae6b9" />


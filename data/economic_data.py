import pandas_datareader.data as web
from datetime import datetime
import pandas as pd
from config import FRED_INDICATORS

def get_economic_data():
    end = datetime.today()
    start = end - pd.DateOffset(years=1)
    data = {}
    for name, code in FRED_INDICATORS.items():
        df = web.DataReader(code, 'fred', start, end)
        data[name] = df
    return data

def calculate_percent_changes(data):
    changes = {}
    values = {}
    for name, df in data.items():
        start = df.iloc[0].values[0]
        end = df.iloc[-1].values[0]
        change = ((end - start) / start) * 100
        changes[name] = change
        values[name] = end
    return changes, values

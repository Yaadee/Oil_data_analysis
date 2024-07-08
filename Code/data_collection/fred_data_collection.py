import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

# Function to get data from FRED
def get_fred_data(ticker, start_date, end_date):
    data = web.DataReader(ticker, 'fred', start_date, end_date)
    return data

# Define the date range
start_date = '1987-05-20'
end_date = datetime.now().strftime('%Y-%m-%d')

# Collect data
gdp = get_fred_data('GDP', start_date, end_date)
inflation = get_fred_data('CPIAUCSL', start_date, end_date)
unemployment = get_fred_data('UNRATE', start_date, end_date)
exchange_rate = get_fred_data('DEXUSEU', start_date, end_date)

# Save data to CSV

gdp.to_csv('Inputs/data/raw_data/gdp.csv')
inflation.to_csv('Inputs/data/raw_data/inflation.csv')
unemployment.to_csv('Inputs/data/raw_data/unemployment.csv')
exchange_rate.to_csv('Inputs/data/raw_data/exchange_rate.csv')

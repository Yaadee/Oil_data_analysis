import pandas_datareader.data as web
from datetime import datetime

# Get inflation data (Consumer Price Index for All Urban Consumers: All Items in U.S. City Average)
inflation_data = web.DataReader('CPIAUCSL', 'fred', start='1970-01-01', end=datetime.now())

# Save inflation data to CSV
inflation_data.to_csv('Inputs/data/raw_data/inflation_data.csv')
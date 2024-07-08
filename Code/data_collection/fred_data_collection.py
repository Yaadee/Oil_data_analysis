# import pandas as pd
# import pandas_datareader.data as web
# from datetime import datetime

# # Function to get data from FRED
# def get_fred_data(ticker, start_date, end_date):
#     data = web.DataReader(ticker, 'fred', start_date, end_date)
#     return data

# # Define the date range
# start_date = '1987-05-20'
# end_date = datetime.now().strftime('%Y-%m-%d')

# # Collect data
# gdp = get_fred_data('GDP', start_date, end_date)
# inflation = get_fred_data('CPIAUCSL', start_date, end_date)
# unemployment = get_fred_data('UNRATE', start_date, end_date)
# exchange_rate = get_fred_data('DEXUSEU', start_date, end_date)
# # Global Economic Policy Uncertainty Index
# gepu_data = get_fred_data('GEPUCURRENT', start_date, end_date)
# # Equity Market Volatility Tracker
# emv_data = get_fred_data('EMVELECTGOVRN', start_date, end_date)
# # OPEC Policies
# opec_data = get_fred_data('COOTHERZ315', start_date, end_date)

# # Save data to CSV
# gdp.to_csv('Inputs/data/raw_data/gdp.csv')
# inflation.to_csv('Inputs/data/raw_data/inflation.csv')
# unemployment.to_csv('Inputs/data/raw_data/unemployment.csv')
# exchange_rate.to_csv('Inputs/data/raw_data/exchange_rate.csv')
# gepu_data.to_csv('Inputs/data/raw_data/global_economic_policy_uncertainty.csv')
# emv_data.to_csv('Inputs/data/raw_data/equity_market_volatility.csv')
# opec_data.to_csv('Inputs/data/raw_data/opec_policies.csv')

# print("Data fetched and saved.")


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
brent_oil_prices = web.DataReader('DCOILBRENTEU', 'fred', start_date, end_date)
gdp = get_fred_data('GDP', start_date, end_date)
inflation = get_fred_data('CPIAUCSL', start_date, end_date)
unemployment = get_fred_data('UNRATE', start_date, end_date)
exchange_rate = get_fred_data('DEXUSEU', start_date, end_date)
gepu_data = get_fred_data('GEPUCURRENT', start_date, end_date)
emv_data = get_fred_data('EMVELECTGOVRN', start_date, end_date)
opec_data = get_fred_data('COOTHERZ315', start_date, end_date)

# Save raw data to CSV
brent_oil_prices.to_csv('Inputs/data/raw_data/BrentOilPrices.csv')
gdp.to_csv('Inputs/data/raw_data/gdp.csv')
inflation.to_csv('Inputs/data/raw_data/inflation.csv')
unemployment.to_csv('Inputs/data/raw_data/unemployment.csv')
exchange_rate.to_csv('Inputs/data/raw_data/exchange_rate.csv')
gepu_data.to_csv('Inputs/data/raw_data/global_economic_policy_uncertainty.csv')
emv_data.to_csv('Inputs/data/raw_data/equity_market_volatility.csv')
opec_data.to_csv('Inputs/data/raw_data/opec_policies.csv')

print("Data collection completed and saved to CSV.")

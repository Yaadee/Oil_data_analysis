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
# gepu_data = get_fred_data('GEPUCURRENT', start_date, end_date)
# emv_data = get_fred_data('EMVELECTGOVRN', start_date, end_date)
# opec_data = get_fred_data('COOTHERZ315', start_date, end_date)

# # Save raw data to CSV
# gdp.to_csv('Inputs/data/raw_data/gdp.csv')
# inflation.to_csv('Inputs/data/raw_data/inflation.csv')
# unemployment.to_csv('Inputs/data/raw_data/unemployment.csv')
# exchange_rate.to_csv('Inputs/data/raw_data/exchange_rate.csv')
# gepu_data.to_csv('Inputs/data/raw_data/global_economic_policy_uncertainty.csv')
# emv_data.to_csv('Inputs/data/raw_data/equity_market_volatility.csv')
# opec_data.to_csv('Inputs/data/raw_data/opec_policies.csv')

# # Load the data and ensure the date column is consistently named 'DATE'
# brent_oil_prices = pd.read_csv('Inputs/data/raw_data/BrentOilPrices.csv', parse_dates=['Date'])
# brent_oil_prices.rename(columns={'Date': 'DATE'}, inplace=True)
# brent_oil_prices.set_index('DATE', inplace=True)

# gdp = pd.read_csv('Inputs/data/raw_data/gdp.csv', parse_dates=['DATE'])
# gdp.set_index('DATE', inplace=True)

# inflation = pd.read_csv('Inputs/data/raw_data/inflation.csv', parse_dates=['DATE'])
# inflation.set_index('DATE', inplace=True)

# unemployment = pd.read_csv('Inputs/data/raw_data/unemployment.csv', parse_dates=['DATE'])
# unemployment.set_index('DATE', inplace=True)

# exchange_rate = pd.read_csv('Inputs/data/raw_data/exchange_rate.csv', parse_dates=['DATE'])
# exchange_rate.set_index('DATE', inplace=True)

# gepu_data = pd.read_csv('Inputs/data/raw_data/global_economic_policy_uncertainty.csv', parse_dates=['DATE'])
# gepu_data.set_index('DATE', inplace=True)

# emv_data = pd.read_csv('Inputs/data/raw_data/equity_market_volatility.csv', parse_dates=['DATE'])
# emv_data.set_index('DATE', inplace=True)

# opec_data = pd.read_csv('Inputs/data/raw_data/opec_policies.csv', parse_dates=['DATE'])
# opec_data.set_index('DATE', inplace=True)

# # Resample the data to annual frequency if necessary
# brent_oil_prices_annual = brent_oil_prices.resample('A').mean()
# gdp_annual = gdp.resample('A').mean()
# inflation_annual = inflation.resample('A').mean()
# unemployment_annual = unemployment.resample('A').mean()
# exchange_rate_annual = exchange_rate.resample('A').mean()
# gepu_annual = gepu_data.resample('A').mean()
# emv_annual = emv_data.resample('A').mean()
# opec_annual = opec_data.resample('A').mean()

# # Merge the datasets
# merged_data = brent_oil_prices_annual.merge(gdp_annual, left_index=True, right_index=True, how='inner')
# merged_data = merged_data.merge(inflation_annual, left_index=True, right_index=True, how='inner')
# merged_data = merged_data.merge(unemployment_annual, left_index=True, right_index=True, how='inner')
# merged_data = merged_data.merge(exchange_rate_annual, left_index=True, right_index=True, how='inner')
# merged_data = merged_data.merge(gepu_annual, left_index=True, right_index=True, how='inner')
# merged_data = merged_data.merge(emv_annual, left_index=True, right_index=True, how='inner')
# merged_data = merged_data.merge(opec_annual, left_index=True, right_index=True, how='inner')

# # Add an empty 'Date' column
# merged_data['Date'] = ''

# # Save the merged data to CSV
# merged_data.to_csv('Inputs/data/processed_data/merged_data.csv')

# print("Data merged, 'Date' column added, and saved.")

# # Calculate correlations
# correlations = merged_data[['Price', 'GDP', 'CPIAUCSL', 'UNRATE', 'DEXUSEU', 'GEPUCURRENT', 'EMVELECTGOVRN', 'COOTHERZ315']].corr()



# print("Correlation Matrix:")
# print(correlations)
# print("\nMerged Data Sample:")
# print(merged_data.head(10))




import pandas as pd

# Load the data and ensure the date column is consistently named 'DATE'
brent_oil_prices = pd.read_csv('Inputs/data/raw_data/BrentOilPrices.csv', parse_dates=['Date'])
brent_oil_prices.rename(columns={'Date': 'Date','Price':'OilPrice'}, inplace=True)
brent_oil_prices.set_index('Date', inplace=True)

gdp = pd.read_csv('Inputs/data/raw_data/gdp.csv', parse_dates=['DATE'])
gdp.rename(columns={'DATE': 'Date', 'GDP': 'GDP'}, inplace=True)
gdp.set_index('Date', inplace=True)

inflation = pd.read_csv('Inputs/data/raw_data/inflation.csv', parse_dates=['DATE'])
inflation.rename(columns={'DATE': 'Date', 'CPIAUCSL': 'Inflation'}, inplace=True)
inflation.set_index('Date', inplace=True)

unemployment = pd.read_csv('Inputs/data/raw_data/unemployment.csv', parse_dates=['DATE'])
unemployment.rename(columns={'DATE': 'Date', 'UNRATE': 'Unemployment'}, inplace=True)
unemployment.set_index('Date', inplace=True)

exchange_rate = pd.read_csv('Inputs/data/raw_data/exchange_rate.csv', parse_dates=['DATE'])
exchange_rate.rename(columns={'DATE': 'Date', 'DEXUSEU': 'ExchangeRate'}, inplace=True)
exchange_rate.set_index('Date', inplace=True)

gepu_data = pd.read_csv('Inputs/data/raw_data/global_economic_policy_uncertainty.csv', parse_dates=['DATE'])
gepu_data.rename(columns={'DATE': 'Date', 'GEPUCURRENT': 'GlobalEconomicPolicy'}, inplace=True)
gepu_data.set_index('Date', inplace=True)

emv_data = pd.read_csv('Inputs/data/raw_data/equity_market_volatility.csv', parse_dates=['DATE'])
emv_data.rename(columns={'DATE': 'Date', 'EMVELECTGOVRN': 'equity_market_volatility'}, inplace=True)
emv_data.set_index('Date', inplace=True)

opec_data = pd.read_csv('Inputs/data/raw_data/opec_policies.csv', parse_dates=['DATE'])
opec_data.rename(columns={'DATE': 'Date', 'COOTHERZ315': 'opec_policies'}, inplace=True)
opec_data.set_index('Date', inplace=True)

# Resample the data to annual frequency if necessary
brent_oil_prices_annual = brent_oil_prices.resample('A').mean()
gdp_annual = gdp.resample('A').mean()
inflation_annual = inflation.resample('A').mean()
unemployment_annual = unemployment.resample('A').mean()
exchange_rate_annual = exchange_rate.resample('A').mean()
gepu_annual = gepu_data.resample('A').mean()
emv_annual = emv_data.resample('A').mean()
opec_annual = opec_data.resample('A').mean()

# Merge the datasets
merged_data = brent_oil_prices_annual.merge(gdp_annual, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(inflation_annual, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(unemployment_annual, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(exchange_rate_annual, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(gepu_annual, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(emv_annual, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(opec_annual, left_index=True, right_index=True, how='inner')

# Save the merged data to CSV
merged_data.to_csv('Inputs/data/processed_data/merged_data.csv')

print("Data preprocessing completed, merged data saved to CSV.")

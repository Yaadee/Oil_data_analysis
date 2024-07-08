
import pandas as pd
import pandas as pd

def preprocess_data(file_path, output_path):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data.to_csv(output_path)
    print(f"Data preprocessed and saved to {output_path}")
     #Load the data and ensure the date column is consistently named 'DATE'
# Preprocess Brent Oil Prices
preprocess_data('Inputs/data/raw_data/BrentOilPrices.csv', 'Inputs/data/processed_data/preprocessed_brent_prices_data.csv')

gdp = pd.read_csv('Inputs/data/raw_data/gdp.csv', parse_dates=['DATE'])
gdp.rename(columns={'DATE': 'Date', 'GDP': 'GDP'}, inplace=True)
gdp.set_index('Date', inplace=True)
gdp.to_csv("Inputs/data/processed_data/preprocessed_gdp_data.csv")


inflation = pd.read_csv('Inputs/data/raw_data/inflation.csv', parse_dates=['DATE'])
inflation.rename(columns={'DATE': 'Date', 'CPIAUCSL': 'Inflation'}, inplace=True)
inflation.set_index('Date', inplace=True)
inflation.to_csv("Inputs/data/processed_data/preprocessed_inflation_data.csv")


unemployment = pd.read_csv('Inputs/data/raw_data/unemployment.csv', parse_dates=['DATE'])
unemployment.rename(columns={'DATE': 'Date', 'UNRATE': 'Unemployment'}, inplace=True)
unemployment.set_index('Date', inplace=True)
unemployment.to_csv("Inputs/data/processed_data/preprocessed_unemployment.csv")



exchange_rate = pd.read_csv('Inputs/data/raw_data/exchange_rate.csv', parse_dates=['DATE'])
exchange_rate.rename(columns={'DATE': 'Date', 'DEXUSEU': 'ExchangeRate'}, inplace=True)
exchange_rate.set_index('Date', inplace=True)
exchange_rate.to_csv("Inputs/data/processed_data/preprocessed_exchange_rate.csv")


gepu_data = pd.read_csv('Inputs/data/raw_data/global_economic_policy_uncertainty.csv', parse_dates=['DATE'])
gepu_data.rename(columns={'DATE': 'Date', 'GEPUCURRENT': 'GlobalEconomicPolicy'}, inplace=True)
gepu_data.set_index('Date', inplace=True)
gepu_data.to_csv("Inputs/data/processed_data/preprocessed_gepu_data.csv")


emv_data = pd.read_csv('Inputs/data/raw_data/equity_market_volatility.csv', parse_dates=['DATE'])
emv_data.rename(columns={'DATE': 'Date', 'EMVELECTGOVRN': 'equity_market_volatility'}, inplace=True)
emv_data.set_index('Date', inplace=True)
emv_data.to_csv("Inputs/data/processed_data/preprocessed_emv_data.csv")


opec_data = pd.read_csv('Inputs/data/raw_data/opec_policies.csv', parse_dates=['DATE'])
opec_data.rename(columns={'DATE': 'Date', 'COOTHERZ315': 'opec_policies'}, inplace=True)
opec_data.set_index('Date', inplace=True)
opec_data.to_csv("Inputs/data/processed_data/preprocessed_opec_data.csv")


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
# brent_oil_prices_annual = brent_oil_prices.resample('A').mean()
# gdp_annual = gdp.resample('A').mean()
# inflation_annual = inflation.resample('A').mean()
# unemployment_annual = unemployment.resample('A').mean()
# exchange_rate_annual = exchange_rate.resample('A').mean()
# gepu_annual = gepu_data.resample('A').mean()
# emv_annual = emv_data.resample('A').mean()
# opec_annual = opec_data.resample('A').mean()

# Merge the datasets
merged_data = brent_oil_prices.merge(gdp, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(inflation, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(unemployment, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(exchange_rate, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(gepu_data, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(emv_data, left_index=True, right_index=True, how='inner')
merged_data = merged_data.merge(opec_data, left_index=True, right_index=True, how='inner')

# Save the merged data to CSV
merged_data.to_csv('Inputs/data/processed_data/merged_data.csv')

print("Data preprocessing completed, merged data saved to CSV.")

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR

# Load the preprocessed datasets
brent_prices = pd.read_csv('Inputs/data/processed_data/preprocessed_brent_prices_data.csv', index_col='Date', parse_dates=True)
gdp = pd.read_csv('Inputs/data/processed_data/preprocessed_gdp_data.csv', index_col='Date', parse_dates=True)
inflation = pd.read_csv('Inputs/data/processed_data/preprocessed_inflation_data.csv', index_col='Date', parse_dates=True)
unemployment = pd.read_csv('Inputs/data/processed_data/preprocessed_unemployment.csv', index_col='Date', parse_dates=True)
exchange_rate = pd.read_csv('Inputs/data/processed_data/preprocessed_exchange_rate.csv', index_col='Date', parse_dates=True)
gepu = pd.read_csv('Inputs/data/processed_data/preprocessed_gepu_data.csv', index_col='Date', parse_dates=True)
emv = pd.read_csv('Inputs/data/processed_data/preprocessed_emv_data.csv', index_col='Date', parse_dates=True)
opec = pd.read_csv('Inputs/data/processed_data/preprocessed_opec_data.csv', index_col='Date', parse_dates=True)

# Ensure all datasets have the same frequency
datasets = [brent_prices, gdp, inflation, unemployment, exchange_rate, gepu, emv, opec]
for dataset in datasets:
    dataset.index = pd.to_datetime(dataset.index)
    dataset.index = dataset.index.to_period('M')

# Merge the datasets on the Date column
data = brent_prices.join([gdp, inflation, unemployment, exchange_rate, gepu, emv, opec], how='inner').dropna()

# Fit the VAR model
model = VAR(data)
lag_order = model.select_order(maxlags=15)
print(lag_order.summary())
optimal_lag = lag_order.aic

results = model.fit(optimal_lag)

# Print the summary of the results
print(results.summary())

# Forecast the next 10 periods
forecast = results.forecast(data.values[-results.k_ar:], steps=10)
forecast_df = pd.DataFrame(forecast, index=pd.date_range(start=data.index[-1].to_timestamp(), periods=10, freq='M'), columns=data.columns)

# Plot the forecast
plt.figure(figsize=(10, 6))
for col in forecast_df.columns:
    plt.plot(forecast_df.index, forecast_df[col], label=f'Forecast {col}')
plt.legend()
plt.title('VAR Model Forecast')
plt.xlabel('Date')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the forecast to CSV
forecast_df.to_csv('Results/var/forecast.csv')
print("VAR model forecasting completed and saved to Results/var/forecast.csv")

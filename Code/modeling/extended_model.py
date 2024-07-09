import pandas as pd
from statsmodels.tsa.statespace.varmax import VARMAX

# Load the datasets
brent_prices = pd.read_csv('Inputs/data/processed_data/preprocessed_brent_prices_data.csv', index_col='Date', parse_dates=True)
gdp = pd.read_csv('Inputs/data/raw_data/gdp.csv', index_col='DATE', parse_dates=True)
inflation = pd.read_csv('Inputs/data/raw_data/inflation.csv', index_col='DATE', parse_dates=True)
exchange_rate = pd.read_csv('Inputs/data/raw_data/exchange_rate.csv', index_col='DATE', parse_dates=True)

# Merge the datasets
data = brent_prices.join([gdp, inflation, exchange_rate], how='inner').dropna()

# Rename columns for clarity
data.columns = ['Brent_Oil_Price', 'GDP', 'Inflation', 'Exchange_Rate']

# Fit the VARMAX model
model = VARMAX(data, order=(1, 1))
results = model.fit()

# Forecast the prices
forecast = results.get_forecast(steps=30)
forecast_df = forecast.predicted_mean

# Plot the original and forecasted prices
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Brent_Oil_Price'], label='Original Brent Oil Prices')
plt.plot(forecast_df.index, forecast_df['Brent_Oil_Price'], label='Forecasted Brent Oil Prices')
plt.title('Brent Oil Prices Forecast with Extended Model')
plt.xlabel('Date')
plt.ylabel('Price (USD per Barrel)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the forecast to CSV
forecast_df.to_csv('Results/extended_model/forecasted_prices.csv')
print("Extended model forecast completed and saved to Results/extended_model/forecasted_prices.csv")

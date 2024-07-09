import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.arima.model import ARIMA

# Load the preprocessed Brent oil prices data
data = pd.read_csv('Inputs/data/processed_data/preprocessed_brent_prices_data.csv', index_col='Date', parse_dates=True)

# Split the data into training and test sets
train_size = int(len(data) * 0.7)
train, test = data[0:train_size], data[train_size:len(data)]

# Fit the ARIMA model
model = ARIMA(train['Price'], order=(1, 1, 1))
results = model.fit()

# Forecast the prices
forecast = results.forecast(steps=len(test))
test['Forecast'] = forecast.values

# Calculate performance metrics
mse = mean_squared_error(test['Price'], test['Forecast'])
mae = mean_absolute_error(test['Price'], test['Forecast'])

print(f'Mean Squared Error: {mse}')
print(f'Mean Absolute Error: {mae}')

# Plot the original and forecasted prices
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(train.index, train['Price'], label='Train Data')
plt.plot(test.index, test['Price'], label='Test Data')
plt.plot(test.index, test['Forecast'], label='Forecast')
plt.title('ARIMA Model Backtest')
plt.xlabel('Date')
plt.ylabel('Brent Oil Price (USD per Barrel)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the forecast and performance metrics to CSV
test[['Price', 'Forecast']].to_csv('Results/model_validation/forecasted_prices.csv')
metrics_df = pd.DataFrame({'MSE': [mse], 'MAE': [mae]})
metrics_df.to_csv('Results/model_validation/performance_metrics.csv')
print("Model validation completed and saved to Results/model_validation")

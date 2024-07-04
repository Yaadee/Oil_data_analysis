# import pandas as pd
# import matplotlib.pyplot as plt
# from statsmodels.tsa.api import VAR

# def var_model(input_path_brent, input_path_gdp, output_path, forecast_steps):
#     # Load data
#     brent_prices = pd.read_csv(input_path_brent, parse_dates=['Date'])
#     gdp_data = pd.read_csv(input_path_gdp, parse_dates=['date'])  # Assuming 'date' is the column for GDP data
    
#     # Rename columns for consistency
#     gdp_data.rename(columns={'date': 'Date', 'GDP': 'GDP'}, inplace=True)
    
#     # Merge data on 'Date' column
#     combined_data = pd.merge(brent_prices, gdp_data[['Date', 'GDP']], on='Date', how='inner')
#     combined_data.set_index('Date', inplace=True)
    
#     # Check for constant columns or missing values
#     if combined_data.isnull().any().any():
#         raise ValueError("Data contains missing values.")
    
#     if combined_data.var().sum() == 0:
#         raise ValueError("Data contains constant columns.")
    
#     # Fit VAR model
#     model = VAR(combined_data[['Price', 'GDP']])
#     var_results = model.fit(maxlags=5, ic='aic')
    
#     # Forecast
#     var_forecast = var_results.forecast(var_results.y, steps=forecast_steps)
    
#     # Add forecasted results to DataFrame
#     forecast_index = pd.date_range(start=combined_data.index[-1], periods=forecast_steps + 1, freq='M')[1:]
#     forecast_df = pd.DataFrame(var_forecast, index=forecast_index, columns=['Price_Forecast', 'GDP_Forecast'])
#     combined_data = pd.concat([combined_data, forecast_df])
    
#     # Save combined_data to CSV
#     combined_data.to_csv(output_path)
    
#     # Plotting
#     plt.figure(figsize=(14, 7))
#     plt.plot(combined_data.index, combined_data['Price'], label='Actual Brent Price')
#     plt.plot(forecast_df.index, forecast_df['Price_Forecast'], label='Forecasted Brent Price')
#     plt.title('VAR Model Forecast of Brent Prices')
#     plt.xlabel('Date')
#     plt.ylabel('Price')
#     plt.legend()
#     plt.grid(True)
#     plt.savefig("Results/var_forecast_plot.png")  # Save plot as PNG
#     plt.show()

# if __name__ == "__main__":
#     brent_path = "Inputs/data/processed_data/cleaned_brent_prices_data.csv"
#     gdp_path = "Inputs/data/processed_data/cleaned_gdp_data.csv"
#     output_path = "Results/bvar/var_results.csv"
#     forecast_steps = 10
    
#     try:
#         var_model(brent_path, gdp_path, output_path, forecast_steps)
#     except ValueError as ve:
#         print(f"Error in VAR model: {ve}")

import pandas as pd
from statsmodels.tsa.api import VAR

# Load data
brent_prices = pd.read_csv("Inputs/data/processed_data/cleaned_brent_prices_data.csv")
gdp_data = pd.read_csv("Inputs/data/processed_data/cleaned_gdp_data.csv")

# Convert 'Date' column to string type in brent_prices DataFrame
brent_prices['Date'] = brent_prices['Date'].astype(str)

# Merge on 'Date' and set index
combined_data = pd.merge(brent_prices, gdp_data, left_on='Date', right_on='date', how='inner')
combined_data.set_index('Date', inplace=True)

# Fit BVAR model
model = VAR(combined_data[['Brent_Price', 'GDP']])
bvar_results = model.fit(maxlags=5, ic='aic')

# Forecast
bvar_forecast = bvar_results.forecast(bvar_results.y, steps=10)
print(bvar_forecast)


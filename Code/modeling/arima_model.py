# import pandas as pd
# from statsmodels.tsa.arima.model import ARIMA

# def arima_model(input_path, output_path):
#     data = pd.read_csv(input_path, index_col='Date', parse_dates=True)
#     model = ARIMA(data['Price'], order=(5, 1, 0))
#     model_fit = model.fit()
#     data['Forecast_ARIMA'] = model_fit.predict(start=1, dynamic=False)
#     data.to_csv(output_path)

# if __name__ == "__main__":
#     arima_model("Inputs/data/processed_data/cleaned_brent_prices_data.csv", "Results/arima/arima_results.csv")


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load your datasets (assuming you have them as CSV files)
oil_prices = pd.read_csv("Inputs/data/processed_data/preprocessed_oil_data.csv")
gdp_data = pd.read_csv("Inputs/data/processed_data/preprocessed_gdp_data.csv")
inflation_data = pd.read_csv("Inputs/data/processed_data/preprocessed_inflation_data.csv")

# Assuming potential column names ('date', 'Date', 'DATE')
date_columns = ['date', 'Date', 'DATE']

# Function to handle date column conversion
def convert_to_datetime(df, date_columns):
    for col in date_columns:
        if col in df.columns:
            df['Date'] = pd.to_datetime(df[col])
            return df
    raise ValueError("Date column not found in the DataFrame.")

# Convert date columns for each dataset
oil_prices = convert_to_datetime(oil_prices, date_columns)
gdp_data = convert_to_datetime(gdp_data, date_columns)
inflation_data = convert_to_datetime(inflation_data, date_columns)

# Merge datasets on 'Date' column
merged_data = pd.merge(oil_prices, gdp_data, on='Date', suffixes=('_oil', '_gdp'))
merged_data = pd.merge(merged_data, inflation_data, on='Date')

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Plot oil prices
axs[0].plot(merged_data['Date'], merged_data['Price'], label='Oil Price', color='blue')
axs[0].set_ylabel('Oil Price (USD per barrel)')
axs[0].set_title('Oil Price and Economic Indicators')

# Plot GDP
axs[1].plot(merged_data['Date'], merged_data['GDP'], label='GDP', color='green')
axs[1].set_ylabel('GDP')

# Plot Inflation
axs[2].plot(merged_data['Date'], merged_data['CPIAUCSL'], label='Inflation', color='orange')
axs[2].set_ylabel('Inflation')

# Add legend and title
fig.suptitle('Impact of GDP and Inflation on Oil Prices', fontsize=16)
plt.xlabel('Date')

plt.tight_layout()
plt.show()

# Correlation analysis
correlation_matrix = merged_data[['Price', 'GDP', 'CPIAUCSL']].corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Regression analysis (example: linear regression of oil price on GDP and inflation)
X = merged_data[['GDP', 'CPIAUCSL']]
y = merged_data['Price']

model = LinearRegression()
model.fit(X, y)




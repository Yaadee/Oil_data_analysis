import pandas as pd
import matplotlib.pyplot as plt

# Load the preprocessed Brent oil prices data
brent_prices = pd.read_csv('Inputs/data/processed_data/preprocessed_brent_prices_data.csv', index_col='Date', parse_dates=True)

# Create a date range that matches the index of brent_prices
date_range = pd.date_range(start='1987-01-01', periods=len(brent_prices), freq='MS')

# Hypothetical data for technological changes (fracking, renewables, efficiency)
tech_changes_data = {
    'DATE': date_range,
    'Fracking_Adoption': pd.Series([x/100 for x in range(len(brent_prices))]),  # Hypothetical increasing trend
    'Renewable_Energy_Adoption': pd.Series([x/200 for x in range(len(brent_prices))]),  # Hypothetical increasing trend
    'Fuel_Efficiency_Improvements': pd.Series([x/300 for x in range(len(brent_prices))])  # Hypothetical increasing trend
}

tech_changes = pd.DataFrame(tech_changes_data)
tech_changes.set_index('DATE', inplace=True)

# Merge the datasets
data = brent_prices.join(tech_changes, how='inner')

# Plot the impact of technological changes on Brent oil prices
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], label='Brent Oil Price')
plt.plot(data.index, data['Fracking_Adoption'], label='Fracking Adoption (Hypothetical)')
plt.plot(data.index, data['Renewable_Energy_Adoption'], label='Renewable Energy Adoption (Hypothetical)')
plt.plot(data.index, data['Fuel_Efficiency_Improvements'], label='Fuel Efficiency Improvements (Hypothetical)')
plt.title('Impact of Technological Changes on Brent Oil Prices')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

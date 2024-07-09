import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
brent_prices = pd.read_csv('Inputs/data/processed_data/preprocessed_brent_prices_data.csv', index_col='Date', parse_dates=True)
gdp = pd.read_csv('Inputs/data/raw_data/gdp.csv', index_col='DATE', parse_dates=True)
inflation = pd.read_csv('Inputs/data/raw_data/inflation.csv', index_col='DATE', parse_dates=True)
unemployment = pd.read_csv('Inputs/data/raw_data/unemployment.csv', index_col='DATE', parse_dates=True)
exchange_rate = pd.read_csv('Inputs/data/raw_data/exchange_rate.csv', index_col='DATE', parse_dates=True)

# Merge the datasets on the DATE column
data = brent_prices.join([gdp, inflation, unemployment, exchange_rate], how='inner').dropna()

# Rename columns for clarity
data.columns = ['Brent_Oil_Price', 'GDP', 'Inflation', 'Unemployment', 'Exchange_Rate']

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Brent Oil Price and Economic Indicators')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

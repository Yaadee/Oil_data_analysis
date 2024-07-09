import pandas as pd
import matplotlib.pyplot as plt

# Load the preprocessed Brent oil prices data
brent_prices = pd.read_csv('Inputs/data/processed_data/preprocessed_brent_prices_data.csv', index_col='Date', parse_dates=True)

# Hypothetical data for political and regulatory factors (environmental regulations, trade policies)
political_factors_data = {
    'DATE': pd.date_range(start='2000-01-01', periods=len(brent_prices), freq='M'),
    'Environmental_Regulations': pd.Series([x/150 for x in range(len(brent_prices))]),  # Hypothetical increasing trend
    'Trade_Policies': pd.Series([x/250 for x in range(len(brent_prices))])  # Hypothetical increasing trend
}

political_factors = pd.DataFrame(political_factors_data)
political_factors.set_index('DATE', inplace=True)

# Merge the datasets
data = brent_prices.join(political_factors, how='inner')

# Plot the impact of political and regulatory factors on Brent oil prices
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], label='Brent Oil Price')
plt.plot(data.index, data['Environmental_Regulations'], label='Environmental Regulations (Hypothetical)')
plt.plot(data.index, data['Trade_Policies'], label='Trade Policies (Hypothetical)')
plt.title('Impact of Political and Regulatory Factors on Brent Oil Prices')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

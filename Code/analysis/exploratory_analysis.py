
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged data
merged_data = pd.read_csv('Inputs/data/processed_data/merged_data.csv', parse_dates=['Date'])
merged_data.set_index('Date', inplace=True)

# Plotting multiple EDA visualizations

# Time series plot of Brent Oil Prices
plt.figure(figsize=(14, 7))
plt.plot(merged_data.index, merged_data['OilPrice'], marker='o', linestyle='-')
plt.title('Brent Oil Prices Over Time')
plt.xlabel('Year')
plt.ylabel('Oil Price')
plt.grid(True)
plt.show()

# Pairplot for correlation overview
sns.pairplot(merged_data[['OilPrice', 'GDP', 'Inflation', 'Unemployment', 'ExchangeRate']],
             kind='scatter', diag_kind='kde')
plt.suptitle('Pairplot of Variables', y=1.02)
plt.show()

# Heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(merged_data.corr(), annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

# Boxplot of Global Economic Policy Uncertainty
plt.figure(figsize=(10, 6))
sns.boxplot(x=merged_data['GlobalEconomicPolicy'])
plt.title('Boxplot of Global Economic Policy Uncertainty')
plt.xlabel('Global Economic Policy Uncertainty')
plt.show()

# Line plot of Equity Market Volatility
plt.figure(figsize=(12, 6))
plt.plot(merged_data.index, merged_data['equity_market_volatility'], color='purple')
plt.title('Equity Market Volatility Over Time')
plt.xlabel('Year')
plt.ylabel('Volatility Index')
plt.grid(True)
plt.show()

# Scatter plot of Oil Price vs. GDP
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['GDP'], merged_data['OilPrice'], color='green', alpha=0.5)
plt.title('Scatter Plot of Oil Price vs. GDP')
plt.xlabel('GDP')
plt.ylabel('Oil Price')
plt.grid(True)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged data
merged_data = pd.read_csv('Inputs/data/processed_data/merged_data.csv', parse_dates=['Date'])
merged_data.set_index('Date', inplace=True)

# Compute correlations with Oil Price
correlations = merged_data.corr()['OilPrice'].drop('OilPrice')

# Plotting correlations
plt.figure(figsize=(10, 6))
sns.barplot(x=correlations.index, y=correlations.values, palette='viridis')
plt.title('Correlation of Economic Indicators with Oil Price')
plt.xlabel('Economic Indicators')
plt.ylabel('Correlation Coefficient')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

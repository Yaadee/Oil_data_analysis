# import pandas as pd
# import matplotlib.pyplot as plt


# def exploratory_analysis(input_path):
#     data = pd.read_csv(input_path, index_col='Date', parse_dates=True)
#     plt.figure(figsize=(10,6))
#     plt.plot(data['Price'], label='Brent Oil Prices')
#     plt.title('Brent Oil Prices Over Time')
#     plt.xlabel('Date')
#     plt.ylabel('Price (USD)')
#     plt.legend()
#     plt.show()
#     data_understanding =data.head(100)
#     print(data_understanding)
#     print("Number of null counts",data.isnull().count())

# if __name__ == "__main__":
#     exploratory_analysis("Inputs/data/processed_data/cleaned_brent_prices_data.csv")



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the merged data
# data = pd.read_csv('Inputs/data/processed_data/merged_data.csv', index_col='DATE', parse_dates=True)

# # Plot the data
# plt.figure(figsize=(14, 7))
# sns.lineplot(data=data)
# plt.title('Brent Oil Prices and Economic Indicators')
# plt.ylabel('Values')
# plt.xlabel('Year')
# plt.show()

# # Correlation heatmap
# plt.figure(figsize=(10, 6))
# sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
# plt.title('Correlation Heatmap')
# plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# def exploratory_analysis(input_path):
#     # Load the data
#     data = pd.read_csv(input_path, index_col='Date', parse_dates=True)
    
#     # Print the column names to check for 'Close' column
#     print("Column Names:", data.columns)
    
#     # Print the first few rows to inspect the data
#     print("First 5 rows of data:\n", data.head())
    
#     # Plot Brent Oil Prices Over Time
#     plt.figure(figsize=(10, 6))
    
#     # Ensure 'Close' column exists
#     if 'Close' in data.columns:
#         plt.plot(data['Close'], label='Brent Oil Prices')
#         plt.title('Brent Oil Prices Over Time')
#         plt.xlabel('Date')
#         plt.ylabel('Price (USD)')
#         plt.legend()
#         plt.show()
#     else:
#         print("Error: 'Close' column not found in the data.")

#     # Display the first 100 rows for data understanding
#     data_understanding = data.head(100)
#     print(data_understanding)

#     # Display the number of null values in each column
#     null_counts = data.isnull().sum()
#     print("Number of null values in each column:\n", null_counts)

# def plot_merged_data(merged_path):
#     # Load the merged data
#     data = pd.read_csv(merged_path, index_col='DATE', parse_dates=True)

#     # Plot Brent Oil Prices and Economic Indicators Over Time
#     plt.figure(figsize=(14, 7))
#     sns.lineplot(data=data)
#     plt.title('Brent Oil Prices and Economic Indicators')
#     plt.ylabel('Values')
#     plt.xlabel('Year')
#     plt.show()

#     # Plot Correlation Heatmap
#     plt.figure(figsize=(10, 6))
#     sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
#     plt.title('Correlation Heatmap')
#     plt.show()

# if __name__ == "__main__":
#     # Perform exploratory analysis on Brent oil prices
#     exploratory_analysis("Inputs/data/processed_data/cleaned_brent_prices_data.csv")
    
#     # Plot merged data for Brent oil prices and economic indicators
#     plot_merged_data("Inputs/data/processed_data/merged_data.csv")


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

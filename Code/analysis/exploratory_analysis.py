import pandas as pd
import matplotlib.pyplot as plt


def exploratory_analysis(input_path):
    data = pd.read_csv(input_path, index_col='Date', parse_dates=True)
    plt.figure(figsize=(10,6))
    plt.plot(data['Price'], label='Brent Oil Prices')
    plt.title('Brent Oil Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()
    data_understanding =data.head(100)
    print(data_understanding)
    print("Number of null counts",data.isnull().count())

if __name__ == "__main__":
    exploratory_analysis("Inputs/data/processed_data/cleaned_brent_prices_data.csv")



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the merged data
data = pd.read_csv('Inputs/data/processed_data/merged_data.csv', index_col='DATE', parse_dates=True)

# Plot the data
plt.figure(figsize=(14, 7))
sns.lineplot(data=data)
plt.title('Brent Oil Prices and Economic Indicators')
plt.ylabel('Values')
plt.xlabel('Year')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

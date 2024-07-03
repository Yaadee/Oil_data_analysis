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
    exploratory_analysis("Inputs/data/processed_data/preprocessed_data.csv")
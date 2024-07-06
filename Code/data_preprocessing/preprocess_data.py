# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# def preprocess_data(input_path, output_path):
#     # Read input CSV
#     data = pd.read_csv(input_path)
    
#     # Extract year from 'Date' column and rename it to 'date'
#     data['date'] = pd.to_datetime(data['Date']).dt.year
#     data = data.drop('Date', axis=1)
    
#     # Save preprocessed data to output CSV (without altering 'Price')
#     data.to_csv(output_path, index=False)

# def preprocess_GDP_data(input_path, output_path):
#     # Read input CSV
#     data = pd.read_csv(input_path)
    
#     # Extract year from 'DATE' column and rename it to 'date'
#     data['date'] = pd.to_datetime(data['date']).dt.year
#     # Save preprocessed data to output CSV
#     data.to_csv(output_path, index=False)

# def preprocess_CPIAUCSL_data(input_path, output_path):
#     # Read input CSV
#     data = pd.read_csv(input_path)
    
#     # Extract year from 'DATE' column and rename it to 'date'
#     data['date'] = pd.to_datetime(data['DATE']).dt.year
#     data = data.drop('DATE', axis=1)
    
#     # Save preprocessed data to output CSV
#     data.to_csv(output_path, index=False)

# if __name__ == "__main__":
#     preprocess_data("Inputs/data/raw_data/BrentOilPrices.csv", "Inputs/data/processed_data/preprocessed_oil_data.csv")
#     preprocess_GDP_data("Inputs/data/raw_data/all_countries_gdp.csv", "Inputs/data/processed_data/preprocessed_gdp_data.csv")
#     preprocess_CPIAUCSL_data("Inputs/data/raw_data/inflation_data.csv", "Inputs/data/processed_data/preprocessed_inflation_data.csv")



# # import pandas as pd

# # Load the data
# brent_data = pd.read_csv('Inputs/data/raw_data/BrentOilPrices.csv', index_col='Date', parse_dates=True)
# gdp_data_usa = pd.read_csv('Inputs/data/raw_data/all_countries_gdp.csv', index_col='date', parse_dates=True)
# inflation_data = pd.read_csv('Inputs/data/raw_data/inflation_data.csv', index_col='DATE', parse_dates=True)


# # Resample the data to annual frequency (optional)
# brent_data_annual = brent_data.resample('A').mean()
# gdp_data_usa_annual = gdp_data_usa.resample('A').mean()
# inflation_data_annual = inflation_data.resample('A').mean()

# # Merge the datasets
# merged_data = brent_data_annual.merge(gdp_data_usa_annual, left_index=True, right_index=True, how='inner')
# merged_data = merged_data.merge(inflation_data_annual, left_index=True, right_index=True, how='inner')

# # Save the merged data to CSV
# merged_data.to_csv('Inputs/data/processed_data/merged_data.csv')


import pandas as pd

def preprocess_data(input_path, output_path):
    # Read input CSV
    data = pd.read_csv(input_path)
    
    # Extract year from 'Date' column and rename it to 'date'
    data['date'] = pd.to_datetime(data['Date']).dt.year
    data = data.drop('Date', axis=1)
    
    # Save preprocessed data to output CSV (without altering 'Price')
    data.to_csv(output_path, index=False)

def preprocess_GDP_data(input_path, output_path):
    # Read input CSV
    data = pd.read_csv(input_path)
    
    # Extract year from 'date' column and rename it to 'date'
    data['date'] = pd.to_datetime(data['date']).dt.year
    
    # Save preprocessed data to output CSV
    data.to_csv(output_path, index=False)

def preprocess_CPIAUCSL_data(input_path, output_path):
    # Read input CSV
    data = pd.read_csv(input_path)
    
    # Extract year from 'DATE' column and rename it to 'date'
    data['date'] = pd.to_datetime(data['DATE']).dt.year
    data = data.drop('DATE', axis=1)
    
    # Save preprocessed data to output CSV
    data.to_csv(output_path, index=False)

def merge_datasets(brent_path, gdp_path, inflation_path, output_path):
    # Load the preprocessed data
    brent_data = pd.read_csv(brent_path)
    gdp_data = pd.read_csv(gdp_path)
    inflation_data = pd.read_csv(inflation_path)
    
    # Set 'date' as the index and ensure it's datetime
    brent_data['date'] = pd.to_datetime(brent_data['date'], format='%Y')
    gdp_data['date'] = pd.to_datetime(gdp_data['date'], format='%Y')
    inflation_data['date'] = pd.to_datetime(inflation_data['date'], format='%Y')

    brent_data.set_index('date', inplace=True)
    gdp_data.set_index('date', inplace=True)
    inflation_data.set_index('date', inplace=True)
    
    # Resample the data to annual frequency
    brent_data_annual = brent_data.resample('A').mean()
    gdp_data_annual = gdp_data.resample('A').mean()
    inflation_data_annual = inflation_data.resample('A').mean()
    
    # Merge the datasets
    merged_data = brent_data_annual.merge(gdp_data_annual, left_index=True, right_index=True, how='inner')
    merged_data = merged_data.merge(inflation_data_annual, left_index=True, right_index=True, how='inner')
    
    # Save the merged data to CSV
    merged_data.to_csv(output_path)

if __name__ == "__main__":
    preprocess_data("Inputs/data/raw_data/BrentOilPrices.csv", "Inputs/data/processed_data/preprocessed_oil_data.csv")
    preprocess_GDP_data("Inputs/data/raw_data/all_countries_gdp.csv", "Inputs/data/processed_data/preprocessed_gdp_data.csv")
    preprocess_CPIAUCSL_data("Inputs/data/raw_data/inflation_data.csv", "Inputs/data/processed_data/preprocessed_inflation_data.csv")

    merge_datasets(
        "Inputs/data/processed_data/preprocessed_oil_data.csv",
        "Inputs/data/processed_data/preprocessed_gdp_data.csv",
        "Inputs/data/processed_data/preprocessed_inflation_data.csv",
        "Inputs/data/processed_data/merged_data.csv"
    )















# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Load Brent oil prices data
# # Assuming your data is in a CSV file named 'brent_oil_prices.csv'
# data = pd.read_csv('Inputs/data/processed_data/cleaned_brent_prices_data.csv', parse_dates=['Date'], index_col='Date')

# # Basic exploration
# print(data.head())
# print(data.info())

# # Plot the time series
# plt.figure(figsize=(12, 6))
# plt.plot(data['Price'], label='Brent Oil Price')
# plt.title('Historical Brent Oil Prices')
# plt.xlabel('Date')
# plt.ylabel('Price (USD per barrel)')
# plt.legend()
# plt.show()

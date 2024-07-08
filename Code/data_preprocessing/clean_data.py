import pandas as pd

def clean_data(file_path, output_path):
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)
    data.to_csv(output_path, index=False)
    print(f"Data cleaned and saved to {output_path}")

# Clean Brent Oil Prices
clean_data('Inputs/data/raw_data/BrentOilPrices.csv', 'Inputs/data/processed_data/cleaned_brent_prices_data.csv')

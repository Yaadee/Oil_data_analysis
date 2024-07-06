import pandas as pd

import pandas as pd

def clean_data(input_path, output_path):
    brent_prices = pd.read_csv(input_path)
    gdp_data = pd.read_csv(input_path)
    inlation_data = pd.read_csv(input_path)

    brent_prices.dropna(inplace=True)
    gdp_data.dropna(inplace=True)
    inlation_data.dropna(inplace=True)

    brent_prices.to_csv(output_path, index=False)
    gdp_data.to_csv(output_path, index=False)
    inlation_data.to_csv(output_path, index=False)

    brent_prices.fillna(method='ffill', inplace=True)
    gdp_data.fillna(method='ffill', inplace=True)
    inlation_data.fillna(method='ffill', inplace=True)


if __name__ == "__main__":
    clean_data("Inputs/data/raw_data/BrentOilPrices.csv", "Inputs/data/processed_data/cleaned_brent_prices_data.csv")
    clean_data("Inputs/data/raw_data/all_countries_gdp.csv","Inputs/data/processed_data/cleaned_gdp_data.csv")
    clean_data("Inputs/data/raw_data/inflation_data.csv","Inputs/data/processed_data/cleaned_inflation_data.csv")
    


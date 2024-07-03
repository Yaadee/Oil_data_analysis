import pandas as pd

import pandas as pd

def clean_data(input_path, output_path):
    data = pd.read_csv(input_path)
    data.dropna(inplace=True)
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_data("Inputs/data/raw_data/BrentOilPrices.csv", "Inputs/data/processed_data/cleaned_data.csv")


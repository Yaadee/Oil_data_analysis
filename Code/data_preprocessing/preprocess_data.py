import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    scaler = StandardScaler()
    data['Price'] = scaler.fit_transform(data[['Price']])
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data("Inputs/data/processed_data/cleaned_data.csv", "Inputs/data/processed_data/preprocessed_data.csv")

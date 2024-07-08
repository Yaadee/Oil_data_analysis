import pandas as pd

def generate_insights(file_path):
    data = pd.read_csv(file_path)
    print(data.describe())
    print(data.head())
    print(data.tail())

# Generate Insights for ARIMA Forecast Results
generate_insights('Results/arima/forecast.csv')

# Generate Insights for GARCH Forecast Results
generate_insights('Results/garch/forecast.csv')

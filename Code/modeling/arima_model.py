import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def arima_model(input_path, output_path):
    data = pd.read_csv(input_path, index_col='Date', parse_dates=True)
    model = ARIMA(data['Price'], order=(5, 1, 0))
    model_fit = model.fit()
    data['Forecast_ARIMA'] = model_fit.predict(start=1, dynamic=False)
    data.to_csv(output_path)

if __name__ == "__main__":
    arima_model("Inputs/data/processed_data/cleaned_brent_prices_data.csv", "Results/arima_results.csv")

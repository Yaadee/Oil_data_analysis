# run_garch_model.py

from arch import arch_model
import pandas as pd

def fit_garch_model(data):
    # Fit GARCH model
    model = arch_model(data, vol='Garch', p=1, q=1)
    garch_results = model.fit()
    return garch_results

def forecast_garch_model(model_results, horizon=10):
    # Forecast
    garch_forecast = model_results.forecast(horizon=horizon)
    return garch_forecast

def save_to_csv(data, filename):
    data.to_csv(filename, index=True)

if __name__ == "__main__":
    # Load cleaned data
    brent_prices = pd.read_csv("Inputs/data/processed_data/cleaned_brent_prices_data.csv")

    # Fit GARCH model
    garch_results = fit_garch_model(brent_prices['Price'])

    # Forecast and save results to CSV
    garch_forecast = forecast_garch_model(garch_results)
    save_to_csv(garch_forecast.variance, 'Results/garch/garch_forecast_results.csv')

    # Optionally, print the forecasted variance
    print(garch_forecast.variance[-1:])

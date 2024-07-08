import pandas as pd
from arch import arch_model

def garch_model(file_path, column, forecast_steps):
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    model = arch_model(data[column], vol='Garch', p=1, q=1)
    model_fit = model.fit()
    
    # Forecast variance
    forecast = model_fit.forecast(horizon=forecast_steps)
    variance_forecast = forecast.variance.dropna().iloc[-1]
    
    # Generate date range for forecast
    last_date = data.index[-1]
    forecast_index = pd.date_range(start=last_date, periods=forecast_steps, freq=data.index.freq)
    variance_forecast.index = forecast_index
    
    print(variance_forecast)
    variance_forecast.to_csv('Results/garch/forecast.csv')
    print("GARCH model forecasting completed and saved to Results/garch/forecast.csv")

# GARCH Model for Brent Oil Prices
garch_model('Inputs/data/processed_data/preprocessed_brent_prices_data.csv', 'Price', 10)

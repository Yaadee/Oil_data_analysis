import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def arima_model(file_path, column, order, forecast_steps):
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    model = ARIMA(data[column], order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=forecast_steps)
    
    # Generate date range for forecast
    last_date = data.index[-1]
    forecast_index = pd.date_range(start=last_date, periods=forecast_steps + 1, freq=data.index.freq)[-forecast_steps:]
    forecast.index = forecast_index
    
    print(forecast)
    forecast.to_csv('Results/arima/forecast.csv')
    print("ARIMA model forecasting completed and saved to Results/arima/forecast.csv")

# ARIMA Model for Brent Oil Prices
arima_model('Inputs/data/processed_data/preprocessed_brent_prices_data.csv', 'Price', (5, 1, 0), 10)

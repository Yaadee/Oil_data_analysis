import pandas as pd
import matplotlib.pyplot as plt

def plot_forecast(file_path, title):
    data = pd.read_csv(file_path, index_col=0, parse_dates=True)
    
    plt.figure(figsize=(10, 5))
    plt.plot(data, marker='o')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Forecasted Values')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plot ARIMA Forecast Results
plot_forecast('Results/arima/forecast.csv', 'ARIMA Model Forecast')

# Plot GARCH Forecast Results
plot_forecast('Results/garch/forecast.csv', 'GARCH Model Forecast')

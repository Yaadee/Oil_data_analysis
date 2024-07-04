import pandas as pd
from bsts import BSTS
from bsts.model_components import LocalLevel

def bsts_model(input_path, output_path):
    # Load data
    data = pd.read_csv(input_path, index_col='Date', parse_dates=True)
    
    # Prepare data (assuming 'Date' is the index and 'Brent_Price' is the column)
    prices = data['Brent_Price']
    
    # Define the model components
    components = [LocalLevel()]
    
    # Create the model
    model = Bsts(prices, components)
    
    # Fit the model
    model.fit(num_iterations=1000)
    
    # Forecast
    forecast_horizon = 10
    pred = model.predict(forecast_horizon)
    predicted_mean = pred.mean()
    predicted_interval = pred.predicted_interval()
    
    # Add forecasted results to original data
    data['Forecast_BSTS'] = predicted_mean
    
    # Save results to CSV
    data.to_csv(output_path)

if __name__ == "__main__":
    bsts_model("Inputs/data/processed_data/cleaned_brent_prices_data.csv", "Results/bsts_results.csv")

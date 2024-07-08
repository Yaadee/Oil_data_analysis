import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ruptures as rpt

# Load Brent oil prices data
price_df = pd.read_csv("Inputs/data/processed_data/preprocessed_brent_prices_data.csv")

# Convert the 'Date' column to datetime object
price_df['Date'] = pd.to_datetime(price_df['Date'])
price_df = price_df.dropna(subset=['Date'])
price_df.set_index('Date', inplace=True)

# Resample the data to annual frequency, taking the mean price for each year
annual_price_df = price_df.resample('A').mean()

# Plot the annual Brent oil prices
plt.figure(figsize=(10, 6))
plt.plot(annual_price_df.index, annual_price_df['Price'], marker='o', linestyle='-')
plt.title('Annual Brent Oil Prices')
plt.xlabel('Year')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# Function to plot change points
def plot_change_points(signal, result, title):
    plt.figure(figsize=(12, 6))
    rpt.display(signal, result)
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Price')
    xticks = annual_price_df.index[result[:-1]]
    plt.xticks(ticks=result[:-1], labels=[str(year.year) for year in xticks], rotation=45)
    plt.show()

# Change point detection with l2 model
signal = annual_price_df['Price'].values
model_l2 = "l2"  # model to apply: "l2"
algo_l2 = rpt.Pelt(model=model_l2).fit(signal)
result_l2 = algo_l2.predict(pen=10)

# Display results for l2 model
plot_change_points(signal, result_l2, 'Change Point Detection on Annual Brent Oil Prices (l2 model)')

# Print detected change points for l2 model
print(f"Detected change points (l2 model): {result_l2[:-1]} (note: these are indices of the detected points)")

# Change point detection with l1 model
model_l1 = "l1"  # model to apply: "l1"
algo_l1 = rpt.Pelt(model=model_l1).fit(signal)
result_l1 = algo_l1.predict(pen=10)

# Display results for l1 model
plot_change_points(signal, result_l1, 'Change Point Detection on Annual Brent Oil Prices (l1 model)')

# Print detected change points for l1 model
print(f"Detected change points (l1 model): {result_l1[:-1]} (note: these are indices of the detected points)")

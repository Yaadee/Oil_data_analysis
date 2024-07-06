
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import ruptures as rpt

# # Load and format the data
# price_df = pd.read_csv("Inputs/data/processed_data/cleaned_brent_prices_data.csv")

# # Convert the 'Date' column to datetime object
# price_df['Date'] = pd.to_datetime(price_df['Date'])

# # Drop rows where the 'Date' conversion failed
# price_df = price_df.dropna(subset=['Date'])

# # Set 'Date' as the index
# price_df.set_index('Date', inplace=True)

# # Resample the data to annual frequency, taking the mean price for each year
# annual_price_df = price_df.resample('A').mean()

# # Convert the time series values to a numpy 1D array
# points = annual_price_df['Price'].values
# dates = annual_price_df.index.year  # Extract the years for x-axis labels

# # Function to display results and extract turning point years
# def display_and_extract_turning_points(points, model_cls, method_name, **kwargs):
#     model = kwargs.pop('model', 'l2')  # Remove 'model' from kwargs if it exists
#     pen = kwargs.pop('pen', None)  # Remove 'pen' from kwargs if it exists
#     n_bkps = kwargs.pop('n_bkps', 3)  # Remove 'n_bkps' from kwargs if it exists
#     algo = model_cls(model=model, **kwargs).fit(points)
    
#     if pen is not None:
#         result = algo.predict(pen=pen)
#     else:
#         result = algo.predict(n_bkps=n_bkps)
    
#     turning_point_years = [dates[cp] for cp in result[:-1]]  # exclude the last breakpoint
#     rpt.show.display(points, result, figsize=(10, 6))
#     plt.xticks(ticks=np.arange(len(dates)), labels=dates, rotation=45)  # Set x-axis labels
#     plt.title(f'Change Point Detection: {method_name}')
#     plt.show()
#     return turning_point_years

# # RUPTURES PACKAGE

# # Change point detection with the Pelt search method
# turning_points_pelt = display_and_extract_turning_points(points, rpt.Pelt, 'Pelt Search Method', model="rbf", pen=0.5)
# print(f'Turning points (Pelt): {turning_points_pelt}')

# # Change point detection with the Binary Segmentation search method
# turning_points_binseg = display_and_extract_turning_points(points, rpt.Binseg, 'Binary Segmentation Search Method', model="l2", n_bkps=5)
# print(f'Turning points (Binary Segmentation): {turning_points_binseg}')

# # Change point detection with the Window-based search method
# turning_points_window = display_and_extract_turning_points(points, rpt.Window, 'Window-Based Search Method', model="l2", width=3, n_bkps=5)
# print(f'Turning points (Window-Based): {turning_points_window}')

# # Change point detection with the Dynamic Programming search method
# turning_points_dynp = display_and_extract_turning_points(points, rpt.Dynp, 'Dynamic Programming Search Method', model="l1", min_size=1, n_bkps=5)
# print(f'Turning points (Dynamic Programming): {turning_points_dynp}')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ruptures as rpt

# Load Brent oil prices data
price_df = pd.read_csv("Inputs/data/processed_data/cleaned_brent_prices_data.csv")

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

# Change point detection
signal = annual_price_df['Price'].values
model = "l2"  # model to apply: "l1", "l2", "rbf", etc.
algo = rpt.Pelt(model=model).fit(signal)
result = algo.predict(pen=10)

# Display results
plt.figure(figsize=(10, 6))
rpt.display(signal, result)
plt.title('Change Point Detection on Annual Brent Oil Prices')
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()

# Print detected change points
print(f"Detected change points: {result[:-1]} (note: these are indices of the detected points)")

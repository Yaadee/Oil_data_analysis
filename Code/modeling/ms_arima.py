import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

# Load the preprocessed Brent oil prices data
data = pd.read_csv('Inputs/data/processed_data/preprocessed_brent_prices_data.csv', index_col='Date', parse_dates=True)

# Fit the Markov-Switching ARIMA model
model = MarkovRegression(data['Price'], k_regimes=2, trend='c', switching_variance=True)
results = model.fit()

# Print the summary of the results
print(results.summary())

# Plot the smoothed probabilities of the regimes
plt.figure(figsize=(10, 6))
plt.plot(data.index, results.smoothed_marginal_probabilities[0], label='Regime 1 Probability')
plt.plot(data.index, results.smoothed_marginal_probabilities[1], label='Regime 2 Probability')
plt.title('Smoothed Regime Probabilities')
plt.xlabel('Date')
plt.ylabel('Probability')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the smoothed probabilities to CSV
results.smoothed_marginal_probabilities.to_csv('Results/ms_arima/smoothed_probabilities.csv')
print("Markov-Switching ARIMA model analysis completed and saved to Results/ms_arima/smoothed_probabilities.csv")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load the preprocessed Brent oil prices data
data = pd.read_csv('Inputs/data/processed_data/preprocessed_brent_prices_data.csv', index_col='Date', parse_dates=True)
prices = data['Price'].values.reshape(-1, 1)

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_prices = scaler.fit_transform(prices)

# Prepare the dataset for LSTM
def create_dataset(dataset, time_step=1):
    X, Y = [], []
    for i in range(len(dataset) - time_step - 1):
        a = dataset[i:(i + time_step), 0]
        X.append(a)
        Y.append(dataset[i + time_step, 0])
    return np.array(X), np.array(Y)

time_step = 10
X, Y = create_dataset(scaled_prices, time_step)

# Reshape input to be [samples, time steps, features] which is required for LSTM
X = X.reshape(X.shape[0], X.shape[1], 1)

# Split the data into training and test sets
train_size = int(len(X) * 0.7)
test_size = len(X) - train_size
X_train, X_test = X[0:train_size], X[train_size:len(X)]
Y_train, Y_test = Y[0:train_size], Y[train_size:len(Y)]

# Build the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(time_step, 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, Y_train, batch_size=1, epochs=1)

# Predict and invert the scaling
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)

# Plot the predictions
plt.figure(figsize=(10, 6))
plt.plot(data.index, scaler.inverse_transform(scaled_prices), label='Original Data')
plt.plot(data.index[time_step:time_step + len(train_predict)], train_predict, label='Train Prediction')
plt.plot(data.index[time_step + len(train_predict) + 1:time_step + len(train_predict) + 1 + len(test_predict)], test_predict, label='Test Prediction')
plt.title('LSTM Model Forecast')
plt.xlabel('Date')
plt.ylabel('Brent Oil Price (USD per Barrel)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the predictions to CSV
train_predict_df = pd.DataFrame(train_predict, index=data.index[time_step:time_step + len(train_predict)], columns=['Train_Prediction'])
test_predict_df = pd.DataFrame(test_predict, index=data.index[time_step + len(train_predict) + 1:time_step + len(train_predict) + 1 + len(test_predict)], columns=['Test_Prediction'])
train_predict_df.to_csv('Results/lstm/train_predictions.csv')
test_predict_df.to_csv('Results/lstm/test_predictions.csv')
print("LSTM model forecasting completed and saved to Results/lstm")

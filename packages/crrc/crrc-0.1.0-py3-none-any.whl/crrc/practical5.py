def e1():
    return """import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler"""

def e2():
    return """np.random.seed(0)
time_steps = 300
x = np.linspace(0, 50, time_steps)
data = np.sin(x) + np.random.normal(scale=0.2, size=time_steps)
data = data.reshape(-1,1)"""

def e3():
    return """scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data)"""

def e4():
    return """X = []
y = []
sequence_length = 60

for i in range(sequence_length, len(scaled_data)):
    X.append(scaled_data[i-sequence_length:i, 0])
    y.append(scaled_data[i, 0])

X, y = np.array(X), np.array(y)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))"""

def e5():
    return """model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1],1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')"""

def e6():
    return """model.fit(X, y, epochs=20, batch_size=32)"""

def e7():
    return """predicted = model.predict(X)
predicted = scaler.inverse_transform(predicted.reshape(-1,1))
actual = scaler.inverse_transform(y.reshape(-1,1))"""

def e8():
    return """plt.figure(figsize=(12,6))
plt.plot(actual, color='red', label='Actual (Synthetic Stock Price)')
plt.plot(predicted, color='blue', label='Predicted Price')
plt.title('LSTM Stock Price Prediction (Synthetic Data)')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()"""


def e():
    return "Practical 5: RNN (LSTM) for Stock Price"

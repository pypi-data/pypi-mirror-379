def d1():
    return """import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import make_regression
from sklearn.preprocessing import MinMaxScaler"""

def d2():
    return """X, Y = make_regression(
    n_samples=100,
    n_features=2,
    noise=0.2,
    random_state=1
)"""

def d3():
    return """scalerX = MinMaxScaler()
scalerY = MinMaxScaler()
scalerX.fit(X)
scalerY.fit(Y.reshape(-1,1))
X_scaled = scalerX.transform(X)
Y_scaled = scalerY.transform(Y.reshape(-1,1))"""

def d4():
    return """model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(
    loss='mse',
    optimizer='adam'
)"""

def d5():
    return """model.fit(
    X_scaled,
    Y_scaled,
    epochs=1000,
    verbose=0
)"""

def d6():
    return """X_new, _ = make_regression(
    n_samples=3,
    n_features=2,
    noise=0.1,
    random_state=1
)
X_new_scaled = scalerX.transform(X_new)"""

def d7():
    return """Y_pred_scaled = model.predict(X_new_scaled)
Y_pred = scalerY.inverse_transform(Y_pred_scaled)

for xi, yi in zip(X_new_scaled, Y_pred_scaled):
    print(f"x={xi}, predicted={yi}")"""



def d():
    return "Practical 4: Linear Regression with Deep FFN"

def b1():
    return """import numpy as np
from keras.layers import Dense 
from keras.models import Sequential"""

def b2():
    return """model = Sequential()
model.add(Dense(units=2, activation='relu', input_dim=2))
model.add(Dense(units=1, activation='sigmoid'))"""

def b3():
    return """model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)"""

def b4():
    return """print(model.summary())
print(model.get_weights())"""

def b5():
    return """X = np.array([
    [0., 0.],
    [0., 1.],
    [1., 0.],
    [1., 1.]
])
Y = np.array([0., 1., 1., 0.])"""

def b6():
    return """model.fit(X, Y, epochs=1000, batch_size=4)

print(model.get_weights())
print(model.predict(X, batch_size=4))"""


def b():
    return "Practical 2: XOR Problem with Feedforward Network"

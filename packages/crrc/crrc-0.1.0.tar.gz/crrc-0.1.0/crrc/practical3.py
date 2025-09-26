def c1():
    return """from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
import numpy as np"""

def c2():
    return """X, Y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)

scaler = MinMaxScaler()
scaler.fit(X)
X = scaler.transform(X)"""

def c3():
    return """model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam')"""

def c4():
    return """model.fit(X, Y, epochs=500)"""

def c5():
    return """Xnew, Yreal = make_blobs(n_samples=3, centers=2, n_features=2, random_state=1)
Xnew = scaler.transform(Xnew)
Ynew_probs = model.predict(Xnew)
Ynew_probs = (Ynew_probs > 0.5).astype(int)

for i in range(len(Xnew)):
    print("X=%s, Predicted=%s, Desired=%s" % (Xnew[i], Ynew_probs[i], Yreal[i]))"""


def c():
    return "Practical 3: Classification with 2 Hidden Layers"

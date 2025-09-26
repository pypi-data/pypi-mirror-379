def g1():
    return """import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical"""

def g2():
    return """(X_train, y_train), (X_test, y_test) = mnist.load_data()"""

def g3():
    return """X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
X_test = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)"""

def g4():
    return """model = Sequential([
    Conv2D(32, kernel_size=3, activation='relu', input_shape=(28,28,1)),
    Conv2D(64, kernel_size=3, activation='relu'),
    Flatten(),
    Dense(10, activation='softmax')
])"""

def g5():
    return """model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])"""

def g6():
    return """model.fit(X_train, y_train,
          validation_data=(X_test, y_test),
          epochs=1,
          batch_size=128)"""

def g7():
    return """index = 0
sample_image = X_test[index]
prediction = model.predict(np.expand_dims(sample_image, axis=0))
predicted_class = np.argmax(prediction)
actual_class = np.argmax(y_test[index])"""

def g8():
    return """plt.figure(figsize=(3,3))
plt.imshow(sample_image.reshape(28,28), cmap='gray')
plt.title(f"Predicted: {predicted_class}, Actual: {actual_class}")
plt.axis('off')
plt.show()"""


def g():
    return "Practical 7: CNN for MNIST Digit Classification"

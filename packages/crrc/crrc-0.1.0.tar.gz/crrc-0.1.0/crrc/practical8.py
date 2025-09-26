def h1():
    return """import keras
from keras.datasets import mnist
from keras import layers
import numpy as np
import matplotlib.pyplot as plt"""

def h2():
    return """(X_train, _), (X_test, _) = mnist.load_data()
X_train = X_train.astype('float32') / 255.
X_test = X_test.astype('float32') / 255.
X_train = X_train[..., np.newaxis]
X_test = X_test[..., np.newaxis]"""

def h3():
    return """noise_factor = 0.5
X_train_noisy = np.clip(X_train + noise_factor * np.random.normal(size=X_train.shape), 0, 1)
X_test_noisy = np.clip(X_test + noise_factor * np.random.normal(size=X_test.shape), 0, 1)"""

def h4():
    return """plt.figure(figsize=(20, 2))
for i in range(10):
    ax = plt.subplot(1, 10, i+1)
    plt.imshow(X_test_noisy[i].squeeze(), cmap='gray')
    ax.axis('off')
plt.show()"""

def h5():
    return """input_img = keras.Input(shape=(28, 28, 1))
x = layers.Conv2D(32, 3, activation='relu', padding='same')(input_img)
x = layers.MaxPooling2D(2, padding='same')(x)
x = layers.Conv2D(32, 3, activation='relu', padding='same')(x)
encoded = layers.MaxPooling2D(2, padding='same')(x)

x = layers.Conv2D(32, 3, activation='relu', padding='same')(encoded)
x = layers.UpSampling2D(2)(x)
x = layers.Conv2D(32, 3, activation='relu', padding='same')(x)
x = layers.UpSampling2D(2)(x)
decoded = layers.Conv2D(1, 3, activation='sigmoid', padding='same')(x)"""

def h6():
    return """autoencoder = keras.Model(input_img, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')"""

def h7():
    return """autoencoder.fit(X_train_noisy, X_train,
                epochs=1,
                batch_size=128,
                validation_data=(X_test_noisy, X_test))"""

def h8():
    return """predictions = autoencoder.predict(X_test_noisy)
plt.figure(figsize=(20, 2))
for i in range(10):
    ax = plt.subplot(1, 10, i+1)
    plt.imshow(predictions[i].squeeze(), cmap='gray')
    ax.axis('off')
plt.show()"""


def h():
    return "Practical 8: Autoencoder for Image Denoising"

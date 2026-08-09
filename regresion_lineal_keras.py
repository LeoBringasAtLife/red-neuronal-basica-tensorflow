import tensorflow as tf
from tensorflow import keras
import numpy as np

# Datos falsos
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
xs = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# Red neuronal de 1 neurona
modelo =  keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
modelo.compile(optimizer='sgd', loss='mean_squared_error')

# Predice cuántos es 10
print(modelo.predict(np.array([10.0])))

# Output: [[9.8863735]]

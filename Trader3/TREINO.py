#https://www.tensorflow.org/guide/keras/train_and_evaluate
from tensorflow.keras.layers import Dense
from tensorflow.keras import layers, Sequential
import tensorflow as tf
from sklearn.neighbors import KNeighborsRegressor

import pickle
import PREPRO

dados = PREPRO.preparar()  # X_train, X_test, y_train, y_test, tabelax, tabelay

# KNR
modelo = KNeighborsRegressor(n_neighbors=3)
modelo.fit(dados[0], dados[2])
pickle.dump(modelo, open('Tabelas/knr.sav', 'wb'))

# TENSOR
modelo = Sequential()
modelo.add(layers.Flatten())
modelo.add(layers.Dense(1, kernel_initializer="random_uniform",
           bias_initializer="random_uniform"))

modelo.add(layers.Dropout(0.2))

modelo.add(Dense(5,activation=layers.LeakyReLU(alpha=0.1)
))
modelo.add(layers.Dropout(0.1))


callback = tf.keras.callbacks.EarlyStopping(
    monitor='loss', patience=10, mode='auto')

modelo.compile(loss='MSLE', optimizer='Nadam', metrics=['accuracy'])

modelo.fit(dados[0], dados[2], batch_size=64, epochs=100,
                  verbose=2, validation_data=(dados[1], dados[3]))



modelo.save('Tabelas')

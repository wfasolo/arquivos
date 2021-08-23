# https://www.tensorflow.org/guide/keras/train_and_evaluate
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
modelo.add(layers.Dense(256, kernel_initializer="random_uniform",
           bias_initializer="random_uniform"))

modelo.add(layers.Dropout(0.2))
modelo.add(Dense(15, activation='relu'))
modelo.add(Dense(12, activation='selu'))
modelo.add(layers.Dropout(0.1))
#modelo.add(Dense(6, activation=layers.LeakyReLU(alpha=0.1)))
#modelo.add(layers.Dropout(0.1))
modelo.add(Dense(3))



callback = tf.keras.callbacks.EarlyStopping(
    monitor='loss', patience=10, mode='auto')
opt = tf.keras.optimizers.RMSprop(learning_rate=0.00001)

modelo.compile(loss='MSE', optimizer="Nadam", metrics=['accuracy'])

modelo.fit(dados[0], dados[2], batch_size=64, epochs=1500,
           verbose=2, validation_data=(dados[1], dados[3]))

#results = modelo.evaluate(dados[1][:-200], dados[3][:-200], batch_size=128)

modelo.save('Tabelas')

print("test loss, test acc:", results)
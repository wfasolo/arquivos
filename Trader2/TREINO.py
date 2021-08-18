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
modelo.add(Dense(28, activation="relu"))
modelo.add(Dense(64, activation="elu"))
modelo.add(Dense(32, activation="selu"))
modelo.add(Dense(16))
modelo.add(Dense(4))

callback = tf.keras.callbacks.EarlyStopping(monitor='loss', min_delta=0.01)
opt = tf.keras.optimizers.RMSprop(learning_rate=0.00001)
modelo.compile(loss='MAE', optimizer=opt, metrics=['accuracy'])

modelo.fit(dados[0], dados[2], batch_size=64, epochs=100,
           verbose=2, validation_data=(dados[1], dados[3]))

modelo.save('Tabelas')


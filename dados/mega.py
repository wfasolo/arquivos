import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np

dad = pd.read_csv('mega.csv')
dados = pd.DataFrame(
    {'conc': dad.concurso, '1d': dad.d1, '2d': dad.d2, '3d': dad.d3, '4d': dad.d4, '5d': dad.d5, '6d': dad.d6})
X = dados.drop('conc', axis=1).to_numpy()

from sklearn.preprocessing import MinMaxScaler
MinMaxScaler = MinMaxScaler()
X = MinMaxScaler.fit_transform(X)

X_train,y_train = X[:-1],X[1:]




model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(160, activation='relu', input_shape=[6]),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation='linear')
])


model.compile(optimizer='adam',
              loss='mean_absolute_error',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=20, batch_size=1, verbose=1)
# model.fit(X_train, y_train, epochs=10)
y_pred = model.predict(X_test)

print(y_pred)

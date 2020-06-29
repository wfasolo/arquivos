# Import Required Libraries
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras

df = pd.read_csv('a.csv')
print(df)

print(df.corr())
df['tipo'] = df['tipo'].map({True: 1, False: 0})
print(len(df.loc[df['tipo'] == 1]))

X = df.drop(columns=('valor')).values
y = df['valor'].values

# Splitting the data set for training and validating
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)

y_train = minmax_scale(y_train)
y_test = minmax_scale(y_test)

X_train = tf.keras.utils.normalize(X_train, axis=1)
X_test = tf.keras.utils.normalize(X_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=5, batch_size=1, verbose=1,validation_data=(X_test, y_test))
# model.fit(X_train, y_train, epochs=10)
predictions = model.predict(X_test)
print('First prediction:', predictions[0])

score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
print(X_test)


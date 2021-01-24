
# https://www.infoq.com/br/news/2019/06/tensorflow-chrome-dinosaur-game/

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.svm import SVC
import tensorflow as tf
from tensorflow import keras



jogadas = pd.DataFrame()
jogada = []


def a(jogadas):
    for pos in range(5):
        jogada.append((pos+1))

        jogadas = pd.DataFrame(
            [[pd.Series(jogada).values, [pos+1]]]).append(jogadas, ignore_index=True)

    return jogadas


jogadas = a(jogadas)
# print(jogadas[0][1:]) #todos menos o ultimo
# print(jogadas[1][:-1]) #todos menos o primeiro

(X_train, y_train) = (jogadas[0][1:], jogadas[1][:-1])

a = []
b = pd.DataFrame()
c = [[1], [2], [3], [4], [5]]
for i in range(5):

    a.append(i)
    b = b.append([a], ignore_index=True)

b = b.fillna(0)

model1 = KNeighborsClassifier(n_neighbors=(1))
model1.fit(b, c)

ultimo = [b.T[len(b)-1].values]
print('ggg', ultimo)

previsao = model1.predict(ultimo)

print('a', previsao)

model = SVC(kernel='rbf', gamma='auto', probability=True)
model.fit(b, c)
print(b)
# Fazer previsoes
y_pred = model.predict(ultimo)
print('b', y_pred)

model = tf.keras.models.Sequential([tf.keras.layers.Dense(16, activation='relu', input_shape=(
    5,)), tf.keras.layers.Dropout(0.2), tf.keras.layers.Dense(6)])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

ultimo = [jogadas.T[len(jogadas)-1].values]
print(np.ravel(c))
print(ultimo)
#model.fit(b.values, np.ravel(c), epochs=10)
y_pred = model.predict([ultimo])

print(y_pred)


model1 = tf.keras.models.Sequential()
model1.add(tf.keras.layers.Flatten())
model1.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model1.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model1.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model1.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model1.fit(b.values, np.ravel(c), epochs=5, batch_size=1, verbose=1)
# model.fit(X_train, y_train, epochs=10)
predictions = model1.predict([[1,2,3,4,5]])
print('First prediction:', predictions[0])



# https://www.infoq.com/br/news/2019/06/tensorflow-chrome-dinosaur-game/
# https://www.digitalocean.com/community/tutorials/como-construir-uma-rede-neural-para-reconhecer-digitos-manuscritos-com-o-tensorflow-pt

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.svm import SVC
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

arquivo = open('/home/casa/Documentos/arquivos/jogos/modelos/a.txt', 'r')
dados = pd.read_fwf(arquivo,index_col=0)
arquivo.close()

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
b=pd.DataFrame(dados.values)


c = [[1], [2], [3], [4], [5],[1], [2], [3], [4], [5],[1], [2], [3], [4], [5]]
for i in range(5):
  
    a.append(i)
    b = b.append([a], ignore_index=True)
    
b = b.fillna(0)
print(b)

ultimo = [b.T[len(b)-1].values]
ultimo = list(np.ravel(ultimo))

xv = [[1, 2, 3, 4, 5]]
yv = [[6]]

model3 = Sequential()
model3.add(Dense(125, input_shape=(5,), activation="relu"))
model3.add(Dense(75, activation="relu"))
model3.add(Dense(1, activation="relu"))

optimizer = tf.keras.optimizers.RMSprop(0.001)

model3.compile(loss='MSE',
               optimizer='adam',
               metrics=['mse'])

model3.fit(b.values, np.ravel(c), batch_size=128,
           epochs=10, verbose=0) #validation_data=(xv, yv)

predictions = model3.predict([[0, 1, 2, 3, 4]])
print(predictions[0][0])
print(round(predictions[0][0]), 0)

arquivo = open('/home/casa/Documentos/arquivos/jogos/modelos/a.txt', 'w')
arquivo.write(str(b))
arquivo.close()
print(b)

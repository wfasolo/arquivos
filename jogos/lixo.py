
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.svm import SVC


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

import numpy as np
import pandas as pd
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
print('ggg',ultimo)

previsao = model1.predict(ultimo)

print('a',previsao)

model = SVC(kernel='rbf', gamma='auto', probability=True)
model.fit(b,c)
print(b)
# Fazer previsoes
y_pred = model.predict(ultimo)
print('b',y_pred)


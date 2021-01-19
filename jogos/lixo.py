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

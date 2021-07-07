from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np 
import DADOS2
import RECALC
import GRAF2

previsao2 = []

dados = RECALC.REC(DADOS2.TAB()['tabela'].drop(['Data', 'Hora'], axis=1)/1000)


def TREINO(dados):
    model1 = KNeighborsRegressor(n_neighbors=2)
    model1.fit(dados['X_train'], dados['y_train'])

    # Fazer previsoes
    previsao = model1.predict(dados['ultimo'])

    return previsao


for i in range(15):
    previsao = TREINO(dados)
    previsao2.extend(previsao)

    dados = pd.DataFrame(np.append(dados['X_train'],previsao,axis= 0))
    dados=RECALC.REC(dados)  



prev = pd.DataFrame(previsao2, columns=[
    'Open', 'Close', 'High', 'Low'])

GRAF2.graf(prev)

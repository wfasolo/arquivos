from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import DADOS2
import RECALC
import GRAF2
import os
os.system('cls' if os.name == 'nt' else 'clear')

emp = input("Empresa 'PETR4.SA': ") or "PETR4.SA"
per = input("Periodo '15 dias': ") or "15d"
inter = input("Intervalo '1 dia': ") or "1d"

previsao2 = []

dados = DADOS2.TAB(emp, per, inter)[
    'tabela'].drop(['Data', 'Hora'], axis=1)/1000

dados_rec = RECALC.REC(dados)


def TREINO(dados_T):
    model1 = KNeighborsRegressor(n_neighbors=2)
    model1.fit(dados_T['X_train'], dados_T['y_train'])

    # Fazer previsoes
    previsao = model1.predict(dados_T['ultimo'])

    return previsao


for i in range(5):
    previsao = TREINO(dados_rec)
    previsao2.extend(previsao)
    print(dados)
    previsao = pd.DataFrame(previsao, columns=[
        'Open', 'Close', 'High', 'Low'])
    dados = dados.append(previsao, ignore_index=True)

    dados_rec = RECALC.REC(dados)


prev = pd.DataFrame(previsao2, columns=[
    'Open', 'Close', 'High', 'Low'])

GRAF2.graf(prev)

# https://www.deeplearningbook.com.br/reconhecimento-de-imagens-com-redes-neurais-convolucionais-em-python-parte-4/
from numpy.core.defchararray import mod
from pandas.core.series import Series
from sklearn import metrics
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import requests

import tensorflow as tf
from tensorflow.keras import layers, Sequential
from tensorflow.keras.layers import Dense



######################
url = "https://brapi.ga/api/quote/RADL3?interval=1d&range=10y"
resp = requests.request("GET", url)

dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.json_normalize(dados)
dados = dados.dropna()
dados_limpo = dados.drop(['volume', 'date'], axis=1)
dados_limpo = pd.DataFrame(
    [dados_limpo['open'], dados_limpo['close'], dados_limpo['high'], dados_limpo['low']]).T


# print(pd.to_datetime((dados['date']*1000000000)-3600000000000*3))

tabela = dados_limpo.values
tab_x = []
tab_y = []

tamanho = len(tabela)
volta = 0
while volta != tamanho-3:
    tab2 = []
    for ii in range(volta, volta+3):
        tab2.extend(tabela[ii])
    volta += 1

    tab_y.extend([tabela[ii+1]])
    tab_x.extend([tab2])

tabelax1 = pd.DataFrame(tab_x)
tabelay1 = pd.DataFrame(tab_y)
####################
######################
url = "https://brapi.ga/api/quote/BRDT3?interval=1d&range=10y"
resp = requests.request("GET", url)

dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.json_normalize(dados)
dados = dados.dropna()
dados_limpo = dados.drop(['volume', 'date'], axis=1)
dados_limpo = pd.DataFrame(
    [dados_limpo['open'], dados_limpo['close'], dados_limpo['high'], dados_limpo['low']]).T


# print(pd.to_datetime((dados['date']*1000000000)-3600000000000*3))

tabela = dados_limpo.values
tab_x = []
tab_y = []

tamanho = len(tabela)
volta = 0
while volta != tamanho-3:
    tab2 = []
    for ii in range(volta, volta+3):
        tab2.extend(tabela[ii])
    volta += 1

    tab_y.extend([tabela[ii+1]])
    tab_x.extend([tab2])

tabelax2 = pd.DataFrame(tab_x)
tabelay2 = pd.DataFrame(tab_y)
####################
######################
url = "https://brapi.ga/api/quote/ITUB4?interval=1d&range=10y"
resp = requests.request("GET", url)

dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.json_normalize(dados)
dados = dados.dropna()
dados_limpo = dados.drop(['volume', 'date'], axis=1)
dados_limpo = pd.DataFrame(
    [dados_limpo['open'], dados_limpo['close'], dados_limpo['high'], dados_limpo['low']]).T


# print(pd.to_datetime((dados['date']*1000000000)-3600000000000*3))

tabela = dados_limpo.values
tab_x = []
tab_y = []

tamanho = len(tabela)
volta = 0
while volta != tamanho-3:
    tab2 = []
    for ii in range(volta, volta+3):
        tab2.extend(tabela[ii])
    volta += 1

    tab_y.extend([tabela[ii+1]])
    tab_x.extend([tab2])

tabelax3 = pd.DataFrame(tab_x)
tabelay3 = pd.DataFrame(tab_y)
####################
######################
url = "https://brapi.ga/api/quote/PETR3?interval=1d&range=10y"
resp = requests.request("GET", url)

dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.json_normalize(dados)
dados = dados.dropna()
dados_limpo = dados.drop(['volume', 'date'], axis=1)
dados_limpo = pd.DataFrame(
    [dados_limpo['open'], dados_limpo['close'], dados_limpo['high'], dados_limpo['low']]).T


# print(pd.to_datetime((dados['date']*1000000000)-3600000000000*3))

tabela = dados_limpo.values
tab_x = []
tab_y = []

tamanho = len(tabela)
volta = 0
while volta != tamanho-3:
    tab2 = []
    for ii in range(volta, volta+3):
        tab2.extend(tabela[ii])
    volta += 1

    tab_y.extend([tabela[ii+1]])
    tab_x.extend([tab2])

tabelax4 = pd.DataFrame(tab_x)
tabelay4 = pd.DataFrame(tab_y)
####################

tabelax = pd.concat([tabelax1, tabelax2, tabelax3, tabelax4])
tabelay = pd.concat([tabelay1, tabelay2, tabelay3, tabelay4])

X_train, X_test, y_train, y_test = train_test_split(
    tabelax.values, tabelay.values, test_size=0.3)


ultimo = tab_x[-1:]

#X_train = np.asarray(pd.DataFrame(X_train).astype(np.float32))

model3 = Sequential()


model3.add(layers.Flatten())
model3.add(layers.Dense(256, kernel_initializer="random_uniform",
           bias_initializer="random_uniform", activation="softmax"))
model3.add(Dense(128, activation="exponential"))
model3.add(Dense(64, activation="softplus"))
model3.add(Dense(32, activation="softsign"))
model3.add(Dense(16, activation="selu"))

model3.add(Dense(4, ))


model3.compile(loss='MSE', optimizer='adam', metrics=['accuracy'])


model3.fit(X_train, y_train, batch_size=100, epochs=1000,
           verbose=2, validation_data=(X_test, y_test))


# Fazer previsoes
y_pred = model3.predict(X_test)

t_y_pred = pd.DataFrame(y_pred)
print(t_y_pred)


t_y_test = pd.DataFrame(y_test)
print(t_y_test)


# Fazer previsoes
previsao = model3.predict(ultimo)

print(pd.DataFrame(previsao))
print(pd.DataFrame(tab_y[-1:]))

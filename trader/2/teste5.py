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
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

######################
url = "https://brapi.ga/api/quote/VALE3?interval=1d&range=10y"
resp = requests.request("GET", url)

dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.json_normalize(dados)
dados = dados.dropna()
dados_limpo = dados.drop(['volume', 'date'], axis=1)
dados_limpo=pd.DataFrame([dados_limpo['open'],dados_limpo['close'],dados_limpo['high'],dados_limpo['low']]).T


#print(pd.to_datetime((dados['date']*1000000000)-3600000000000*3))

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

tabelax1=pd.DataFrame(tab_x)
tabelay1=pd.DataFrame(tab_y)
####################
######################
url = "https://brapi.ga/api/quote/PETR4?interval=1d&range=10y"
resp = requests.request("GET", url)

dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.json_normalize(dados)
dados = dados.dropna()
dados_limpo = dados.drop(['volume', 'date'], axis=1)
dados_limpo=pd.DataFrame([dados_limpo['open'],dados_limpo['close'],dados_limpo['high'],dados_limpo['low']]).T


#print(pd.to_datetime((dados['date']*1000000000)-3600000000000*3))

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

tabelax2=pd.DataFrame(tab_x)
tabelay2=pd.DataFrame(tab_y)
####################

tabelax=pd.concat([tabelax1,tabelax2])
tabelay=pd.concat([tabelay1,tabelay2])

X_train, X_test, y_train, y_test = train_test_split(
    tabelax.values, tabelay.values, test_size=0.5)


ultimo = tab_x[-1:]

#X_train = np.asarray(pd.DataFrame(X_train).astype(np.float32))

model3 = Sequential()

model3.add(Dense(16, input_shape=(pd.DataFrame(tab_x[-1:]).shape[1],)))
model3.add(Dense(288, activation="softmax"))
model3.add(Dense(288, activation="relu"))
model3.add(Dense(144, activation="elu"))
model3.add(Dense(16, activation="elu"))


model3.add(Dense(4))

optimizer = tf.keras.optimizers.RMSprop(0.001)

model3.compile(loss='MSE', optimizer='adam', metrics=['mse'])


model3.fit(X_train, y_train, batch_size=128, epochs=1000, verbose=1,validation_data=(X_test,y_test))




# Fazer previsoes
y_pred = model3.predict(X_test)

t_y_pred=pd.DataFrame(y_pred)
print(t_y_pred)


t_y_test=pd.DataFrame(y_test)
print(t_y_test)



# Fazer previsoes
previsao = model3.predict(ultimo)

print(pd.DataFrame(previsao))
print(pd.DataFrame(tab_y[-1:]))




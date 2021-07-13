import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import requests


url = "https://brapi.ga/api/quote/petr4?interval=1d&range=15d"

resp = requests.request("GET", url)

dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.json_normalize(dados)
dados = dados.dropna()
dados_limpo = dados.drop(['volume', 'date'], axis=1)

#print(pd.to_datetime((dados['date']*1000000000)-3600000000000*3))

tabela = dados_limpo.values
tab_x = []
tab_y = []

tamanho = len(tabela)
volta = 0
while volta != tamanho-3:
    tab2 = []
    for ii in range(volta, volta+3):
        tab2.extend([tabela[ii]])
    volta += 1

    tab_y.extend([tabela[ii+1]])
    tab_x.extend([tab2])


tabela_x = pd.DataFrame(tab_x, columns=['x1', 'x2', 'x3'])
tabela_x['y1'] = tab_y


(X_train, y_train) = (pd.DataFrame(tab_x[:-1]).values, pd.DataFrame(tab_y[1:]).values)
ultimo = X_train[-1:]
print(X_train.view())
X_train = np.asarray(pd.DataFrame(X_train).astype(np.float32))
print(X_train)

model3 = Sequential()
model3.add(tf.keras.layers.Reshape((4,1)))
model3.add(Dense(112))
model3.add(Dense(220, activation="softmax"))
model3.add(Dense(100, activation="relu"))
model3.add(Dense(100, activation="elu"))


model3.add(Dense(4))

optimizer = tf.keras.optimizers.RMSprop(0.001)

#model3.compile(loss='MSE', optimizer='adam', metrics=['mse'])


adam = tf.keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
model3.compile(loss='mean_squared_error', optimizer=adam)


model3.fit([X_train], y_train, batch_size=256, epochs=200, verbose=1)


# Fazer previsoes
previsao2 = []

previsao = model3.predict(ultimo)
print(previsao)
# https://www.deeplearningbook.com.br/reconhecimento-de-imagens-com-redes-neurais-convolucionais-em-python-parte-4/

from sklearn.model_selection import train_test_split


import pandas as pd
import requests

import tensorflow as tf
from tensorflow.keras import layers, Sequential
from tensorflow.keras.layers import Dense

#####

tabelax = tabelay = pd.DataFrame()

empresa = ["VALE3", "PETR3", "ABEV3", "ASAI3", "AZUL4", "B3SA3", "BIDI11", "BBSE3", "BRML3", "BBDC3", "BBDC4", "BRAP4", "BBAS3", "BRKM5", "BRFS3", "BPAC11", "CRFB3", "CCRO3", "CMIG4", "HGTX3", "CIEL3",
           "COGN3", "CPLE6", "CSAN3", "CPFE3", "CVCB3", "CYRE3", "ECOR3", "ELET3", "ELET6", "EMBR3", "ENBR3", "ENGI11", "ENEV3", "EGIE3", "EQTL3", "EZTC3", "FLRY3", "GGBR4", "GOAU4", "GOLL4", "NTCO3", "HAPV3", "HYPE3"]

######################
for i in range(len(empresa)):
    ticker = empresa[i]
    print(ticker)
    url = "https://brapi.ga/api/quote/"+ticker+"?interval=1d&range=1y"
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
    tabelax = pd.concat([tabelax, tabelax1], ignore_index=True)
    tabelay = pd.concat([tabelay, tabelay1], ignore_index=True)


#####


X_train, X_test, y_train, y_test = train_test_split(
    tabelax.values, tabelay.values, test_size=0.1)


ultimo = tab_x[-1:]

#X_train = np.asarray(pd.DataFrame(X_train).astype(np.float32))

model3 = Sequential()


model3.add(layers.Flatten())
model3.add(layers.Dense(256, kernel_initializer="random_uniform",
           bias_initializer="random_uniform"))
model3.add(Dense(128,activation="relu"))
model3.add(Dense(64, activation="elu"))
model3.add(Dense(32))
model3.add(Dense(16))

model3.add(Dense(4))

callback = tf.keras.callbacks.EarlyStopping(monitor='loss', min_delta=0.01)

model3.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])


model3.fit(X_train, y_train, batch_size=100, epochs=100,
           verbose=2, validation_data=(X_test, y_test), callbacks=[callback])


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

from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go
import pandas as pd
import requests


url = "https://brapi.ga/api/quote/petr4?interval=1d&range=5d"

resp = requests.request("GET", url)

dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.io.json.json_normalize(dados)
dados=dados.dropna()
dados_limpo = dados.drop(['volume', 'date'], axis=1)

print(pd.to_datetime((dados['date']*1000000000)-3600000000000*3))

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
print (tabela_x)

trace1 = {
    'x': pd.to_datetime((dados['date']*1000000000)-3600000000000*3),
    'open': dados['open'],
    'close': dados['close'],
    'high': dados['high'],
    'low': dados['low'],
    'type': 'candlestick',

    'showlegend': False
}

data = [trace1]
layout = go.Layout()

fig = go.Figure(data=data, layout=layout)
fig.show()

scaler = MinMaxScaler()
scaler.fit(dados_limpo)
dados_limpo=scaler.transform(dados_limpo)
print(tab_x)
(X_train, y_train) = (tab_y[:-1], tab_x[1:])

ultimo = y_train[-1:]
print('ultimo: ',X_train)


#model1 = RandomForestClassifier(max_depth=2, random_state=0)
model1 = KNeighborsRegressor(n_neighbors=5)
model1.fit(X_train, y_train)

# Fazer previsoes
previsao = model1.predict(ultimo)

print("previsao: ",scaler.inverse_transform(previsao))

from numpy.core.defchararray import mod
from sklearn import metrics
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go
import pandas as pd
import requests


url = "https://brapi.ga/api/quote/vale3?interval=1d&range=1y"

resp = requests.request("GET", url)

dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.io.json.json_normalize(dados)
dados = dados.dropna()
dados_limpo = dados.drop(['volume', 'date'], axis=1)
dados_limpo=pd.DataFrame([dados_limpo['open'],dados_limpo['close'],dados_limpo['high'],dados_limpo['low']]).T


#print(pd.to_datetime((dados['date']*1000000000)-3600000000000*3))

tabela = dados_limpo.values
tab_x = []
tab_y = []

tamanho = len(tabela)
volta = 0
while volta != tamanho-4:
    tab2 = []
    for ii in range(volta, volta+4):
        tab2.extend(tabela[ii])
    volta += 1

    tab_y.extend([tabela[ii+1]])
    tab_x.extend([tab2])




X_train, X_test, y_train, y_test = train_test_split(
    tab_x, tab_y, test_size=0.2)


ultimo = tab_x[-1:]


#model1 = RandomForestClassifier(max_depth=2, random_state=0)
model1 = KNeighborsRegressor(n_neighbors=4)

model1.fit(X_train, y_train)

# Fazer previsoes
y_pred = model1.predict(X_test)

t_y_pred=pd.DataFrame(y_pred)
print(t_y_pred)


t_y_test=pd.DataFrame(y_test)
print(t_y_test)

print(model1.score(X_test,y_test))

trace1 = {
    'x': pd.Series(range(len(t_y_pred[0]))),
    'open': t_y_pred[0],
    'close': t_y_pred[1],
    'high': t_y_pred[2],
    'low': t_y_pred[3],
    'type': 'candlestick',

    'showlegend': False
}

trace2 = {
    'x': pd.Series(range(len(t_y_test[0]))),
    'open': t_y_test[0],
    'close': t_y_test[1],
    'high': t_y_test[2],
    'low': t_y_test[3],
    'type': 'candlestick',

    'showlegend': False
}

data = [trace1,trace2]
layout = go.Layout()
fig = go.Figure(data=data, layout=layout)
fig.show()


y_pred = model1.predict(ultimo)
print(ultimo)
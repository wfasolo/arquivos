import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


dados = yf.download(  # or pdr.get_data_yahoo(...
    # tickers list or string as well
    tickers=["PETR4.SA", "VALE3.SA"],

    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period="1y",

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')
    interval="1d",

    # group by ticker (to access via data['SPY'])
    # (optional, default is 'column')
    group_by='ticker',

    # adjust all OHLC automatically
    # (optional, default is False)
    auto_adjust=True,

    # download pre/post regular market hours data
    # (optional, default is False)
    prepost=True,

    # use threads for mass downloading? (True/False/Integer)
    # (optional, default is True)
    threads=True,

    # proxy URL scheme use use when downloading?
    # (optional, default is None)
    proxy=None
)

df = pd.DataFrame(dados["PETR4.SA"])
df = df.dropna()
df = df
dd = pd.to_datetime((df.index).values, format="%Y-%d-%m %H:%M:%S")
dd = (dd.strftime('%H:%M %d-%m-%y'))
dd = pd.to_datetime(dd.values, format="%H:%M %d-%m-%y")


tabela = pd.DataFrame([dd, df.Open*1000, df.Close*1000, df.High*1000, df.Low*1000], index=[
                      'Data', 'Open', 'Close', 'High', 'Low']).T


tabela.Open, tabela.Close = (tabela.Open.astype(int), tabela.Close.astype(int))
tabela.High, tabela.Low = (tabela.High.astype(int), tabela.Low.astype(int))

X = tabela.drop(['Data'], axis=1)


(X_train, y_train) = (X[:-1].values, X[1:].values)
ultimo = y_train[-1:]

# Tainan model
model1 = KNeighborsClassifier(n_neighbors=(1))
model1.fit(X_train, y_train)

# Fazer previsoes
previsao2 = []
previsao = model1.predict(ultimo)
previsao2.extend(previsao/1000)
for i in range(30):
    previsao = model1.predict(previsao)
    previsao2.extend(previsao/1000)


previsao2 = pd.DataFrame(previsao2)

trace1 = {
    'x': pd.Series(range(len(previsao2))),
    'open': previsao2[0],
    'close': previsao2[1],
    'high': previsao2[2],
    'low': previsao2[3],
    'type': 'candlestick',

    'showlegend': False
}


data = [trace1]
layout = go.Layout()

fig = go.Figure(data=data, layout=layout)
fig.show()
print(previsao2)

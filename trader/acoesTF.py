from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

from sklearn import metrics
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go

data = yf.download(  # or pdr.get_data_yahoo(...
    # tickers list or string as well
    tickers="MGLU3.SA",

    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period="1mo",

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')
    interval="1h",

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

df = pd.DataFrame(data)
df=df.dropna()
dd = pd.to_datetime((df.index).values, format="%Y-%d-%m %H:%M:%S")
dd = (dd.strftime('%H%M'))
# plotar o gráfico de candlestick
trace1 = {
    'x': dd,
    'open': df.Open,
    'close': df.Close,
    'high': df.High,
    'low': df.Low,
    'type': 'candlestick',

    'showlegend': False
}


data = [trace1]
layout = go.Layout()

fig = go.Figure(data=data, layout=layout)
# fig.show()


y = df.Open
X = pd.DataFrame(dd).astype(int)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.01, shuffle=True)



model3 = Sequential()
model3.add(Dense(1, input_shape=(1,)))
model3.add(Dense(250, activation="softmax"))
model3.add(Dense(200, activation="relu"))
model3.add(Dense(100, activation="elu"))


model3.add(Dense(1))

optimizer = tf.keras.optimizers.RMSprop(0.001)

model3.compile(loss='MSE', optimizer='adam', metrics=['mse'])

model3.fit(X.values, y.values, batch_size=128, epochs=300, verbose=0)

predictions = model3.predict([1000,1100,1200,1300,1400,1500,1600])

print(y)
print(predictions)

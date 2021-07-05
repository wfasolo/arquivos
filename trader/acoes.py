import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "PETR4.SA VALE",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "1d",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "15m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

df=pd.DataFrame(data.VALE)
dd=pd.to_datetime((df.index).values, format="%Y-%d-%m %H:%M:%S")
dd=(dd.strftime('%H:%M'))
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
fig.show()
import plotly.graph_objects as go
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import yfinance as yf
import pandas as pd


def TAB(emp,per,ent):
    dados = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers=[emp],

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period=per,

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval=ent,

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

    #, start="2021-06-20", end="2021-07-05"
    
    )

    df = pd.DataFrame(dados)
    df = df.dropna()

    dd = pd.to_datetime((df.index).values, format="%Y-%d-%m %H:%M:%S")
    hora = (dd.strftime('%H:%M'))

    tabela = pd.DataFrame([hora, dd, df.Open*1000, df.Close*1000, df.High*1000, df.Low*1000], index=[
        'Hora', 'Data', 'Open', 'Close', 'High', 'Low']).T

    filt = tabela[tabela['Hora'] == '20:00'].index
    tabela.drop(filt, inplace=True)

    tabela.Open, tabela.Close = (
        tabela.Open.astype(int), tabela.Close.astype(int))
    tabela.High, tabela.Low = (tabela.High.astype(int), tabela.Low.astype(int))

    return {'tabela': tabela}

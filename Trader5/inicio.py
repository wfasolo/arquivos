import pandas as pd
import numpy as np
import requests
from tqdm import tqdm
import mplfinance as fplt
from datetime import date, timedelta, datetime
import time


per = input("Periodo '5d': ") or "5d"
inter = input("Intervalo '5m': ") or "5m"

tabela = pd.DataFrame()
data_atual = date.today()  # - timedelta(days=1)

url = "https://brapi.ga/api/available?search="
resp = requests.request("GET", url)

stocks = pd.DataFrame(resp.json())
stocks = stocks.sort_values('stocks')
empresa = np.array(stocks['stocks'])


def f_url(ticker):
    try:
        url = "https://brapi.ga/api/quote/"+ticker+"?interval="+inter+"&range="+per
        resp = requests.get(url, timeout=5)
        dados = pd.DataFrame(resp.json())
        dados = dados['results'][0]['historicalDataPrice']
        dados = pd.json_normalize(dados)
        dados = dados.dropna()

    except:
        dados = [[0]]
        print("erro")

    return dados


def tab(dados):
    if len(dados) >= 10:

        dados['date'] = pd.to_datetime(dados['date']-10800, unit='s')
        dados_ant = dados.loc[dados["date"].dt.date != data_atual]
        dados_atual = dados.loc[dados["date"].dt.date == data_atual]
        media20 = dados_ant['close'][-20:].mean()
        media200 = dados_ant['close'][-200:].mean()
        atual_c = dados_atual['close'][:1]
        anterior_c = dados_ant['close'][-1:]
        atual_o = dados_atual['open'][:1]
        anterior_o = dados_ant['open'][-1:]
        cor = atual_c.values/atual_o.values
        movel = dados['close'].rolling(21).mean()
        

        if atual_o.empty == False and \
                atual_o.values >= anterior_c.values and \
                atual_o.values >= anterior_o.values and \
                atual_o.values >= [media20] and\
                atual_o.values >= [media200] and cor[0] >= [1.003]:

            print(ticker, ' ', cor)
            tabela = pd.concat(
                [dados_ant[-10:], dados_atual[:50]], ignore_index=True)
            tabela.index = pd.to_datetime(tabela['date'], unit='s')
            movel = movel[-len(tabela):]
            mavdf = pd.DataFrame(
                dict(aber=atual_o.values, m20=media20, m200=media200), index=tabela.index)
            mavdf['movel']=movel.values
            grafico(tabela, mavdf)

        return atual_o


def grafico(tabela, mavdf):

    ap = fplt.make_addplot(mavdf, type='line')

    fplt.plot(
        tabela,
        type='candle',
        style='charles',
        block=True,
        title='Empresa: '+ticker,
        ylabel='Price ($)',
        addplot=ap,
        #mav=(11),
        vlines=data_atual
    )


teste = tab(f_url('vale3'))
while teste.empty == True:
    print(datetime.now())
    time.sleep(30)
    teste = tab(f_url('vale3'))

for i in range(len(empresa)):
    ticker = empresa[i]

    tab(f_url(ticker))

time.sleep(10)

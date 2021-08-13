import pandas as pd
import numpy as np
import requests
from tqdm import tqdm
import mplfinance as fplt
from datetime import date
import time


per = "15d"
inter = "5m"

tabela = pd.DataFrame()
data_atual = '2021-08-12'
print(data_atual)

url = "https://brapi.ga/api/quote/"+"VALE3"+"?interval="+inter+"&range="+per
resp = requests.get(url, timeout=5)
dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.json_normalize(dados)
dados = dados.dropna()


time.sleep(0.5)


if len(dados) >= 10:

    dados['date'] = pd.to_datetime(dados['date']-10800, unit='s')
    dados_ant = dados.loc[dados["date"].dt.date != data_atual]
    dados_atual = dados.loc[dados["date"].dt.date == data_atual]
    media20 = dados_ant['close'][-20:].mean()
    media200 = dados_ant['close'][-200:].mean()
    tabela = dados_ant[-10:]
    tabela.index = pd.to_datetime(tabela['date'], unit='s')

    AAPL1 = tabela

    mavdf = pd.DataFrame(
        dict(m20=media20, m200=media200), index=tabela.index)

    ap = fplt.make_addplot(mavdf, type='line')

    fplt.plot(tabela, type='candle', vlines=data_atual,
              mav=(2), addplot=ap)

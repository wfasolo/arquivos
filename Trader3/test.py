import pandas as pd
import numpy as np
import requests
from tqdm import tqdm
import mplfinance as fplt
from datetime import date, timedelta, datetime
import time

ticker='PETR4'
per = input("Periodo '5d': ") or "5d"
inter = input("Intervalo '5m': ") or "5m"

tabela = pd.DataFrame()
data_atual = date.today()  # - timedelta(days=1)

url = "https://brapi.ga/api/available?search="
resp = requests.request("GET", url)

stocks = pd.DataFrame(resp.json())
stocks = stocks.sort_values('stocks')
empresa = np.array(stocks['stocks'])

url = "https://brapi.ga/api/quote/"+ticker+"?interval="+inter+"&range="+per
resp = requests.get(url, timeout=5)
dados = pd.DataFrame(resp.json())
dados = dados['results'][0]['historicalDataPrice']
dados = pd.json_normalize(dados)
dados = dados.dropna()


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
    movel=dados['close'].rolling(21).mean()
    movel=movel[-len(tabela):]

    if atual_o.empty == False:


        tabela = pd.concat(
            [dados_ant[-10:], dados_atual[:50]], ignore_index=True)
        tabela.index = pd.to_datetime(tabela['date'], unit='s')
      
        
        mavdf = pd.DataFrame(
            dict(aber=atual_o.values, m20=media20, m200=media200), index=tabela.index)
        mavdf['movel']=movel.values


print(mavdf)


plt.plot(df['close'], label='Close')

plt.plot(df['close'].rolling(21).mean(), label='MA 21 days')
plt.legend(loc='best')

plt.show()

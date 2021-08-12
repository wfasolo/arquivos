import pandas as pd
import numpy as np
import requests
from tqdm import tqdm
import mplfinance as fplt
from datetime import date
import time


per = input("Periodo '5d': ") or "5d"
inter = input("Intervalo '5m': ") or "5m"

tabela = pd.DataFrame()
data_atual = date.today()

url = "https://brapi.ga/api/available?search="
resp = requests.request("GET", url)

stocks = pd.DataFrame(resp.json())
empresa = np.array(stocks['stocks'])

for i in range(len(empresa)):
    ticker = empresa[i]

    try:
        url = "https://brapi.ga/api/quote/"+ticker+"?interval="+inter+"&range="+per
        resp = requests.get(url, timeout=15)
        dados = pd.DataFrame(resp.json())
        dados = dados['results'][0]['historicalDataPrice']
        dados = pd.json_normalize(dados)
        dados = dados.dropna()

        if len(dados) >= 1:

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
            
            if((atual_o.values and atual_c.values) >\
                    (anterior_c.values and anterior_o.values and [media20] and [media200])) and cor[0] > [1.003]:
                print(ticker,' ',cor)
                tabela = pd.concat(
                    [dados_ant[-10:], dados_atual[:10]], ignore_index=True)
                tabela.index = pd.to_datetime(tabela['date'], unit='s')

                fplt.plot(
                    tabela,
                    type='candle',
                    style='charles',
                    block=True,
                    title='Empresa: '+ticker,
                    ylabel='Price ($)'
                )

    except:
        dados = [[0]]
        print("erro")

    time.sleep(0.5)

time.sleep(10)

import pandas as pd
import numpy as np
import requests
from tqdm import tqdm
import time
import os

os.system('clear')


tab = []
tabela = pd.DataFrame()


url = "https://brapi.ga/api/available?search="
resp = requests.request("GET", url)

stocks = pd.DataFrame(resp.json())
stocks = stocks.sort_values('stocks')
empresa = np.array(stocks['stocks'])

for i in tqdm(range(len(empresa))):
    erro = 0
    while erro != 3:
        try:
            ticker = empresa[i]
            url = "https://brapi.ga/api/quote/"+ticker
            resp = requests.get(url, timeout=5000)
            dados = pd.DataFrame(resp.json())
            dados = dados['results'][0]
            dados = pd.json_normalize(dados)
            dados = dados.dropna()

            tab.extend(
                [[dados['symbol'][0], dados['averageDailyVolume10Day'][0], dados['longName'][0]]])
            erro = 3
        except:
            erro += 1
            print(erro, ' ', ticker)
            time.sleep(2)
            os.system('clear')


tabela = pd.DataFrame(tab, columns=['symbol', 'volume', 'nome']).sort_values(
    'volume', ascending=False)
tabela = tabela.reset_index()
tabela = tabela.drop('index', axis=1)
tabela.to_pickle('Tabelas/empresas100')
print(tabela)

import pandas as pd
import numpy as np
import requests
from tqdm import tqdm
import time


per = input("Periodo '15d': ") or "15d"
inter = input("Intervalo '1d': ") or "1d"
normal = input("Normalizar? (S/n): ") or "n"

tabelax = tabelay = pd.DataFrame()


url = "https://brapi.ga/api/available?search="
resp = requests.request("GET", url)

stocks = pd.DataFrame(resp.json())
empresa = np.array(stocks['stocks'])
empresa=['petr4']

for i in tqdm(range(len(empresa))):
    ticker = empresa[i]

    try:
        url = "https://brapi.ga/api/quote/"+ticker+"?interval="+inter+"&range="+per
        resp = requests.get(url, timeout=15)
    except:
        print(resp)
    time.sleep(0.5)
    try:
        dados = pd.DataFrame(resp.json())
        dados = dados['results'][0]['historicalDataPrice']
        dados = pd.json_normalize(dados)
        dados = dados.dropna()
        dados.to_pickle('Tabelas/tabtest')
        dados=dados/dados['open'].median()

    except :
        dados=[[0]]
        print("erro")
        
  

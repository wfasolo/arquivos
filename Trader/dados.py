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
    except :
        dados=[[0]]
        print("erro")
        
    if len(dados) >= 10:
        dados_limpo = pd.DataFrame(
            [dados['open'], dados['close'], dados['high'], dados['low']]).T
        dados_limpo=(round(dados_limpo,3))

        # print(pd.to_datetime((dados['date']*1000000000)-3600000000000*3))

        tabela = dados_limpo.values
        tab_x = []
        tab_y = []

        tamanho = len(tabela)
        volta = 0
        while volta != tamanho-3:
            tab2 = []
            tab3 = []
            for ii in range(volta, volta+3):
                tab2.extend(tabela[ii])
                tab3.extend(tabela[ii+1])
            volta += 1

            tab_y.extend([tab3])
            tab_x.extend([tab2])

        tabelax1 = pd.DataFrame(tab_x)
        tabelay1 = pd.DataFrame(tab_y)

        tabelax = pd.concat([tabelax, tabelax1], ignore_index=True)
        tabelay = pd.concat([tabelay, tabelay1], ignore_index=True)
    else:
        print(ticker)

if normal == 'S' or normal == 's':
    for i in tqdm(range(len(tabelay))):
        tabelax.iloc[i] = (tabelax.iloc[i]/tabelax.iloc[i, 0])
        tabelay.iloc[i] = (tabelay.iloc[i]/tabelay.loc[i, 0])

tabelax.to_pickle('Tabelas/tabelax')
tabelay.to_pickle('Tabelas/tabelay')
print(len(tabelay))
print(tabelax)
print(tabelay)



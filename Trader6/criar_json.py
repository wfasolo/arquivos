import pandas as pd
import requests
import time
import os

tab_json = {}


def ler_json(tickers,inter,per):
    erro = 0
    while erro != 3:
        try:

            url = "https://brapi.ga/api/quote/"+tickers+"?interval="+inter+"&range="+per
            resp = requests.get(url, timeout=50000)
            time.sleep(3)
            erro = 3

        except:
            erro += 1
            print(erro, ' ', os.error)
            time.sleep(2)
            os.system('clear')

    dados = resp.json()

    for i in range(len(dados['results'])):

        d = dados['results'][i]['historicalDataPrice']
        s = dados['results'][i]['symbol']


        tab_json.update({i: {'symbol': s, 'dados': d}})

    return tab_json


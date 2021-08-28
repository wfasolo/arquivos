
import pandas as pd
import requests
import time
import os

per = input("Periodo '15d': ") or "15d"
inter = input("Intervalo '1d': ") or "1d"

tabelax = tabelay = pd.DataFrame()


def ler_ticker(ii):
    b = ""
    tb = pd.read_pickle('Tabelas/empresas100')

    for i in range(0+ii, 20+ii):
        a = (tb['symbol'][i])
        if i < 19+ii:
            b = a+','+b
        else:
            b = b+a

    ticker = [b]
    tickers = ticker[0]
    return tickers


def ler_json(tickers):
    erro = 0
    while erro != 3:
        try:

            url = "https://brapi.ga/api/quote/"+tickers+"?interval="+inter+"&range="+per
            resp = requests.get(url, timeout=50000)
            tabela = pd.DataFrame(resp.json())
            time.sleep(3)
            erro = 3

        except:
            erro += 1
            print(erro, ' ', os.error)
            time.sleep(2)
            os.system('clear')

    return tabela


def criar_tab(tabela, i):
    dados = tabela['results'][i]['historicalDataPrice']
    dados2 = pd.json_normalize(dados)
    dados3 = dados2.dropna()
    dados3['symbol'] = tabela['results'][i]['symbol']
    return dados3


def tab_treino(dadost, tabelax):
    if len(dadost) >= 1:
        dadost.index = pd.to_datetime(dadost['date'])
        tabelax = pd.concat([tabelax, dadost], ignore_index=True)
        print(dadost)
    else:
        print("Erro")

    return tabelax


def salvar_tab(tabelax):
    print(len(tabelax))

    tabelax.to_pickle('Tabelas/tabelas')


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
    dados3['ticker'] = tabela['results'][i]['symbol']
    return dados3


def tab_treino(dadost, tabelax, tabelay):
    if len(dadost) >= 1:

        """media=dadost['open'].max()
        dadost.index=pd.to_datetime(dadost['date']*1e9-1.08e+13)
        dadost['open']=dadost['open']/media
        dadost['close']=dadost['close']/media
        dadost['low']=dadost['low']/media
        dadost['high']=dadost['high']/media
        dadost['volume']=dadost['volume']/dadost['volume'].max()"""

        dados_limpo = pd.DataFrame(
            [dadost['cor'], dadost['corpo'],dadost['dist']]).T

        #dadost.index = pd.to_datetime(dadost['date'])

        tabela = dados_limpo.values

        tab_x = []
        tab_y = []

        tamanho = len(tabela)
        volta = 0
        while volta != tamanho-5:
            tab2 = []
            tab3 = []
            for ii in range(volta, volta+5):
                tab2.extend(tabela[ii])
            volta += 1

            tab_y.extend([tabela[ii+1]])
            tab_x.extend([tab2])

        tabelax1 = pd.DataFrame(tab_x)
        tabelay1 = pd.DataFrame(tab_y)

        tabelax = pd.concat([tabelax, tabelax1], ignore_index=True)
        tabelay = pd.concat([tabelay, tabelay1], ignore_index=True)
    else:
        print("Erro")

    return tabelax, tabelay


def salvar_tab(tabelax, tabelay):
    print((tabelax))
    print((tabelay))
    #tabelay = tabelay.drop([4], axis=1)
    tabelax.to_pickle('Tabelas/tabelax')
    tabelay.to_pickle('Tabelas/tabelay')

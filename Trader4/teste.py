from numpy import modf
import pandas as pd
import mplfinance as fplt
import requests


'''
tab = pd.DataFrame([[15, 30, 10, 25], [25, 30, 20, 30],
                   [25, 30, 15, 25], [15, 40, 10, 10]])
dat = ['8-20-2021', '8-21-2021', '8-22-2021', '8-23-2021']
tab.index = pd.to_datetime(dat)
tab.columns = ['open', 'high', 'low', 'close']

url = "https://brapi.ga/api/quote/petr4?interval=1h&range=15d"
resp = requests.get(url, timeout=50000)
tabela = pd.DataFrame(resp.json())
dados = tabela['results'][0]['historicalDataPrice']
dados2 = pd.json_normalize(dados)
dados3 = dados2.dropna()

tab = dados3.loc[dados3['volume'] != 0]

tab.index = pd.to_datetime(tab['date'])
'''


def converter(tab):
    tabelas = []
    cor_ant = 0
    #tab = tab.loc[tab['volume'] != 0]

    try:
            
        for i in range(1,len(tab)):
            tipo = 0
            open = tab['open'][i]#/tab['high'].mean()
            high = tab['high'][i]#/tab['high'].mean()
            low = tab['low'][i]#/tab['high'].mean()
            close = tab['close'][i]#/tab['high'].mean()
            volume = tab['volume'][i]#/tab['volume'].mean()
            cores = close/open
            sombra = high-low
            # cor
            if cores < 1:
                cor = -1
                corpo = (open-close)
                sl = (close-low)
                sh = (high-low)
            if cores == 1:
                cor = 0
                corpo = 0
                sl = (open-low)
                sh = (high-close)
            if cores > 1:
                cor = 1
                corpo = (close-open)
                sl = (open-low)
                sh = (high-close)

            # tipo
            if sl == sh:
                tipo = 5
            if sl < sh:
                tipo = 4
            if sl > sh:
                tipo = 3
            if sl == 0 and sh > 0:
                tipo = 2
            if sl > 0 and sh == 0:
                tipo = 1

            if cor_ant == -1 or cor_ant == 0:
                if cor == -1 or cor == 0:
                    dist = tab['open'][i]-tab['open'][i-1]
                else:
                    dist = tab['close'][i]-tab['open'][i-1]
            else:
                if cor == -1 or cor == 0:
                    dist = tab['open'][i]-tab['close'][i-1]
                else:
                    dist = tab['close'][i]-tab['close'][i-1]
            cor_ant = cor
            tabelas.extend([[cor, corpo, dist]])
        # print({'cor': cor, 'tipo': tipo, 'corpo': corpo, 'sombra': sombra})
    except:
        print('erro')
    tabelas = pd.DataFrame(
        tabelas, columns=['cor', 'corpo',  'dist'])
    #tabelas['corpo'] = tabelas['corpo']/tabelas['sombra'].mean()
    #tabelas['sombra'] = tabelas['sombra']/tabelas['sombra'].mean()
    

    return tabelas

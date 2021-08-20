import pandas as pd
import requests

tabelax = pd.DataFrame()
tab_x = []


def ret(ticker, per, inter):
    url = "https://brapi.ga/api/quote/"+ticker+"?interval="+inter+"&range="+per
    resp = requests.request("GET", url)

    dados = pd.DataFrame(resp.json())
    dados = dados['results'][0]['historicalDataPrice']
    dados = pd.json_normalize(dados)
    dados = dados.dropna()
    dat=dados['date']
    #dados=dados/dados['open'].median()
    dados['date']=dat
    

    if ((dados['open'][-1:].values == dados['close'][-1:].values) and
            (dados['high'][-1:].values == dados['low'][-1:].values)):
        dados = dados[:-1]


    dados_limpo = pd.DataFrame(
        [dados['open'], dados['close'], dados['high'], dados['low'], dados['volume']]).T
    
    tab = dados_limpo.values

    for i in range(len(tab)-3, len(tab)):
        tab_x.extend(tab[i])

    valor = pd.DataFrame(tab_x).T

    print (valor)
    return (valor, dados)

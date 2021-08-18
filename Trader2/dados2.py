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
    dados=dados/dados['open'].max()

    if ((dados['open'][-1:].values == dados['close'][-1:].values) and
            (dados['high'][-1:].values == dados['low'][-1:].values)):
        dados = dados[:-1]

    dados_limpo = dados.drop(['volume'], axis=1)
    dados_limpo = pd.DataFrame(
        [dados_limpo['open'], dados_limpo['close'], dados_limpo['high'], dados_limpo['low']]).T

    tab = dados_limpo.values

    for i in range(len(tab)-3, len(tab)):
        tab_x.extend(tab[i])

    valor = pd.DataFrame(tab_x).T

    valor = valor/valor[0][0]
    print (valor)
    return (valor, dados['date'])

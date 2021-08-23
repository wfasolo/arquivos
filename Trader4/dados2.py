import pandas as pd
import requests
import teste

tabelax = pd.DataFrame()
tab_x = []


def ret(ticker, per, inter):
    url = "https://brapi.ga/api/quote/"+ticker+"?interval="+inter+"&range="+per
    resp = requests.request("GET", url)

    dados = pd.DataFrame(resp.json())
    dados = dados['results'][0]['historicalDataPrice']
    dados = pd.json_normalize(dados)
    dados=dados[:-1]
    dados = dados.dropna()
    dadost=teste.converter(dados)

    dados_limpo = pd.DataFrame(
            [dadost['cor'], dadost['corpo'],dadost['dist']]).T

    tab = dados_limpo.values
    print(dados_limpo)

    for i in range(len(tab)-5, len(tab)):
        tab_x.extend(tab[i])

    valor = pd.DataFrame(tab_x).T

    return (valor, dados)

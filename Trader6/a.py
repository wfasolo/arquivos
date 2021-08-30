
import pandas as pd
import criar_json
import ler100
import criar_tab2
import grafico

tb = pd.read_pickle('Tabelas/empresas100')

per = input("Periodo '1d': ") or "1d"
inter = input("Intervalo '1d': ") or "1d"
for ii in range(0,100,20):
    Ticker=ler100.ler_ticker(ii)
    print(Ticker)
    tab_json=criar_json.ler_json(Ticker,inter,per)

    for i in range(len(tab_json)):
        try:
            ticker=empresa=(tab_json[i]['symbol'])
            empresa=tb['nome'].loc[tb['symbol']==tab_json[i]['symbol']]
            empresa=empresa.values
            dados=(tab_json[i]['dados'])
            dados2=pd.json_normalize(dados)

            grafico.graf(ticker,empresa[0], criar_tab2.tab(dados2))
        except:
            f=0


import pandas as pd
import criar_json
import ler100
import criar_tab
import grafico

per = input("Periodo '1d': ") or "1d"
inter = input("Intervalo '1d': ") or "1d"

Ticker=ler100.ler_ticker(1)
print(Ticker)
tab_json=criar_json.ler_json(Ticker,inter,per)

for i in range(len(tab_json)):
    try:
        empresa=(tab_json[i]['symbol'])
        dados=(tab_json[i]['dados'])
        dados2=pd.json_normalize(dados)
        dados2= dados2.dropna()
        grafico.graf(empresa, criar_tab.tab(dados2))
    except:
        f=0

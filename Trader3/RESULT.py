import pandas as pd
import pickle
import dados2
from tensorflow.keras import models
import mplfinance as fplt

ticker = input("Empresa: ") or "PETR4"
per = input("Periodo '1d': ") or "1d"
inter = input("Intervalo '15m': ") or "15m"

if inter == "5m":
    tp = 300
if inter == "15m":
    tp = 900
if inter == "30m":
    tp = 1800
if inter == "1h":
    tp = 3600
if inter == "1d":
    tp = 86400


valor = dados2.ret(ticker, per, inter)


def prever(ultimo, modelo, bloco, IA):
    # Fazer previsoes
    for ii in range(1):
        previsao = modelo.predict(ultimo)

        resultado = pd.DataFrame(previsao)
        tt = pd.DataFrame()

        for i in range(0, (len(resultado.T)-3), 4):
            tt2 = pd.DataFrame([resultado[i].values, resultado[i+1].values,
                                resultado[i+2].values, resultado[i+3].values, resultado[i+4].values]).T

            tt = pd.concat([tt, tt2], ignore_index=True)

        tt2 = []
        for i in range(1, len(tt)):
            tt2.extend(tt.iloc[i])

        ultimo = [tt2]

    data = []

    val = valor[1][-3:].drop(['date'], axis=1)
    val.columns = [0, 1, 2, 3, 4]

    tt = pd.concat([val, tt], ignore_index=True)

    for dd in range(len(tt)):
        data.extend((valor[1]['date'][-3:-2])+tp*dd)
    data = pd.DataFrame(data)

    frame = pd.DataFrame(tt.values, columns=[
                         'Open', 'High', 'Low', 'Close', 'Volume'])
    frame = frame.set_index(data[0])
    frame.index = pd.to_datetime(frame.index-10800, unit='s')

    print(frame)

    fplt.plot(
        frame,
        type='candle',
        style='charles',
        block=bloco,
        title=IA+' / '+ticker,
        volume=True,
        ylabel='Price ($)'
    )


# KNR
ultimo = valor[0]
modelo = pickle.load(open('Tabelas/knr.sav', 'rb'))
prever(ultimo, modelo, False, 'KNR')

# Tensor
ultimo = valor[0]
modelo = models.load_model('Tabelas')
prever(ultimo, modelo, True, 'Tensor')

# GRAF.graf(valor)

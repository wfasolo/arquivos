import pandas as pd
import pickle
import GRAF
import dados2
from tensorflow.keras import models
import mplfinance as fplt

ticker = input("Empresa: ") or "PETR4"
per = input("Periodo '1d': ") or "1d"
inter = input("Intervalo '15m': ") or "15m"

if inter == "15m":
    tp = 900
if inter == "30m":
    tp = 1800
if inter == "1h":
    tp = 3600
if inter == "1d":
    tp = 86400


valor = dados2.ret(ticker, per, inter)


def prever(ultimo, modelo, bloco):
    # Fazer previsoes
    for ii in range(1):
        previsao = modelo.predict(ultimo)
        resultado = pd.DataFrame(previsao)
        tt = pd.DataFrame()

        for i in range(0, (len(resultado.T)-3), 4):
            tt2 = pd.DataFrame([resultado[i].values, resultado[i+1].values,
                                resultado[i+2].values, resultado[i+3].values]).T

            tt = pd.concat([tt, tt2], ignore_index=True)

        #tt = pd.concat([tt, pd.DataFrame(previsao)], ignore_index=True)

        tt2 = []
        for i in range(1, len(tt)):
            tt2.extend(tt.iloc[i])

        ultimo = [tt2]

    data = []

    val = valor[1][-3:].drop(['date'], axis=1)
    val.columns = [0, 1, 2, 3]

    tt = pd.concat([val, tt], ignore_index=True)

    for dd in range(len(tt)):
        data.extend((valor[1]['date'][-3:-2])+tp*dd)
    data = pd.DataFrame(data)

    frame = pd.DataFrame(tt.values, columns=['Open', 'Close', 'High', 'Low'])
    frame = frame.set_index(data[0])
    frame.index = pd.to_datetime(frame.index-10800, unit='s')
    frame = (round(frame, 2))
    print(frame)

    fplt.plot(
        frame,
        type='candle',
        style='charles',
        block=bloco,
        title='KNR / '+ticker,
        ylabel='Price ($)'
    )


# KNR
ultimo = valor[0]
modelo = pickle.load(open('Trader/Tabelas/knr.sav', 'rb'))
prever(ultimo, modelo, False)

# Tensor
ultimo = valor[0]
modelo = models.load_model('Trader/Tabelas')
prever(ultimo, modelo, True)

# GRAF.graf(valor)

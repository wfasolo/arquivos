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


# KNR
ultimo = valor[0]
modelo = pickle.load(open('Tabelas/knr.sav', 'rb'))
previsao = modelo.predict(ultimo)
print(previsao)

# Tensor
ultimo = valor[0]
modelo = models.load_model('Tabelas')
previsao = modelo.predict(ultimo)
print(previsao)
# GRAF.graf(valor)

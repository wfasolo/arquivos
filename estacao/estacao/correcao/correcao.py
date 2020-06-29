import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from datetime import datetime

score_Temp2 = 0
score_Pres2 = 0
score_Umid2 = 0

url_weather = 'https://api.weather.com/v1/geocode/-21.129/-41.677/forecast/hourly/48hour.json?units=m&language=pt-BR&apiKey=320c9252a6e642f38c9252a6e682f3c6'

url_station = "https://api.thinger.io/v1/users/wfasolo/buckets/dados_estacao1/data?authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJ0b2tlbl9lc3RfYmQiLCJ1c3IiOiJ3ZmFzb2xvIn0.6FnVjOdAxWpRGwNrVc1RwKtQPaZNNeCqlj3yZDcn-2U"


# Dados site weather.com
resp = requests.get(url_weather)
weather_json = resp.json()
weather_pd = pd.DataFrame(weather_json['forecasts'])
weather_df = pd.DataFrame([(weather_pd.fcst_valid-10800), weather_pd.mslp, weather_pd.hi,
                           weather_pd.rh], index=['dt', 'Pres', 'Temp', 'Umid']).T
weather_df.reset_index(inplace=True, drop=True)
weather_df.dropna()

# Dados estação
resp = requests.get(url_station)
station_json = resp.json()
station_pd = pd.DataFrame(station_json)
station = station_pd['val'].values
station_df = pd.io.json.json_normalize(station)
station_df = pd.DataFrame(station_df)
station_df = station_df.dropna()

# hora
hora = pd.DataFrame()
for i in range(24):
    hora[i] = [datetime.utcfromtimestamp(weather_df['dt'][i]).strftime(
        "%d/%m/%Y"), datetime.utcfromtimestamp(weather_df['dt'][i]).strftime("%H h")]
hora = hora.T

# Concatenar
station = station_df.drop(['Chuv'], axis=1)
station = station.round(2)
inv_station = station[::-1]
weather_df = weather_df.drop(['dt'], axis=1)
dados = pd.concat([inv_station[-20:], weather_df[:24]], ignore_index=True)
intervalo = pd.concat([pd.DataFrame(np.arange(1, 11, 0.5)), pd.DataFrame(
    np.arange(11, 35, 1))], ignore_index=True)


# generate a model of polynomial features
for i in range(2, 20):
    poly = PolynomialFeatures(degree=i, include_bias=False)

    # transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
    X_ = poly.fit_transform(intervalo)
    y_Temp = dados['Temp']
    y_Pres = dados['Pres']
    y_Umid = dados['Umid']

    # criando e treinando o modelo
    model_Temp = LinearRegression()
    model_Pres = LinearRegression()
    model_Umid = LinearRegression()

    model_Temp.fit(X_, y_Temp)
    model_Pres.fit(X_, y_Pres)
    model_Umid.fit(X_, y_Umid)

    pred_Temp = (model_Temp.predict(X_))
    pred_Pres = (model_Pres.predict(X_))
    pred_Umid = (model_Umid.predict(X_))

    score_Temp = model_Temp.score(X_, y_Temp)
    score_Pres = model_Pres.score(X_, y_Pres)
    score_Umid = model_Umid.score(X_, y_Umid)

    if score_Temp > score_Temp2:
        score_Temp2 = score_Temp
        pred_Temp2 = pd.DataFrame(pred_Temp).round(1)
        i_Temp = i

    if score_Pres > score_Pres2:
        score_Pres2 = score_Pres
        pred_Pres2 = pd.DataFrame(pred_Pres).round(1)
        i_Pres = i

    if score_Umid > score_Umid2:
        score_Umid2 = score_Umid
        pred_Umid2 = pd.DataFrame(pred_Umid).round(1)
        i_Umid = i


print(i_Temp, score_Temp2.__round__(4))
print(i_Pres, score_Pres2.__round__(4))
print(i_Umid, score_Umid2.__round__(4))

corrigido = pd.DataFrame([hora[1].values, pred_Pres2[0][-24:], pred_Temp2[0]
                          [-24:], pred_Umid2[0][-24:]], index=['hora', 'Pres', 'Temp', 'Umid']).T

print(corrigido)

plt.plot(corrigido['hora'], corrigido['Temp'])
plt.xticks(rotation=90)
plt.show()
plt.plot(corrigido['hora'], corrigido['Pres'])
plt.xticks(rotation=90)
plt.show()
plt.plot(corrigido['hora'], corrigido['Umid'])
plt.xticks(rotation=90)
plt.show()


trace = go.Scatter(x=corrigido['hora'],
                   y=corrigido['Temp'],
                   text=corrigido['Temp'],
                   textposition='top center',
                   mode='lines+markers+text',
                   showlegend=False)

trace2 = go.Bar(x=corrigido['hora'],
                y=corrigido['Temp'],
                marker_color='LightBlue',
                opacity=0.5,
                showlegend=False
                )

data_temp = [trace, trace2]
py.plot(data_temp)

station_df.to_csv('mu.csv')

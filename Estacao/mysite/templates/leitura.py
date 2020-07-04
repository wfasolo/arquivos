import pandas as pd
import numpy as np
import requests
from datetime import datetime

def ler():

    url_weather = 'https://api.weather.com/v1/geocode/-21.129/-41.677/forecast/hourly/48hour.json?units=m&language=pt-BR&apiKey=320c9252a6e642f38c9252a6e682f3c6'

    url_station = "https://api.thinger.io/v1/users/wfasolo/buckets/dados_estacao1/data?items=0&authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJidWNrZXQiLCJ1c3IiOiJ3ZmFzb2xvIn0.CrjRqDEFx4KDVCnkOTJtVjnZlkHehO0M_TGE3KEPZ10"


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
    print(station_df)
    
    return {'dados': dados, 'intervalo': intervalo,'hora':hora,'estacao':station_df}

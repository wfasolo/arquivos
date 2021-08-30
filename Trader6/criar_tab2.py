import pandas as pd

import mplfinance as fplt
from datetime import date, timedelta, datetime
import time

a = 0


def tab(dados):

    if len(dados) >= 10:

        movel20 = dados['low'].rolling(20).mean()
        movel200 = dados['high'].rolling(200).mean()
        dados['movel20'] = movel20
        dados['movel200'] = movel200
        dados['media'] = dados['movel20']-dados['movel200']
        dados = dados.dropna().reset_index(drop=True)

        for i in range(1, len(dados)):
            global a
            if ((dados['media'][i] > 0 and dados['media'][i-1] < 0) or (dados['media'][i] < 0 and dados['media'][i-1] > 0)):
                a = i

        dados['date'] = pd.to_datetime(dados['date']-10800, unit='s')
        dados = dados.set_index(dados['date'])
        dados.index = pd.to_datetime(dados['date'], unit='s')

        mavdf = pd.DataFrame(dados['movel20'], index=dados['date'])
        mavdf['move200'] = dados['movel200']

    if dados['media'][a] > 0:
        
        return dados, mavdf, dados['date'][a]

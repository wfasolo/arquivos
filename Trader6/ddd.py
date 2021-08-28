import pandas as pd

import mplfinance as fplt
from datetime import date, timedelta, datetime
import time


data_atual = date.today()  - timedelta(days=1)



def tab(dados):

    if len(dados) >= 10:
       
        
        dados['date'] = pd.to_datetime(dados['date']-10800, unit='s')
        dados_ant = dados.loc[dados["date"].dt.date != data_atual]
        dados_atual = dados.loc[dados["date"].dt.date == data_atual]
        media20 = dados_ant['close'][-20:].mean()
        media200 = dados_ant['close'][-200:].mean()
        atual_c = dados_atual['close'][:1]
        anterior_c = dados_ant['close'][-1:]
        atual_o = dados_atual['open'][:1]
        anterior_o = dados_ant['open'][-1:]
        cor = atual_c.values/atual_o.values
        movel = dados['close'].rolling(21).mean()

        if atual_o.empty == False and cor[0] >= [1.003]:

            tabela = pd.concat(
                [dados_ant[-10:], dados_atual[:50]], ignore_index=True)
            tabela.index = pd.to_datetime(tabela['date'], unit='s')
            movel = movel[-len(tabela):]
            mavdf = pd.DataFrame(
                dict(aber=atual_o.values, m20=media20, m200=media200), index=tabela.index)
            mavdf['movel'] = movel.values
         

        return tabela, mavdf,data_atual


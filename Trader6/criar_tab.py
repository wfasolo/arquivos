import pandas as pd

import mplfinance as fplt
from datetime import date, timedelta, datetime
import time


data_atual = date.today() - timedelta(days=1)


def tab(dados):

    if len(dados) >= 10:

        dados['date'] = pd.to_datetime(dados['date']-10800, unit='s')
        dados_ant = dados.loc[dados["date"].dt.date != data_atual]
        dados_atual = dados.loc[dados["date"].dt.date == data_atual]
        atual_c = dados_atual['close'][:1]
        atual_o = dados_atual['open'][:1]
        anterior_o=dados_ant['open'][-1:]
        cor = atual_c.values/atual_o.values
        movel20 = dados['open'].rolling(21).mean()

        tabela = pd.concat(
            [dados_ant[-10:], dados_atual[:50]], ignore_index=True)
        tabela.index = pd.to_datetime(tabela['date'], unit='s')
        movel20 = movel20[-len(tabela):]
        mavdf = pd.DataFrame(
            dict(fec=anterior_o.values,aber=atual_o.values), index=tabela.index)
        mavdf['movel'] = movel20.values

    if atual_o.empty == False and cor[0] >= [1.00]  and atual_o.values>anterior_o.values and atual_o.values > movel20[10:11].values:
        return tabela, mavdf, data_atual

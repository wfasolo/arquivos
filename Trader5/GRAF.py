import plotly.graph_objects as go
import mplfinance as fplt
import pandas as pd
import tabela as tb


def graf(tabela):

    tabela.index = pd.to_datetime(tabela['date']*1e9-1.08e+13)

    print(tabela)

    fplt.plot(
        tabela,
        type='candle',
        style='charles',
        block=True,
        volume=True,
        # addplot=ap,
        #title='Empresa: ',
        #ylabel='Price ($)',


        mav=(21),
        # vlines=data_atual
    )


emp = input("Empresa 'PETR4': ") or "PETR4"
tj = tb.ler_json(emp)

graf(tb.criar_tab(tj, 0))

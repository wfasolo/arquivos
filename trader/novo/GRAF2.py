import plotly.graph_objects as go
import pandas as pd


def graf(tabela):
    trace1 = {
        'x': pd.Series(range(len(tabela))),
        'open': tabela['Open'],
        'close': tabela['Close'],
        'high': tabela['High'],
        'low': tabela['Low'],
        'type': 'candlestick',

        'showlegend': False
    }

    data = [trace1]
    layout = go.Layout()

    fig = go.Figure(data=data, layout=layout)
    fig.show()

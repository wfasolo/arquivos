import plotly.graph_objects as go
import pandas as pd


def graf(tabela):
    trace1 = {
        'x': pd.Series(range(len(tabela))),
        'open': tabela[0],
        'close': tabela[1],
        'high': tabela[2],
        'low': tabela[3],
        'type': 'candlestick',

        'showlegend': False
    }

    data = [trace1]
    layout = go.Layout()

    fig = go.Figure(data=data, layout=layout)
    fig.show()

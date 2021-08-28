import pandas as pd

def ler_ticker(ii):
    b = ""
    tb = pd.read_pickle('Tabelas/empresas100')

    for i in range(0+ii, 20+ii):
        a = (tb['symbol'][i])
        if i < 19+ii:
            b = a+','+b
        else:
            b = b+a

    ticker = [b]
    tickers = ticker[0]
    return tickers


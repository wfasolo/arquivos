
import mplfinance as fplt


def graf(ticker,dados):
    tabela=dados[0]
    mavdf=dados[1]
    data_atual=dados[2]

    ap = fplt.make_addplot(mavdf, type='line')

    fplt.plot(
        tabela,
        type='candle',
        style='charles',
        block=True,
        title='Empresa: '+ticker,
        ylabel='Price ($)',
        addplot=ap,
        # mav=(11),
        vlines=data_atual
    )

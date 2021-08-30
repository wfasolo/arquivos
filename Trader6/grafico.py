
import mplfinance as fplt


def graf(ticker,empresa, dados):
    tabel = dados[0]
    mavdf = dados[1]
    data_atual = dados[2]

    ap = fplt.make_addplot(mavdf, type='line')

    fplt.plot(
        tabel,
        type='candle',
        style='charles',
        block=True,
        title=empresa+' : '+ticker,
        ylabel='Price ($)',
        addplot=ap,
        # mav=(11),
        vlines=data_atual,
        volume=True
    )

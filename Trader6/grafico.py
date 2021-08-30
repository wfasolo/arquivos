
import mplfinance as fplt


def graf(ticker,empresa, dados):
    tabel = dados[0][-50:]
    mavdf = dados[1][-50:]
    data_atual = dados[2]
    print(tabel)

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
        volume=True,
        figsize =(640,480), 
        #scale_padding=0.2
    )

import pandas as pd
import mplfinance as fplt

tabtest = pd.read_pickle('Tabelas/tabtest')
tabtest['date'] = pd.to_datetime(tabtest['date']-10800, unit='s')
frame=tabtest
frame = frame.set_index(tabtest['date'])
frame.index = pd.to_datetime(tabtest['date'], unit='s')
   

print(frame)
# tabtest=tabtest[-20:].reset_index(drop=True)
movel20 = tabtest['high'].rolling(20).mean()
movel200 = tabtest['high'].rolling(200).mean()
tabtest['media20'] = movel20
tabtest['media200'] = movel200
tabtest['media'] = tabtest['media20']-tabtest['media200']
tabtest = tabtest.dropna().reset_index(drop=True)
# print(tabtest.loc[(tabtest['media']>0.999)&(tabtest['media']<1.0007)])

oa = pd.Series(tabtest['high'][:1])

for i in range(1, len(tabtest['media'])):

    t1 = pd.Series(tabtest['media'][i])
    t2 = pd.Series(tabtest['media'][i-1])

    if (t1.values < 0 and t2.values > 0) or (t1.values > 0 and t2.values < 0):
        print(tabtest['date'][i-1])

    o1 = pd.Series(tabtest['high'][i])

    if o1.values < oa.values:
        oa = o1
        print('anterior ', tabtest['date'][i-1])

#ap = fplt.make_addplot(mavdf, type='line')

fplt.plot(
    frame,
    type='candle',
    style='charles',
    block=True,
    title='Empresa: ',
    ylabel='Price ($)',
    #addplot=ap,
     mav=(20,200),
    #vlines=data_atual,
    volume=True,
    
)

# https://translate.google.com/translate?hl=pt-BR&sl=en&tl=pt&u=https%3A%2F%2Fwww.datacamp.com%2Fcommunity%2Ftutorials%2Ffinance-python-trading&prev=search

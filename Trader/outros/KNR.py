from pandas.core.frame import DataFrame
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go
import pandas as pd
from tqdm import tqdm

prev=[]
t_y_pred=pd.DataFrame()
t_y_test=pd.DataFrame()

###
tabelax = pd.read_pickle('Trader/Tabelas/tabelax')
tabelay = pd.read_pickle('Trader/Tabelas/tabelay')
###


###
X_train, X_test, y_train, y_test = train_test_split(
    tabelax.values, tabelay.values, test_size=0.15)
###

ytr=pd.DataFrame(y_train)
yte=pd.DataFrame(y_test)
print(ytr)

###
for i in range(4):

    #model1 = RandomForestClassifier(max_depth=2, random_state=0)
    modelo = KNeighborsRegressor(n_neighbors=3)

    modelo.fit(X_train, ytr[i])

    # Fazer previsoes
    y_pred = modelo.predict(X_test)

    t_y_pred[i] = pd.DataFrame(y_pred)
    
    t_y_test[i] = pd.DataFrame(yte[i])
  


    # Fazer previsoes
    previsao = modelo.predict(tabelax[-2:-1].values)
 

    prev.extend([previsao[0]])
    
print('real: ',pd.DataFrame(tabelay[-2:-1].values))
print('previsao: ',prev)
resultado=pd.DataFrame(tabelax[-2:-1].values)
tt=pd.DataFrame()
for i in range(0,(len(resultado.T)-3),4):
    tt2=pd.DataFrame([resultado[i].values,resultado[i+1].values,resultado[i+2].values,resultado[i+3].values]).T
    
    tt=pd.concat([tt,tt2], ignore_index=True)

tt=pd.concat([tt,pd.DataFrame(prev).T], ignore_index=True)


print(tt)

trace0 = {
    'x': pd.Series(range(len(tt[0]))),
    'open': tt[0],
    'close': tt[1],
    'high': tt[2],
    'low': tt[3],
    'type': 'candlestick',

    'showlegend': False
}
trace1 = {
    'x': pd.Series(range(len(t_y_pred[0]))),
    'open': t_y_pred[0],
    'close': t_y_pred[1],
    'high': t_y_pred[2],
    'low': t_y_pred[3],
    'type': 'candlestick',

    'showlegend': False
}

trace2 = {
    'x': pd.Series(range(len(t_y_test[0]))),
    'open': t_y_test[0],
    'close': t_y_test[1],
    'high': t_y_test[2],
    'low': t_y_test[3],
    'type': 'candlestick',

    'showlegend': False
}

data = [trace0]
layout = go.Layout()
fig = go.Figure(data=data, layout=layout)
fig.show()


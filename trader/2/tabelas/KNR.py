from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go
import pandas as pd

prev=[]
###
tabelax = pd.read_pickle(
    '/home/cedae/Documentos/arquivos/trader/2/tabelas/tabelax')
tabelay = pd.read_pickle(
    '/home/cedae/Documentos/arquivos/trader/2/tabelas/tabelay')
###

###
X_train, X_test, y_train, y_test = train_test_split(
    tabelax.values/10, tabelay.values/10, test_size=0.2)
###

ytr=pd.DataFrame(y_train)
yte=pd.DataFrame(y_test)


###
for i in range(4):

    #model1 = RandomForestClassifier(max_depth=2, random_state=0)
    modelo = KNeighborsRegressor(n_neighbors=3)

    modelo.fit(X_train, ytr[i])

    # Fazer previsoes
    y_pred = modelo.predict(X_test)

    t_y_pred = pd.DataFrame(y_pred)
    #print(t_y_pred)

    t_y_test = pd.DataFrame(yte[i])
    #print(t_y_test)


    # Fazer previsoes
    previsao = modelo.predict(tabelax[-1:].values/10)
    print(previsao)

    prev.extend([previsao[0]])
    
print(pd.DataFrame(tabelay[-1:].values))
print(prev)

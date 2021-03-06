from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import DADOS
import GRAF

dados=DADOS.TAB()

# Tainan model
model1 = KNeighborsClassifier(n_neighbors=(1))
model1.fit(dados['X_train'],dados['y_train'])

# Fazer previsoes
previsao2 = []
previsao = model1.predict(dados['ultimo'])
previsao2.extend(previsao/1000)
for i in range(5):
    previsao = model1.predict(previsao)
    previsao2.extend(previsao/1000)


prev = pd.DataFrame(previsao2, columns=[
    'Open', 'Close', 'High', 'Low'])

GRAF.graf(prev)
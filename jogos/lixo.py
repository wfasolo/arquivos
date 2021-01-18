from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.svm import SVC

import numpy as np
import pandas as pd
a = []
b = pd.DataFrame()
c = [[1], [2], [3], [4], [5]]
for i in range(5):

    a.append(i)
    b = b.append([a], ignore_index=True)

b = b.fillna(0)

model1 = KNeighborsClassifier(n_neighbors=(1))
model1.fit(b, c)

ultimo = [b.T[len(b)-1].values]

previsao = model1.predict(ultimo)

print('a',previsao)

model = SVC(kernel='rbf', gamma='auto', probability=True)
model.fit(b,c)

# Fazer previsoes
y_pred = model.predict(ultimo)
print('b',y_pred)

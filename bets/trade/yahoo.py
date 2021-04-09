from yahooquery import Ticker
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

X_train = []
yy = []
petr = Ticker('AMZN')

petro = petr.history(period="1d",  interval="90m")

# print(petro)

plt.plot(range(len(petro.high.values)), petro.high.values)
# plt.show()
y_train = petro.high.values
for i in range(len(petro.high.values)):
    X_train.append([i, i])
    yy.append(y_train[i])

X_train = np.array(X_train)
yy=np.array(yy)
# Tainan model
model = RandomForestClassifier(n_estimators=1, n_jobs=-1)

model.fit(X_train, yy)
# Fazer previsoes
#y_pred = model.predict(X_test)

#acur = metrics.accuracy_score(y_test, y_pred)

#previsao = pd.DataFrame(model.predict_proba(prev_trans))

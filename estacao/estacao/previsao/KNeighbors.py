import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics as metrics


def valor(X_train, X_test, y_train, y_test):
    acur = pd.Series()

    for n_n in range(1, 100):

        # Tainan model
        model1 = KNeighborsClassifier(n_neighbors=(n_n))
        model1.fit(X_train, y_train)

        # Fazer previsoes
        y_pred = model1.predict(X_test)

        acur1 = pd.Series(metrics.accuracy_score(y_test, y_pred))
        acur = acur.append(acur1, ignore_index=True)

    return acur

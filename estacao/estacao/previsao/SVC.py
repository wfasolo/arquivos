import pandas as pd
from sklearn import metrics
from sklearn.svm import SVC


def valor(X_train, X_test, y_train, y_test):
    acur = pd.Series()

    for i in range(1, 101):

        # Tainar modelo
        model = SVC(kernel='rbf', gamma=i)
        model.fit(X_train, y_train)

        # Fazer previsoes
        y_pred = model.predict(X_test)

        acur1 = pd.Series(metrics.accuracy_score(y_test, y_pred))
        acur = acur.append(acur1, ignore_index=True)

    return acur

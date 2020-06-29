import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics as metrics


def valor(X_train, X_test, y_train, y_test, atual):
    

    

    # Tainan model
    model = KNeighborsClassifier(n_neighbors=(1))
    model.fit(X_train, y_train)

    # Fazer previsoes
    y_pred = model.predict(X_test)

    acur = metrics.accuracy_score(y_test, y_pred)

    print('KN: ', model.predict_proba(atual))


    return acur

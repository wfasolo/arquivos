from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier


def valor(X_train, X_test, y_train, y_test, prev_trans):

    # Tainar modelo
    model = RandomForestClassifier(n_estimators=1, n_jobs=-1)
    model.fit(X_train, y_train)

    # Fazer previsoes
    y_pred = model.predict(X_test)

    acur = metrics.accuracy_score(y_test, y_pred)

    previsao = model.predict_proba(prev_trans)

    return {'acuracia': acur, 'previsao': previsao}

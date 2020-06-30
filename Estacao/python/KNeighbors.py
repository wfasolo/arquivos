from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics as metrics


def valor(X_train, X_test, y_train, y_test, prev_trans):

    # Tainan model
    model = KNeighborsClassifier(n_neighbors=(1))
    model.fit(X_train, y_train)

    # Fazer previsoes
    y_pred = model.predict(X_test)

    acur = metrics.accuracy_score(y_test, y_pred)

    previsao=model.predict_proba(prev_trans)

    return {'acuracia': acur, 'previsao': previsao}

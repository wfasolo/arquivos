import pandas as pd
from sklearn import metrics
from sklearn.svm import SVC


def valor(X_train, X_test, y_train, y_test, atual):
  

    

    # Tainar modelo
    model = SVC(kernel='rbf', gamma=1, probability=True)
    model.fit(X_train, y_train)

    # Fazer previsoes
    y_pred = model.predict(X_test)

    acur = metrics.accuracy_score(y_test, y_pred)

     
    print('SVC: ', model.predict_proba(atual))
    
    return acur

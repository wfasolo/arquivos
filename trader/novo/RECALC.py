import pandas as pd


def REC(X):
    (X_train, y_train) = (X[:-1].values, X[1:].values)
    ultimo = y_train[-1:]

    return {'X_train': X_train, 'y_train': y_train, 'ultimo': ultimo}

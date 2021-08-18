from sklearn.model_selection import train_test_split
import pandas as pd


def preparar():

    tabelax = pd.read_pickle('Tabelas/tabelax')
    tabelay = pd.read_pickle('Tabelas/tabelay')
    ###
    X_train, X_test, y_train, y_test = train_test_split(
        tabelax.values, tabelay.values, test_size=0.2)
    ###
    return(X_train, X_test, y_train, y_test, tabelax, tabelay)


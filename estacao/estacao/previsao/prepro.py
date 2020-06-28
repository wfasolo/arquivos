import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def dados():

    mu_csv = pd.read_csv('mu.csv', sep=',')

    chuva = pd.DataFrame([mu_csv['Temp'], mu_csv['Pres'],
                          mu_csv['Umid'],  mu_csv['Chuva']], index=['Temp', 'Press', 'Umid', 'Chuv']).T

    chuva = chuva.dropna()
   
    X = chuva.drop(['Chuv'], axis=1)
    y = chuva['Chuv']
    
    atual=chuva.drop(['Chuv'], axis=1)
    atual=atual[-1:]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    atual = scaler.transform(atual)

    return {'X_train': X_train, 'X_test': X_test, 'y_train': y_train, 'y_test': y_test,'atual':atual}

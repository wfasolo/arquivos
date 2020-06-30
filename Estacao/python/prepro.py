import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import correcao

def dados(corrigir,chuva):

   
    chuva=corrigir['estacao']
    previsaoh=corrigir['corrigido']
    previsao = previsaoh.drop(['hora'], axis=1)
  
    X = chuva.drop(['Chuv'], axis=1)
    y = chuva['Chuv']
       
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    previsao = scaler.transform(previsao)

    return {'X_train': X_train, 'X_test': X_test, 'y_train': y_train, 'y_test': y_test,'previsao':previsao}

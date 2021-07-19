# https://www.deeplearningbook.com.br/reconhecimento-de-imagens-com-redes-neurais-convolucionais-em-python-parte-4/

import pandas as pd
from sklearn.model_selection import train_test_split


###
tabelax = pd.read_pickle(
    '/home/cedae/Documentos/arquivos/trader/2/tabelas/tabelax')
tabelay = pd.read_pickle(
    '/home/cedae/Documentos/arquivos/trader/2/tabelas/tabelay')
###
tabelay=pd.DataFrame([tabelay[1]/tabelay[0],tabelay[2]/tabelay[0],tabelay[3]/tabelay[0]]).T
print(tabelay)

def prepara():
    X_train, X_test, y_train, y_test = train_test_split(
        tabelax.values, tabelay.values, test_size=0.1)

    return {'X_train': X_train, 'X_test': X_test, 'y_train': y_train,'y_test': y_test}



import DADOS
import GRAF
import pandas as pd

dados=DADOS.TAB()
tab=pd.DataFrame(dados['X_train'],columns=[
    'Open', 'Close', 'High', 'Low'])
GRAF.graf(tab)
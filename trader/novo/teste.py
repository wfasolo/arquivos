import pandas as pd
import DADOS2

tab_x = []
tab_y = []

dados = DADOS2.TAB("PETR4.SA", "5d","1d")[
    'tabela'].drop(['Data', 'Hora'], axis=1)/1000

print(dados)

tamanho = len(tabela)
volta = 0
while volta != tamanho-3:
    tab2 = []
    for ii in range(volta, volta+3):
        tab2.extend([tabela[ii]])
    volta += 1

    tab_y.extend([tabela[ii+1]])
    tab_x.extend([tab2])


# tab_x=pd.DataFrame(tab_y,columns=['a'])
tab_x = pd.DataFrame(tab_x, columns=['x1', 'x2', 'x3'])
tab_x['y1'] = tab_y

print(tab_x)
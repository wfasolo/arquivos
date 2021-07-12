import pandas as pd

tab_x = []
tab_y = []

tabela = [[0, 0, 0, 0],
          [1, 1, 1, 1],
          [2, 2, 2, 2],
          [3, 3, 3, 3],
          [4, 4, 4, 4],
          [5, 5, 5, 5],
          [6, 6, 6, 6],
          [7, 7, 7, 7],
          [8, 8, 8, 8]]

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
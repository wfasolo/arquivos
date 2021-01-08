#https://www.kaggle.com/dhanushkishore/a-self-learning-tic-tac-toe-program?scriptVersionId=46958713

import pandas as pd
import random

jogador = 1
j1 = pd.Series(0)
j2 = pd.Series(0)


p = [[190, 185],
     [190, 285],
     [190, 385],
     [290, 185],
     [290, 285],
     [290, 385],
     [390, 185],
     [390, 285],
     [390, 385]]


for r in range(0, 19):
    pos = random.randint(0, 8)

    if p[pos] != 0:
        p[pos] = 0
        if jogador == 1:
            j2=pd.Series(pos)
            j1=j1.append(j2, ignore_index=True)
            jogador = 1
        else:
            jogador = 1
        
       

    print(j1)
    if (list(j1[j1 == 1].index) and list(j1[j1 == 2].index) and list(j1[j1 == 3].index)) or (list(j1[j1 == 4].index) and list(j1[j1 == 5].index) and list(j1[j1 == 6].index)):
        print('sim')

 

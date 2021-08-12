import numpy as np
import pandas as pd
import math
import random

prob1 = 0
prob2 = 0
empate = 0
time1 = 2.1
time2 = 1.08
propabilidade = []

poisson1 = [0, 0, 0, 0, 0, 0]
poisson2 = [0, 0, 0, 0, 0, 0]

gols = np.array([[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]).astype(np.float32)

for i in range(0, 6):
    poisson1[i] = (np.exp(-time1)*(time1**i))/math.factorial(i)
    poisson2[i] = (np.exp(-time2)*(time2**i))/math.factorial(i)

for linha in range(0, 6):
    for coluna in range(0, 6):
        gols[linha, coluna] = round(poisson1[linha]*poisson2[coluna]*100, 2)

for linha in range(0, 6):
    for coluna in range(0, 6):
        if linha > coluna:
            prob1 = round(prob1+gols[linha, coluna], 2)
        elif linha == coluna:
            empate = round(empate+gols[linha, coluna], 2)
        elif linha < coluna:
            prob2 = round(prob2+gols[linha, coluna], 2)

print(prob1, empate, prob2)

for i in range(100000):
    aleatorio = random.randrange(0, 100)

    if aleatorio < int(prob1):
        propabilidade.append('casa')

    elif aleatorio < (int(empate)+int(prob1)):
        propabilidade.append('empate')

    else:
        propabilidade.append('fora')


a = pd.Series(propabilidade)
print('casa: ', len(a.loc[a == 'casa']))
print('empate: ', len(a.loc[a == 'empate']))
print('fora: ', len(a.loc[a == 'fora']))


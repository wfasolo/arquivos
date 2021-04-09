import numpy as np
import pandas as pd
import math
import random
import scraping as sc

tabela = sc.scrap()
print(tabela)
perg1 = input("time casa: ")
perg2 = input("time fora: ")
t1 = tabela.loc[tabela['time'] == perg1]
t2 = tabela.loc[tabela['time'] == perg2]

prob1 = 0
prob2 = 0
empate = 0
time1 = t1['ofs'].values[0]*t2['def'].values[0]
time2 = t2['ofs'].values[0]*t1['def'].values[0]
print(round(time1,1), round(time2,1))


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
        gols[linha, coluna] = round(poisson1[linha]*poisson2[coluna]*100, 1)

for linha in range(0, 6):
    for coluna in range(0, 6):
        if linha > coluna:
            prob1 = round(prob1+gols[linha, coluna], 2)
        elif linha == coluna:
            empate = round(empate+gols[linha, coluna], 2)
        elif linha < coluna:
            prob2 = round(prob2+gols[linha, coluna], 2)

print(prob1, empate, prob2)

cs = 0
ep = 0
fr = 0
for ii in range(10000):
    propabilidade = []
    for i in range(3):
        rd = random.randrange(100)

        if rd < prob1:
            propabilidade.append('casa')

        elif rd < (empate+prob1):
            propabilidade.append('empate')

        else:
            propabilidade.append('fora')

    a = pd.Series(propabilidade)
    '''print(" ")
    print('casa: ', len(a.loc[a == 'casa']))
    print('empate: ', len(a.loc[a == 'empate']))
    print('fora: ', len(a.loc[a == 'fora']))'''

    if len(a.loc[a == 'casa']) > len(a.loc[a == 'fora']):
        cs += 1
    elif len(a.loc[a == 'casa']) < len(a.loc[a == 'fora']):
        fr += 1
    else:
        ep += 1


print(gols)
print(np.unravel_index(gols.argmax(), gols.shape))

print(round(cs/ii*100,1), round(ep/ii*100,1), round(fr/ii*100,1))
print(round(1/(cs/ii),1), round(1/(ep/ii),1), round(1/(fr/ii),1))




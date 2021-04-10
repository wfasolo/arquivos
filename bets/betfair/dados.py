import numpy as np
import pandas as pd
import math
import random


def fim(tabela, perg1, perg2):

    t1 = tabela.loc[tabela['time'] == perg1]
    t2 = tabela.loc[tabela['time'] == perg2]

    prob1 = 0
    prob2 = 0
    empate = 0
    time1 = t1['ofs'].values[0]*t2['def'].values[0]
    time2 = t2['ofs'].values[0]*t1['def'].values[0]

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
            gols[linha, coluna] = round(
                poisson1[linha]*poisson2[coluna]*100, 3)

    for linha in range(0, 6):
        for coluna in range(0, 6):
            if linha > coluna:
                prob1 = round(prob1+gols[linha, coluna], 2)
            elif linha == coluna:
                empate = round(empate+gols[linha, coluna], 2)
            elif linha < coluna:
                prob2 = round(prob2+gols[linha, coluna], 2)

    cs = 0
    ep = 0
    fr = 0
    for ii in range(1):
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

        if len(a.loc[a == 'casa']) > len(a.loc[a == 'fora']):
            cs += 1
        elif len(a.loc[a == 'casa']) < len(a.loc[a == 'fora']):
            fr += 1
        else:
            ep += 1

    placar = (np.unravel_index(gols.argmax(), gols.shape))

    return [list(placar), cs, ep, fr]

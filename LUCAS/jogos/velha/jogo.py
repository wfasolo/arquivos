import time
import pandas as pd
import numpy as np
import random


from telas import tela, linhas, posicao
from ganhar import final

jogador = 1
jogacum = []

jogadas = pd.DataFrame([[0, 0]], columns=[0, 1])

condicao = True

pml = pd.Series([0, 1, 2, 0, 1, 2, 0, 1, 2])
pmc = pd.Series([0, 0, 0, 1, 1, 1, 2, 2, 2])


def vez(jogavez):

    if jogavez == 1:
        pos = int(input('Entre com uma casa: '))-1

    elif jogavez == 2:
        pos = random.randint(0, 8)

    return pos


def jogad(jogador, jogadas):
    pos = vez(jogador)

    if p[pos] != 0 and condicao == True:
        posicao(p[pos], jogador)
        jogada.append((pos+1))
        jogacum.append((pos+1))
        jogadas = jogadas.append([jogada], ignore_index=True)
        jogadas = jogadas.fillna(0)

        p[pos] = 0

        if jogador == 1:
            matriz[pml[pos], pmc[pos]] = 1
            jogador = 2

        elif jogador == 2:
            matriz[pml[pos], pmc[pos]] = 2
            jogador = 1

    return [jogador, jogadas, jogacum]


for cont in range(5):
    jogada = []

    p = pd.Series([[190, 185], [190, 285], [190, 385],
                   [290, 185], [290, 285], [290, 385],
                   [390, 185], [390, 285], [390, 385]])

    matriz = np.array([[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]])

    tela()

    while(condicao):

        jogar = jogad(jogador, jogadas)
        jogador = jogar[0]
        jogadas = jogar[1]
        jogacum = jogar[2]

        fim = final(matriz,p,linhas)

        if fim != 9:
            print(jogadas)
            break

    time.sleep(5)


#jogue 100 partida aparti de uma dedrminada pocição

#Se xpartida=ypartida eliminea a ypartida

#analise as partidas que tem os 3(Dpois de analisar, analise com nj-1,-1,-1,-1...) ultimo lance iguais vê qual é (Se vez=jogador 1, procure o melhor valor caso contrario escolha o menor)
#(Se os resudados forem iguais escolha aleatorio)e depois nas proximas analises só conte a ultima jogada(que vai receber a pontuação da escolha na sua analise)
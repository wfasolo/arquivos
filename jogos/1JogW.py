import time
import pandas as pd
import numpy as np
import pygame
import random

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

jogador = 1
condicao = True
linha = 0

p = pd.Series([[190, 185], [190, 285], [190, 385],
               [290, 185], [290, 285], [290, 385],
               [390, 185], [390, 285], [390, 385]])

matriz = np.array([[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]).astype(np.float32)

pml = pd.Series([0, 1, 2, 0, 1, 2, 0, 1, 2])
pmc = pd.Series([0, 0, 0, 1, 1, 1, 2, 2, 2])

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill(BLACK)
font = pygame.font.SysFont(None, 55)
pygame.display.set_caption('Joga da Velha')


def tela():
    pygame.draw.line(screen, WHITE, [150, 250], [450, 250], 2)
    pygame.draw.line(screen, WHITE, [150, 350], [450, 350], 2)

    pygame.draw.line(screen, WHITE, [250, 150], [250, 450], 2)
    pygame.draw.line(screen, WHITE, [350, 150], [350, 450], 2)

    # atualizando a tela
    pygame.display.flip()


def posicao(posi, jogadores):

    if jogadores == 1:
        jog = 'X'

    if jogadores == 2:
        jog = "O"

    time.sleep(0.2)

    text = font.render(jog, True, WHITE)
    screen.blit(text, posi)

    pygame.display.flip()


def vez(jogavez):
    if jogavez == 1:
        pos = int(input('Entre com uma casa: '))-1

    elif jogavez == 2:
        pos = random.randint(0, 8)

    return pos


def jogad(jogador):
    pos = vez(jogador)

    if p[pos] != 0 and condicao == True:
        posicao(p[pos], jogador)
        p[pos] = 0

        if jogador == 1:
            matriz[pml[pos], pmc[pos]] = 1
            jogador = 2

        elif jogador == 2:
            matriz[pml[pos], pmc[pos]] = 2
            jogador = 1

    return jogador


def ganhou_X():

    if (set(matriz.T[0]) == set([1, 1, 1])):
        linha = 1
        condicao = False

    elif(set(matriz.T[1]) == set([1, 1, 1])):
        linha = 2
        condicao = False

    elif(set(matriz.T[2]) == set([1, 1, 1])):
        linha = 3
        condicao = False

    elif(set(matriz[0]) == set([1, 1, 1])):
        linha = 4
        condicao = False

    elif(set(matriz[1]) == set([1, 1, 1])):
        linha = 5
        condicao = False

    elif(set(matriz[2]) == set([1, 1, 1])):
        linha = 6
        condicao = False

    elif(set(matriz.diagonal()) == set([1, 1, 1])):
        linha = 7
        condicao = False

    elif(set(np.fliplr(matriz).diagonal()) == set([1, 1, 1])):
        linha = 8
        condicao = False

    else:
        linha = 0
        condicao = True

    return [condicao, linha]


def ganhou_O():

    if (set(matriz.T[0]) == set([2, 2, 2])):
        linha = 1
        condicao = False

    elif(set(matriz.T[1]) == set([2, 2, 2])):
        linha = 2
        condicao = False

    elif(set(matriz.T[2]) == set([2, 2, 2])):
        linha = 3
        condicao = False

    elif(set(matriz[0]) == set([2, 2, 2])):
        linha = 4
        condicao = False

    elif(set(matriz[1]) == set([2, 2, 2])):
        linha = 5
        condicao = False

    elif(set(matriz[2]) == set([2, 2, 2])):
        linha = 6
        condicao = False

    elif(set(matriz.diagonal()) == set([2, 2, 2])):
        linha = 7
        condicao = False

    elif(set(np.fliplr(matriz).diagonal()) == set([2, 2, 2])):
        linha = 8
        condicao = False

    else:
        linha = 0
        condicao = True

    return [condicao, linha]


def empate(condicao):
    if list(p[p != 0].index) and condicao == True:
        condicao = True

    else:
        condicao = False

    return condicao


def linhas(linha):
    if linha == 0:
        pass
    elif linha == 1:
        pygame.draw.line(screen, RED, [200, 140], [200, 460], 2)  # 1

    elif linha == 2:
        pygame.draw.line(screen, RED, [300, 140], [300, 460], 2)  # 2

    elif linha == 3:
        pygame.draw.line(screen, RED, [400, 140], [400, 460], 2)  # 3

    elif linha == 4:
        pygame.draw.line(screen, RED, [140, 200], [460, 200], 2)  # 4

    elif linha == 5:
        pygame.draw.line(screen, RED, [140, 300], [460, 300], 2)  # 5

    elif linha == 6:
        pygame.draw.line(screen, RED, [140, 400], [460, 400], 2)  # 6

    elif linha == 7:
        pygame.draw.line(screen, RED, [140, 140], [460, 460], 2)  # 7

    elif linha == 8:
        pygame.draw.line(screen, RED, [140, 460], [460, 140], 2)  # 8

    pygame.display.flip()


def final():
    Result = 9

    cond = ganhou_X()
    condicao = cond[0]

    if condicao == False:
        linhas(cond[1])
        text = font.render('Ganhou X!!!', True, WHITE)
        screen.blit(text, [200, 550])
        pygame.display.flip()
        Result = 1

    cond = ganhou_O()
    condicao = cond[0]
    if condicao == False:
        linhas(cond[1])
        text = font.render('Ganhou O!!!', True, WHITE)
        screen.blit(text, [200, 550])
        pygame.display.flip()
        Result = 2

    condicao = empate(condicao)
    if condicao == False:
        text = font.render('Empatou!!!', True, WHITE)
        screen.blit(text, [200, 550])
        pygame.display.flip()
        Result = 0

    return Result


tela()

while(condicao):

    jogador = jogad(jogador)

    fim = final()

    if fim != 9:
        break


time.sleep(5)

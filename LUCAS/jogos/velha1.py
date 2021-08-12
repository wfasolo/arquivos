import time
import pandas as pd
import pygame
import random

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

jogador = 1
j1 = pd.Series()
j2 = pd.Series()
jogadas = pd.DataFrame()
condicao = True
linha = 0
Result = 9

p = pd.Series([[190, 185],
               [190, 285],
               [190, 385],
               [290, 185],
               [290, 285],
               [290, 385],
               [390, 185],
               [390, 285],
               [390, 385]])

pygame.init()

screen = pygame.display.set_mode((600, 600))

# carregando fonte
font = pygame.font.SysFont(None, 55)
pygame.display.set_caption('Joga da Velha')

# preenchendo o fundo com preto
screen.fill(BLACK)

# desenhando na superfície


def tela():
    pygame.draw.line(screen, WHITE, [150, 250], [450, 250], 2)
    pygame.draw.line(screen, WHITE, [150, 350], [450, 350], 2)

    pygame.draw.line(screen, WHITE, [250, 150], [250, 450], 2)
    pygame.draw.line(screen, WHITE, [350, 150], [350, 450], 2)

    # atualizando a tela
    pygame.display.flip()

# definindo posição


def posicao(posi, jogadores):

    if jogadores == 1:
        jog = 'X'

    if jogadores == 2:
        jog = "O"

    time.sleep(0.2)

    text = font.render(jog, True, WHITE)
    screen.blit(text, posi)

    pygame.display.flip()


def jogad(jogadorj, j111, j222):
    pos = random.randint(0, 8)

    if p[pos] != 0:
        posicao(p[pos], jogadorj)
        p[pos] = 0

        if jogadorj == 1:
            j11 = pd.Series(pos+1)
            j111 = j1.append(j11, ignore_index=True)
            jogadorj = 2

        elif jogadorj == 2:
            j22 = pd.Series(pos+1)
            j222 = j2.append(j22, ignore_index=True)
            jogadorj = 1

    return [jogadorj, j111, j222]


def ganhou_X():

    if (list(j1[j1 == 1].index) and list(j1[j1 == 2].index) and list(j1[j1 == 3].index)):
        linha = 1
        condicao = False

    elif(list(j1[j1 == 4].index) and list(j1[j1 == 5].index) and list(j1[j1 == 6].index)):
        linha = 2
        condicao = False

    elif(list(j1[j1 == 7].index) and list(j1[j1 == 8].index) and list(j1[j1 == 9].index)):
        linha = 3
        condicao = False

    elif(list(j1[j1 == 1].index) and list(j1[j1 == 4].index) and list(j1[j1 == 7].index)):
        linha = 4
        condicao = False

    elif(list(j1[j1 == 2].index) and list(j1[j1 == 5].index) and list(j1[j1 == 8].index)):
        linha = 5
        condicao = False

    elif(list(j1[j1 == 3].index) and list(j1[j1 == 6].index) and list(j1[j1 == 9].index)):
        linha = 6
        condicao = False

    elif(list(j1[j1 == 1].index) and list(j1[j1 == 5].index) and list(j1[j1 == 9].index)):
        linha = 7
        condicao = False

    elif(list(j1[j1 == 3].index) and list(j1[j1 == 5].index) and list(j1[j1 == 7].index)):
        linha = 8
        condicao = False

    else:
        linha = 0
        condicao = True

    return [condicao, linha]


def ganhou_O():

    if (list(j2[j2 == 1].index) and list(j2[j2 == 2].index) and list(j2[j2 == 3].index)):
        linha = 1
        condicao = False

    elif(list(j2[j2 == 4].index) and list(j2[j2 == 5].index) and list(j2[j2 == 6].index)):
        linha = 2
        condicao = False

    elif(list(j2[j2 == 7].index) and list(j2[j2 == 8].index) and list(j2[j2 == 9].index)):
        linha = 3
        condicao = False

    elif(list(j2[j2 == 1].index) and list(j2[j2 == 4].index) and list(j2[j2 == 7].index)):
        linha = 4
        condicao = False

    elif(list(j2[j2 == 2].index) and list(j2[j2 == 5].index) and list(j2[j2 == 8].index)):
        linha = 5
        condicao = False

    elif(list(j2[j2 == 3].index) and list(j2[j2 == 6].index) and list(j2[j2 == 9].index)):
        linha = 6
        condicao = False

    elif(list(j2[j2 == 1].index) and list(j2[j2 == 5].index) and list(j2[j2 == 9].index)):
        linha = 7
        condicao = False

    elif(list(j2[j2 == 3].index) and list(j2[j2 == 5].index) and list(j2[j2 == 7].index)):
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


tela()


while(condicao):
    jogs = jogad(jogador, j1, j2)

    jogador = jogs[0]
    j1 = jogs[1]
    j2 = jogs[2]

    cond = ganhou_X()
    condicao=cond[0]
    if condicao == False:
        linhas(cond[1])
        text = font.render('Ganhou X!!!', True, WHITE)
        screen.blit(text, [200, 550])
        pygame.display.flip()
        Result = 1
        break

    cond = ganhou_O()
    condicao=cond[0]
    if condicao == False:
        linhas(cond[1])
        text = font.render('Ganhou O!!!', True, WHITE)
        screen.blit(text, [200, 550])
        pygame.display.flip()
        Result = 2
        break

    condicao = empate(condicao)
    if condicao == False:
        text = font.render('Empatou!!!', True, WHITE)
        screen.blit(text, [200, 550])
        pygame.display.flip()
        Result = 0
        break


# espera
time.sleep(3)
jogadas = jogadas.append([j1, j2], ignore_index=True)


print(jogadas)

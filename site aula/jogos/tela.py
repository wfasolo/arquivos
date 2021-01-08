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
j1 = pd.Series(11)
j2 = pd.Series(11)
condicao = True


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
def posicao(pos, jogador):

    if jogador == 1:
        jog = 'X'
    else:
        jog = "O"

    time.sleep(1)

    text = font.render(jog, True, WHITE)
    screen.blit(text, pos)

    pygame.display.flip()


def ganhou():

    if (list(j2[j2 == 1].index) and list(j2[j2 == 2].index) and list(j2[j2 == 3].index)):
        print('ganhou')
        condicao = False
    else:
        condicao = True

    if(list(j2[j2 == 4].index) and list(j2[j2 == 5].index) and list(j2[j2 == 6].index)):
        print('ganhou')
        condicao = False
    else:
        condicao = True

    if(list(j2[j2 == 7].index) and list(j2[j2 == 8].index) and list(j2[j2 == 9].index)):
        print('ganhou')
        condicao = False
    else:
        condicao = True

    if(list(j2[j2 == 1].index) and list(j2[j2 == 4].index) and list(j2[j2 == 7].index)):
        print('ganhou')
        condicao = False
    else:
        condicao = True

    if(list(j2[j2 == 2].index) and list(j2[j2 == 5].index) and list(j2[j2 == 8].index)):
        print('ganhou')
        condicao = False
    else:
        condicao = True

    if(list(j2[j2 == 3].index) and list(j2[j2 == 6].index) and list(j2[j2 == 9].index)):
        print('ganhou')
        condicao = False
    else:
        condicao = True
    if(list(j2[j2 == 1].index) and list(j2[j2 == 5].index) and list(j2[j2 == 9].index)):
        print('ganhou')
        condicao = False
    else:
        condicao = True

    if(list(j2[j2 == 3].index) and list(j2[j2 == 5].index) and list(j2[j2 == 7].index)):
        print('ganhou')
        condicao = False
    else:
        condicao = True

    return condicao


def empate(condicao):
    if list(p[p != 0].index) and condicao == True:
        condicao = True

    else:
        screen.fill(BLACK)
        text = font.render('Empatou!!!', True, WHITE)
        screen.blit(text, [250, 250])

        pygame.display.flip()
        condicao = False
    return condicao


def jogad(jogador, j111, j222):
    pos = random.randint(0, 8)

    if p[pos] != 0:
        posicao(p[pos], jogador)
        p[pos] = 0
        if jogador == 1:
            j11 = pd.Series(pos)
            j111 = j1.append(j11, ignore_index=True)
            jogador = 2

        else:
            j22 = pd.Series(pos)
            j222 = j2.append(j22, ignore_index=True)
            jogador = 1

    return [jogador, j111, j222]


tela()


while(condicao):

    condicao = ganhou()
    if condicao == False:
        break
    condicao = empate(condicao)
    if condicao == False:
        break
    jog = jogad(jogador, j1, j2)
    jogador = jog[0]
    j1 = jog[1]
    j2 = jog[2]

    print(jog[1])


# espera
time.sleep(2)

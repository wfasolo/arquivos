import time
import pandas as pd
import pygame
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

resultado = pd.DataFrame()
ccc=pd.DataFrame()

pygame.init()

screen = pygame.display.set_mode((600, 600))

# carregando fonte
font = pygame.font.SysFont(None, 55)
pygame.display.set_caption('Joga da Velha')


def tela():
    screen.fill(BLACK)
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


def jogad(jogadorj, c1, c2):
    pos = random.randint(0, 8)

    if p[pos] != 0:
        ccc = pd.DataFrame([j11, j22]).T
        ccc.fillna(0, inplace=True)

        posicao(p[pos], jogadorj)
        p[pos] = 0

        if jogadorj == 1:
            j11[c1] = pos+1
            resul[c1] = result
            c1 = c1+1
            jogadorj = 2

        elif jogadorj == 2:
            poss=IA(ccc)
            print(poss)
            time.sleep(2)
            
            j22[c2] = poss
            resul[c2] = result
            c2 = c2+1
            jogadorj = 1
        



    return [jogadorj, c1, c2]


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


def IA(cc):


    (X_train, y_train) = (cc[:-1], cc[1:])
    ultimo = y_train[-1:]
    model1 = KNeighborsClassifier(n_neighbors=(1))
    model1.fit(X_train, y_train)
    previsao = model1.predict(ultimo)
    prev=previsao[0][0]

    return int(prev)


for ii in range(0, 1):
    p = pd.Series([[190, 185],
                   [190, 285],
                   [190, 385],
                   [290, 185],
                   [290, 285],
                   [290, 385],
                   [390, 185],
                   [390, 285],
                   [390, 385]])

    jogador = 1
    j11 = pd.Series([5,1])
    j22 = pd.Series([1,5])
    resul = pd.Series([0])
    jogadas = pd.DataFrame()
    condicao = True
    linha = 0
    result = 9
    c1 = 0
    c2 = 0

    tela()

    while(condicao):

        jogs = jogad(jogador, c1, c2)

        jogador = jogs[0]
        c1 = jogs[1]
        c2 = jogs[2]
        j1 = pd.Series(j11)
        j2 = pd.Series(j22)
 


        cond = ganhou_X()
        condicao = cond[0]
        if condicao == False:
            linhas(cond[1])
            text = font.render('Ganhou X!!!', True, WHITE)
            screen.blit(text, [200, 550])
            pygame.display.flip()
            result = 1
            break

        cond = ganhou_O()
        condicao = cond[0]
        if condicao == False:
            linhas(cond[1])
            text = font.render('Ganhou O!!!', True, WHITE)
            screen.blit(text, [200, 550])
            pygame.display.flip()
            result = 2
            break

        condicao = empate(condicao)
        if condicao == False:
            text = font.render('Empatou!!!', True, WHITE)
            screen.blit(text, [200, 550])
            pygame.display.flip()
            result = 0
            break

    jogadas = jogadas.append([j1, j2], ignore_index=True).T
    resul[c2] = result
    resul2 = pd.DataFrame(resul)
    resultado[ii] = [jogadas[0].values, jogadas[1].values, resul2[0].values]
    time.sleep(1)

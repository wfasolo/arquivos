import time
import json
import pandas as pd
import numpy as np
import pygame
import random
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

arquivo = open('/home/casa/Documentos/arquivos/jogos/modelos/velhax.txt', 'r')
dadosx = pd.read_fwf(arquivo, index_col=0)
arquivo.close()

arquivo = open('/home/casa/Documentos/arquivos/jogos/modelos/velhay.txt', 'r')
dadosy = json.loads(arquivo.read())
arquivo.close()

a=np.load(r'/home/casa/Documentos/arquivos/jogos/modelos/y.npy')
a=list(a)
dadosy = a

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

condicao = True
linha = 0
jogador = 1
jogacum = dadosy
jogadas = pd.DataFrame(dadosx.values)


pml = pd.Series([0, 1, 2, 0, 1, 2, 0, 1, 2])
pmc = pd.Series([0, 0, 0, 1, 1, 1, 2, 2, 2])

pygame.init()

screen = pygame.display.set_mode((600, 600))

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


def posicao(pos, jogador):

    if jogador == 1:
        jog = 'X'

    if jogador == 2:
        jog = "O"

    time.sleep(0.2)

    text = font.render(jog, True, WHITE)
    screen.blit(text, pos)

    pygame.display.flip()


def vez(jogavez):

    if jogavez == 1:
        pos = int(input('Entre com uma casa: '))-1
        # pos = random.randint(0, 8)

    elif jogavez == 2:
        if len(jogadas) < 10:
            pos = random.randint(0, 8)
        else:
            pos = IA()

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


def IA():
    predictions = 0
    while(predictions == 0):
        x = jogadas.drop(len(jogadas)-1)
        y = np.ravel(jogacum)
        ultimo = [jogadas.T[len(jogadas)-1].values]
        ultimo = list(np.ravel(ultimo))

        model3 = Sequential()
        model3.add(Dense(3, input_shape=(len(ultimo),), activation="relu"))
        model3.add(Dense(2, activation="relu"))
      
        
        model3.add(Dense(1, activation="relu"))

        optimizer = tf.keras.optimizers.RMSprop(0.001)

        model3.compile(loss='MSE', optimizer='adam', metrics=['mse'])

        model3.fit(x.values, y, batch_size=128, epochs=200, verbose=1)

        predictions = model3.predict([ultimo])

        print(int(round(predictions[0][0], 0)))

    return int(round(predictions[0][0], 0))-1


for cont in range(3):
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

        fim = final()

        if fim != 9:
            break

    time.sleep(1)

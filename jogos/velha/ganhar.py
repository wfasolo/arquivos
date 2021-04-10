import numpy as np
import telas as tl

def ganhou_X(matriz):

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


def ganhou_O(matriz):

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


def empate(condicao,p):
    if list(p[p != 0].index) and condicao == True:
        condicao = True

    else:
        condicao = False

    return condicao


def final(matriz,p,linhas):
    Result = 9

    cond = ganhou_X(matriz)
    condicao = cond[0]
    if condicao == False:
        linhas(cond[1])
        text = tl.font.render('Ganhou X!!!', True, tl.WHITE)
        tl.screen.blit(text, [200, 550])
        tl.pygame.display.flip()
        Result = 1

    cond = ganhou_O(matriz)
    condicao = cond[0]
    if condicao == False:
        linhas(cond[1])
        text = tl.font.render('Ganhou O!!!', True, tl.WHITE)
        tl.screen.blit(text, [200, 550])
        tl.pygame.display.flip()
        Result = 2

    condicao = empate(condicao,p)
    if condicao == False:
        text = tl.font.render('Empatou!!!', True, tl.WHITE)
        tl.screen.blit(text, [200, 550])
        tl.pygame.display.flip()
        Result = 0

    return Result


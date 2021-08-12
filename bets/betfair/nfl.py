import random as rd
import time
import os

cont = 1
jardascont = 10
pesoacerto = 0
pesojardas = 0
pontostime1 = 0
pontostime2 = 0
jardastime1 = 25
jardastime2 = 75
ataque = 'time1'
jardas = 0


def pergunta():
    global pesoacerto, pesojardas
    jogada = input('qual tipo de jogada: ')

    if jogada == "run":
        corredor = input('quem vai correr: ')
        if corredor == "qb":
            print("qb run")
            pesoacerto = 95
            pesojardas = 2
        elif corredor == "rb":
            print("rb run")
            pesoacerto = 90
            pesojardas = 10
        elif corredor == "fb":
            print("fb run")
            pesoacerto = 98
            pesojardas = 1
        else:
            print("corredor invalido")
    elif jogada == "pass":
        estilo = input('qual estilo de pass: ')
        if estilo == "short":
            print("short pass")
            pesoacerto = 85
            pesojardas = 30
        elif estilo == "medium":
            print("medium pass")
            pesoacerto = 70
            pesojardas = 50
        elif estilo == "long":
            print("long pass")
            pesoacerto = 50
            pesojardas = 80
        else:
            print("estilo invalido")
    else:
        print("jogada invalida")


def jogada():
    global resultado, pesoacerto

    sucessojogada = rd.choices(['completo', 'incompleto'], weights=[
                               pesoacerto, 100-pesoacerto], k=1)
    if sucessojogada[0] == 'incompleto':
        resultado = rd.choices(
            ['tornover', 'incompleto'], weights=[20, 80], k=1)
    else:
        resultado = rd.choices(
            ['decida', 'firt down', 'avanço', 'touchdown'], weights=[55, 25, 15, 5], k=1)


def resutados():
    global resultado, ataque, jardastime1, jardastime2, jardas, pesojardas, cont
    if resultado[0] == 'decida':
        jardas = int(rd.randint(2, 10)*pesojardas/100)
    elif resultado[0] == 'firt down':
        jardas = 10
    elif resultado[0] == 'avanço':
        jardas = int(rd.randint(11, 74)*(pesojardas/100))
    elif resultado[0] == 'touchdown':
        jardas = 75
    elif resultado[0] == 'tornover':
        if ataque == 'time1':
            ataque = 'time2'
            jardas = 0
        else:
            ataque = 'time1'
            jardas = 0
    elif resultado[0] == 'incompleto':
        jardas = 0

    if ataque == 'time1':
        jardastime1 += jardas
        jardastime2 -= jardas
    else:
        jardastime2 += jardas
        jardastime1 -= jardas


def TD():
    global jardastime1, jardastime2, ataque, pontostime1, pontostime2
    if jardastime1 >= 100:
        pontostime1 += 7
        ataque = 'time2'
        jardastime1 = 75
        jardastime2 = 25

    if jardastime2 >= 100:
        pontostime2 += 7
        ataque = 'time1'
        jardastime2 = 75
        jardastime1 = 25


def campo():
    global ataque, pontostime1, pontostime2
    if ataque == 'time1':
        posicao = int(jardastime1/5)
        jard = jardastime1
    else:
        posicao = int(jardastime2/5)
        jard = jardastime2

    os.system('clear')

    for ii in range(21):
        if ii == posicao:
            print('|----', ataque, '----|', jard)
        else:
            print('|---------------|')

    if jard >= 100:
        print('TOUCHDOWN!!!')
        time.sleep(5)


for i in range(10):

    campo()
    pergunta()
    jogada()
    resutados()
    TD()

    if resultado[0] == 'decida':
        jardascont -= jardas
        if cont == 5 and jardascont >= 1:
            cont = 1
            jardascont = 10
            if ataque == 'time1':
                ataque = 'time2'
                jardas = 0
            else:
                ataque = 'time1'
                jardas = 0
        elif jardascont <= 0:
            cont = 1
            jardascont = 10
        else:
            cont += 1
    else:
        cont = 1
        jardascont = 10

    print(ataque, resultado[0], jardas)
    time.sleep(1)
    if ataque == 'time1':
        print(jardastime1)
    else:
        print(jardastime2)
    time.sleep(1)
    print(cont, jardascont)

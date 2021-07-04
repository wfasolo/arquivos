import random as dados


preço = 5000
empuxo = 0
empuxo2 = empuxo
chance_de_erro = 0
chance_de_erro1 = 0
chance_de_erro2 = 0
chance_de_erro3 = 0
chance_de_erro4 = 0
chance_de_erro5 = 0
contador = 1
parte = ""
while (parte != "sair"):

    parte = input("parte do foquete: ")

    if parte == "motor":
        mortor = int(input("motor: "))
        if mortor == 1:
            preço -= 10
            empuxo += 8
            chance_de_erro1 += 17
        elif mortor == 2:
            preço -= 100
            empuxo += 12.7
            chance_de_erro1 += 14
        elif mortor == 3:
            preço -= 500
            empuxo += 18.4
            chance_de_erro1 += 8
        elif mortor == 4:
            preço -= 750
            empuxo += 19.6
            chance_de_erro1 += 4
        elif mortor == 5:
            preço -= 1000
            empuxo += 31
            chance_de_erro1 += 1
        else:
            print("erro")

    elif parte == "estagio":
        estagio = int(input("estagio: "))
        if estagio == 1:
            preço -= 50
            empuxo -= 8.5
            chance_de_erro2 += 18
        elif estagio == 2:
            preço -= 500
            empuxo -= 8.3
            chance_de_erro2 += 16
        elif estagio == 3:
            preço -= 2500
            empuxo -= 8
            chance_de_erro2 += 10
        elif estagio == 4:
            preço -= 3750
            empuxo -= 7.5
            chance_de_erro2 += 8
        elif estagio == 5:
            preço -= 5000
            empuxo -= 7
            chance_de_erro2 += 5
    elif parte == "combustivel":
        combustivel = int(input("combustivel: "))
        if combustivel == 1:
            preço -= 5
            empuxo += 0.5
            chance_de_erro3 += 19
        elif combustivel == 2:
            preço -= 50
            empuxo += 1
            chance_de_erro3 += 18
        elif combustivel == 3:
            preço -= 250
            empuxo += 1.2
            chance_de_erro3 += 12
        elif combustivel == 4:
            preço -= 330
            empuxo += 1.5
            chance_de_erro3 += 10
        elif combustivel == 5:
            preço -= 500 
            empuxo += 2
            chance_de_erro3 += 8
    else:
        print("todo escolido")
    chance_de_erro = chance_de_erro1+chance_de_erro2+chance_de_erro3/3
    if (preço < 0 or empuxo < 0):
        if preço < 0:
            print("muito caro")
        else:
            print("muito pesado ou pouca força")
    else:
        print(preço, " ", empuxo, " ", chance_de_erro)


while (empuxo2 > 0):
    if empuxo2 >= 10:
        chance_de_erro4 += 1
        empuxo2 -= 10
        contador += 1
    elif empuxo == 5:
        chance_de_erro4 += 5
        empuxo2 -= 5
        contador += 1
    elif empuxo2 >= 1:
        chance_de_erro4 += 10
        empuxo2 -= 1
        contador += 1
    elif empuxo == 0.5:
        chance_de_erro4 += 14
        empuxo2 -= 0.5
        contador += 1
    else:
        chance_de_erro4 += 18
        empuxo2 -= 0.1
        contador += 1

chance_de_erro5 += ((chance_de_erro4/contador)+chance_de_erro)/2

dado = dados.random(1, 20)

if dado > chance_de_erro5:
    dados2 = dados.random(1, 4)
    if dados2 <= 3:
        print("deu certo")
    else:
        print("explodio")
else:
    dados3 = dados.random(1, 4)
    if dados3 <= 2:
        print("não decolou")
    else:
        print("explodio")

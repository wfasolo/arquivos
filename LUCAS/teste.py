

acerto = [[0, 0, 0, 0, 0]]
acertos = 1

valores = [[1, 0, 0, 0, 1],
           [0, 1, 0, 1, 0],
           [0, 1, 1, 0, 0],
           [1, 1, 0, 1, 0],
           [0, 1, 0, 1, 0],
           [0, 1, 1, 0, 0],
           [1, 1, 0, 1, 0],
           [0, 1, 0, 1, 0]]


b = [list(range(len(valores)))]  # peso
print(b)
# while(acertos != 0):
for f in range(15):
    c = [[0, 0, 0, 0, 0]]
    for i in range(len(valores)-2):
        for ii in range(len(valores[0])-1):
            c[0][i] += valores[i][ii]*b[0][i]+b[0][len(b)-1]
            print(c)

        if c[0][i] <= 0:
            c[0][i] = 0
        else:
            c[0][i] = 1

    for i in range(5):
        acerto[0][i] = valores[i][4]-c[0][i]

    acertos = 1-(acerto[0][0] + acerto[0][1] + acerto[0]
                 [2] + acerto[0][3] + acerto[0][4])/5

    for i in range(4):
        b[0][i] += 0.1 * acertos - valores[i][0]
    b[0][5] += 0.1 * acerto[0][4] - b[0][4]
    print(acertos, c, b)


# 0.22, 0.4

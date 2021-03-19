import turtle
import time
import random

pen = turtle.Pen()
pen2 = turtle.Pen()


pen2.sety(10)
pen2.color('Red')

# pen.penup()
# pen2.penup()

for v in range(1, 6):

    for i in range(400):
        ran = random.randint(-5, 2)
        ran2 = random.randint(-5, 2)

        if (i > 0 and i <= 20):
            pen.forward(5-(ran/2))
            pen2.forward(5-(ran2/2))

        if (i > 20 and i <= 200):
            pen.forward(1)
            pen2.forward(1)
            pen.right(1)
            pen2.right(1)

        if (i > 200 and i <= 220):
            pen.forward(5-(ran/2))
            pen2.forward(5-(ran2/2))

        if (i > 220 and i <= 400):
            pen.forward(1)
            pen2.forward(1)
            pen.right(1)
            pen2.right(1)

    posi = (pen.position()-pen2.position())
    if posi[0] < 0:
        print('Vermelho')
    else:
        print('Preto')
time.sleep(2)

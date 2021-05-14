import math
import pygame
from pygame.locals import*
import time
import numpy as np

width = 1000
height = 500
Color_screen = (0, 0, 0)
Color_line = (0, 250, 0)

vel=float(input("velocidade: "))
ang=float(input("angulo: "))
ang=math.radians(ang)

screen = pygame.display.set_mode((width, height))
screen.fill(Color_screen)


tempo=vel*math.sin(ang)/5


pygame.draw.line(screen, (255,0,0), (0, 300), (1000, 300))

pygame.draw.circle(screen, (0,0,255), (700,295), 5)
for t in np.arange(0,tempo+0.1,0.2):
    x= vel*math.cos(ang)*t
    y=300-(vel*math.sin(ang)*t-5*t*t)
    print(t,x,y)
    pygame.draw.line(screen, Color_line, (20+x, y), (22+x, y))
    time.sleep(0.01)
    pygame.display.flip()

    if x>685 and x<720:
        print("acertou")
time.sleep(5)

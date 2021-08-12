import math
import pygame
from pygame.locals import*
import time
import numpy as np
import random as rd

width = 1000
height = 500
Color_screen = (50, 200, 10)
Color_line = (0, 250, 0)


screen = pygame.display.set_mode((width, height))
screen.fill(Color_screen)
pygame.draw.rect(screen, (160, 255, 250), (0, 0, 1000, 350))

angle = 90-11

radar = (100, 350)
radar_len = 50
x = radar[0] + math.cos(270-math.radians(angle)) * radar_len
y = radar[1] + math.sin(270-math.radians(angle)) * radar_len

# then render the line radar->(x,y)
pygame.draw.line(screen, Color("black"), radar, (x, y),  5)
pygame.display.flip()

time.sleep(2)


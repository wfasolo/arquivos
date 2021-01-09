# https://www.kaggle.com/dhanushkishore/a-self-learning-tic-tac-toe-program?scriptVersionId=46958713

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
j1 = pd.Series()
j2 = pd.Series()
jogadas=pd.DataFrame()
condicao = True
Result=9

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


pygame.draw.line(screen, WHITE, [150, 250], [450, 250], 2)
pygame.draw.line(screen, WHITE, [150, 350], [450, 350], 2)

pygame.draw.line(screen, WHITE, [250, 150], [250, 450], 2)
pygame.draw.line(screen, WHITE, [350, 150], [350, 450], 2)












# atualizando a tela
pygame.display.flip()
time.sleep(3)

while (True):
  # get all events
  ev = pygame.event.get()

  # proceed events
  for event in ev:

    # handle MOUSEBUTTONUP
    if event.type == pygame.MOUSEBUTTONUP:
        x,y = pygame.mouse.get_pos()
        print(x,y)
    
      # get a list of all sprites that are under the mouse cursor
      #clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
      # do something with the clicked sprites...

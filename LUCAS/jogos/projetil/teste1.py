import math
import pygame
from pygame.locals import*
import time
import numpy as np
import random as rd

nivel = 0

screen = pygame.display.set_mode((1000, 700))


pygame.font.init()  # inicia font
fonte = pygame.font.get_default_font()  # carrega com a fonte padrão
fontesys = pygame.font.SysFont(fonte, 30)  # usa a fonte padrão


def texto():
    txttela = fontesys.render(txt, 1, (255, 255, 255))
    # coloca na posição 50,900 (tela FHD)
    screen.blit(txttela, (10, pos_text+55))

    input_box = pygame.Rect(100, 50+pos_text, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        done = True

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Render the current text.
        txt_surface = fontesys.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

    return text


def canhao():

    angle = ang-11

    radar = (0, 500)
    radar_len = 50
    x = radar[0] + math.cos(270-math.radians(angle)) * radar_len
    y = radar[1] + math.sin(270-math.radians(angle)) * radar_len

    # then render the line radar->(x,y)
    pygame.draw.line(screen, Color("black"), radar, (x, y),  10)
    pygame.display.flip()


def tela():
    screen.fill((50, 200, 10))
    pygame.draw.rect(screen, (160, 255, 250), (0, 0, 1000, 500))
    pygame.draw.rect(screen, (0, 0, 0), (0, 490, 10, 10))
    pygame.draw.circle(screen, (0, 0, 255), (x_alvo, y_alvo), 6)
    pygame.display.flip()

    pygame.init()


def tiro():
    global nivel 

    for t in np.arange(0, tempo+0.1, 0.1):
        x = 10+vel*math.cos(ang)*t
        y = 490-(vel*math.sin(ang)*t-5*t*t)

        pygame.draw.circle(screen, (255, 0, 255), (x, y), 2+(t/10))

        time.sleep(0.01)
        pygame.display.flip()

        if x > x_alvo-10 and x < x_alvo+10 and y > y_alvo-10 and y < y_alvo+10:

            for bomba in range(1, 50, 1):
                tam = 50-bomba

                pygame.draw.rect(screen, (160, 255, 250), (0, 0, 1000, 500))
                pygame.display.flip()

                pygame.draw.circle(
                    screen, (255, 200, rd.randrange(1, 255, 1)), (x_alvo, y_alvo), tam)
                pygame.draw.rect(screen, (50, 200, 10), (0, 500, 1000, 700))
                pygame.display.flip()

                time.sleep(0.05)
            nivel +=1


for cont in range(100):
    if nivel == 0:
        xnivel = 899
        ynivel = 499
    elif nivel == 1:
        xnivel = 500
        ynivel = 499
    elif nivel >= 2:
        xnivel = 500
        ynivel = 50
  
    x_alvo = rd.randrange(xnivel, 900)
    y_alvo = rd.randrange(ynivel, 500)
    tela()
    pos_text = 0
    txt = 'Ângulo'
    ang = float(texto())
    pos_text = 50
    canhao()
    txt = 'Veloc'
    vel = float(texto())

    ang = math.radians(ang)
    tempo = vel*math.sin(ang)/5
    tiro()
    time.sleep(3)

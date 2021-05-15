import math
import pygame
from pygame.locals import*
import time
import numpy as np
import random as rd



def texto():
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
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
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

    return text

pos_text = 0

width = 1000
height = 500
Color_screen = (50, 200, 10)
Color_line = (0, 250, 0)


screen = pygame.display.set_mode((width, height))
screen.fill(Color_screen)
pygame.draw.rect(screen, (160, 255, 250), (0, 0, 1000, 350))

x_alvo = rd.randrange(700, 701)
y_alvo = rd.randrange(349, 350)


pygame.draw.rect(screen, (0, 0, 0), (0, 340, 10, 10))
pygame.draw.circle(screen, (0, 0, 255), (x_alvo, y_alvo), 5)
pygame.display.flip()

pygame.init()


ang = float(texto())
pos_text = 50
vel = float(texto())
print(ang, vel)
ang = math.radians(ang)
tempo = vel*math.sin(ang)/5

for t in np.arange(0, tempo+0.1, 0.2):
    x = 20+vel*math.cos(ang)*t
    y = 350-(vel*math.sin(ang)*t-5*t*t)

    pygame.draw.circle(screen, (255, 0, 255), (x, y), t/2)

    time.sleep(0.01)
    pygame.display.flip()

    if x > x_alvo-5 and x < x_alvo+5 and y > y_alvo-5 and y < y_alvo+5:

        for bomba in range(1, 100, 20):
            pygame.draw.circle(
                screen, (bomba*2, bomba*2, bomba*2), (x_alvo, y_alvo), bomba)
            pygame.display.flip()
            time.sleep(0.25)
time.sleep(2)

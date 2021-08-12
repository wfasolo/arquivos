import pygame
import time

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


linha = 0

pygame.init()

screen = pygame.display.set_mode((600, 600))

font = pygame.font.SysFont(None, 55)
pygame.display.set_caption('Joga da Velha')


def tela():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [150, 250], [450, 250], 2)
    pygame.draw.line(screen, WHITE, [150, 350], [450, 350], 2)

    pygame.draw.line(screen, WHITE, [250, 150], [250, 450], 2)
    pygame.draw.line(screen, WHITE, [350, 150], [350, 450], 2)

    # atualizando a tela
    pygame.display.flip()


def linhas(linha):
    if linha == 0:
        pass
    elif linha == 1:
        pygame.draw.line(screen, RED, [200, 140], [200, 460], 2)  # 1

    elif linha == 2:
        pygame.draw.line(screen, RED, [300, 140], [300, 460], 2)  # 2

    elif linha == 3:
        pygame.draw.line(screen, RED, [400, 140], [400, 460], 2)  # 3

    elif linha == 4:
        pygame.draw.line(screen, RED, [140, 200], [460, 200], 2)  # 4

    elif linha == 5:
        pygame.draw.line(screen, RED, [140, 300], [460, 300], 2)  # 5

    elif linha == 6:
        pygame.draw.line(screen, RED, [140, 400], [460, 400], 2)  # 6

    elif linha == 7:
        pygame.draw.line(screen, RED, [140, 140], [460, 460], 2)  # 7

    elif linha == 8:
        pygame.draw.line(screen, RED, [140, 460], [460, 140], 2)  # 8

    pygame.display.flip()


def posicao(pos, jogador):

    if jogador == 1:
        jog = 'X'

    if jogador == 2:
        jog = "O"

    time.sleep(0.2)

    text = font.render(jog, True, WHITE)
    screen.blit(text, pos)

    pygame.display.flip()

import pygame
from pygame_input import Inputs, Button, JoyButton

inputs = Inputs()
inputs["fire"] = Button(pygame.K_SPACE, JoyButton(1))
inputs["fire"].on_press_repeated(player.fire, delay=0.1)


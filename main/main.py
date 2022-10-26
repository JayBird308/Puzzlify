#live share test

import pygame
import pygame_menu
from sys import exit

width = 600;
height = 400;

pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

def set_difficulty(value, difficulty):
    pass

def game_start():
    pass

menu = pygame_menu.Menu('Puzzlify', 400, 300, theme = pygame_menu.themes.THEME_BLUE)
menu.add.button('Play', game_start)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)





lenght = 14
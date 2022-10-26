#live share test

import pygame
import pygame_menu
from sys import exit

width = 600;
height = 400;

def set_difficulty(value, difficulty):
    pass

def game_start():
    pass

menu = pygame_menu.Menu('Puzzlify', 400, 300, theme = pygame_menu.themes.THEME_GREEN)
menu.add.button('Play', game_start)
menu.add.button('Quit', pygame_menu.events.EXIT)

pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code


        pygame.display.update()
        clock.tick(60)




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



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code


        pygame.display.update()
        clock.tick(60)




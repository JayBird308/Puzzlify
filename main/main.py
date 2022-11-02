#live share test

import pygame
import pygame_menu
from sys import exit

def set_difficulty(value, difficulty):
    pass

def game_start():
    pass

def main():

    #initialize the pygame module
    pygame.init()

    #load and set pygame logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    #height and width dimensions of application window
    width = 600;
    height = 400;

    #create surface on screen of size height x width
    screen = pygame.display.set_mode((width,height))

    running = True

    while running:


    pygame.init()
    clock = pygame.time.Clock()

    menu = pygame_menu.Menu('Puzzlify', 400, 300, theme = pygame_menu.themes.THEME_BLUE)
    menu.add.button('Play', game_start)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)








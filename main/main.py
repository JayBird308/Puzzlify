import pygame
import pygame_menu
from customMenu_theme import *
import ctypes
from sys import exit

def set_difficulty():
    pass

def game_start():
    pass

def game_select():
    pass

def account_info():
    pass

def main():

    # initialize the pygame module
    pygame.init()

    # height and width of user's desktop to fit application window to
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)

    # load and set pygame logo
    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()

    # create surface on screen of size height x
    screen = pygame.display.set_mode((width,height))

    # adds menu options
    menu = pygame_menu.Menu('Puzzlify', width, height, theme = pygame_menu.themes.THEME_GREEN)
    menu.add.button('Game Selection', game_select)
    menu.add.button('Account', account_info)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    #main loop run variable
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                    # set running condition to false, which will exit main loop
                    running = False
        menu.mainloop(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":

    # call main
    main()







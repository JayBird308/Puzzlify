import pygame
import pygame_menu
from customMenu_theme import *
import ctypes

# GLOBAL VARIABLES
global USER32, WIDTH, HEIGHT
USER32 = ctypes.windll.user32
WIDTH = USER32.GetSystemMetrics(0) # Monitor Resolution Width
HEIGHT = USER32.GetSystemMetrics(1) # Monitor Resolution Height

# menu button action to open game selection submenu
def game_select():
    pygame_menu.Menu('Game Selection', WIDTH, HEIGHT, theme = customMenu_theme)
    pass

# menu button action to open account submenu
def account_info():
    pygame_menu.Menu('Account', WIDTH, HEIGHT, theme = customMenu_theme)
    pass

def main():

    # initialize the pygame module
    pygame.init()

    # load and set pygame window and clock
    clock = pygame.time.Clock()

    # create surface on screen of size width x height
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    # adds menu options
    menu = pygame_menu.Menu('Welcome ' + 'Account_Name' + '!', WIDTH, HEIGHT, theme = customMenu_theme)
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






#live share test

import pygame
import pygame_menu
from sys import exit

def set_difficulty(value, difficulty):
    pass

def game_start():
    pass

def main():

    # initialize the pygame module
    pygame.init()

    # height and width dimensions of application window
    width = 600;
    height = 400;

    # load and set pygame logo
    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()

    # create surface on screen of size height x
    screen = pygame.display.set_mode((width,height))

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
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":

    # call main
    main()







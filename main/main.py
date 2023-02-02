import pygame, pygame_menu
import customMenu_theme
import MathQuiz as MQ
# import memoryGame as memGame
# import trizzleGame as trizzle
from databaseConnection import *
from random import randrange
from typing import Tuple, Any, List
import constants

# GLOBAL VARIABLES
global WIDTH, HEIGHT, SCREEN, FPS
# USER32 = constants.USER32
WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT
SCREEN = constants.SCREEN
FPS = constants.FPS

clock = constants.clock
main_menu = constants.main_menu

class main:
    def printUserEmail(USEREMAIL):
        print("Account Email: ", main.User.Email)

    def printUserCredentials(USERNAME, USERPASSWORD, USEREMAIL):
        print("Account Credentials:")
        print("USERNAME: ", USERNAME)
        print("USERPASSWORD: ", USERPASSWORD)
        print("USEREMAIL: ", USEREMAIL)

    def setUserName(username):
        main.User.Name = username
        return main.User.Name

    def setUserPass(userpassword):
        main.User.Password = userpassword
        return main.User.Password

    def setUserEmail(useremail):
        main.User.Email = useremail
        return main.User.Email

    def random_color() -> Tuple[int, int, int]:
        return randrange(0, 255), randrange(0, 255), randrange(0, 255)

    def main_background() -> None:
        """ Function used by menus, draw on background while menu is active."""
        SCREEN.fill((128, 0, 128))

    def main(test: bool = False) -> None:
        global clock
        global main_menu

        # initialize
        pygame.init()
        clock = pygame.time.Clock()

        # ---------------------------------
        # Create menus: Sub Menus
        # ---------------------------------
        ### --> Game Selection Menu <--- ##
        gameMenu = pygame_menu.Menu('Game Selection', WIDTH, HEIGHT, theme = pygame_menu.themes.THEME_BLUE)
        gameMenu.add.button('Math Quiz', MQ.quiz.play_function)
        gameMenu.add.button('Memory Game', memGame.play)
        gameMenu.add.button('Trizzle')
        gameMenu.add.button('Sliding Puzzle')
        gameMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Login Menu <--- ##
        accountLoginMenu = pygame_menu.Menu('Account Login', WIDTH, HEIGHT, theme = customMenu_theme)
        accountLoginMenu.add.text_input('E-mail: ', default = 'user@email.com')
        accountLoginMenu.add.text_input('Password: ', default = 'password')
        accountLoginMenu.add.button('Login')
        accountLoginMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Create Menu <--- ##
        accountCreateMenu = pygame_menu.Menu('Account Creation', WIDTH, HEIGHT, theme = customMenu_theme)
        accountCreateMenu.add.text_input('Username: ', default = 'user', onchange = main.setUserName)
        accountCreateMenu.add.text_input('Password: ', default = 'password', onchange = main.setUserPass)
        accountCreateMenu.add.text_input('Email Address: ', default = 'user@email.com')
        accountCreateMenu.add.button('Submit Account')
        accountCreateMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Stats Menu <--- ##
        accountStatsMenu = pygame_menu.Menu('Account Statistics', WIDTH, HEIGHT, theme = customMenu_theme)
        accountStatsMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Info Menu <--- ##
        accountInfoMenu = pygame_menu.Menu('Account', WIDTH, HEIGHT, theme = customMenu_theme)
        accountInfoMenu.add.button('Account Login', accountLoginMenu)
        accountInfoMenu.add.button('Create an Account', accountCreateMenu)
        accountInfoMenu.add.button('Account Statistics', accountStatsMenu)
        accountInfoMenu.add.button('Back', pygame_menu.events.BACK)

        # ---------------------------------
        # Create menus: Main
        # ---------------------------------
        main_menu = pygame_menu.Menu(
            '     Welcome to Puzzlify!', 
            WIDTH, HEIGHT, 
            theme = customMenu_theme
        )
        
        main_menu.add.button('Game Selection', gameMenu)
        main_menu.add.button('Account', accountInfoMenu)
        main_menu.add.button('Quit', pygame_menu.events.EXIT)
        # ---------------------------------
            
        # Main Loop
        while True:

            # Tick
            clock.tick(FPS)
                
            # Application Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit(0)

            # Main menu
            main_menu.enable()
            if main_menu.is_enabled():
                main_menu.mainloop(
                    SCREEN, 
                    main.main_background, 
                    disable_loop=test, 
                    fps_limit=FPS
                )

            # Flip surface
            pygame.display.flip()

            # At first loop returns
            if test:
                break

if __name__ == "__main__":
    main.main()
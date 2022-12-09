import pygame, pygame_menu
from customMenu_theme import *
import MathQuiz as MQ
from databaseConnection import *
from random import randrange
from typing import Tuple, Any, Optional, List
# import button, label
import constants

# GLOBAL VARIABLES
global USER32, WIDTH, HEIGHT, SCREEN, FPS, USERNAME, USERPASSWORD, USEREMAIL
USER32 = constants.USER32
WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT
SCREEN = constants.SCREEN
FPS = constants.FPS
USERNAME = constants.USERNAME
USERPASSWORD = constants.USERPASSWORD
USEREMAIL = constants.USEREMAIL

clock = constants.clock
main_menu = constants.main_menu

class main:

    def printCredentials(USERNAME, USERPASSWORD, USEREMAIL):
        print("USERNAME: ", USERNAME)
        print("USERPASSWORD: ", USERPASSWORD)
        print("USEREMAIL: ", USEREMAIL)

    def setUserName(username):
        USERNAME = username
        return USERNAME

    def setUserPass(userpassword):
        USERPASSWORD = userpassword
        return USERPASSWORD

    def setUserEmail(useremail):
        USEREMAIL = useremail
        return USEREMAIL

    def random_color() -> Tuple[int, int, int]:
        return randrange(0, 255), randrange(0, 255), randrange(0, 255)

    # login button action for account database
    def login():
        pass

    # sign up button action for account database
    def signup():
        cursor.execute("INSERT INTO [User](userName, userPassword, userEmail) VALUES (?,?,?);", USERNAME, USERPASSWORD, USEREMAIL)
        main.printCredentials(USERNAME, USERPASSWORD, USEREMAIL)
        cursor.commit()

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
        # Create menus: Play Math Quiz Menu
        # ---------------------------------
        mathQuiz = pygame_menu.Menu(
            'Math Quiz', 
            WIDTH, HEIGHT, 
            theme = customMenu_theme
        )

        mathQuiz.add.button('Start', 
                            MQ.quiz.play_function,
                            pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))
        mathQuiz.add.button('Return to main menu', pygame_menu.events.BACK)

        # ---------------------------------
        # Create menus: Sub Menus
        # ---------------------------------
        ### --> Game Selection Menu <--- ##
        gameMenu = pygame_menu.Menu('Game Selection', WIDTH, HEIGHT, theme = customMenu_theme)
        gameMenu.add.button('Math Quiz', mathQuiz)
        gameMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Login Menu <--- ##
        accountLoginMenu = pygame_menu.Menu('Account Login', WIDTH, HEIGHT, theme = customMenu_theme)
        accountLoginMenu.add.text_input('E-mail: ', default = 'user@email.com', onchange = USEREMAIL)
        accountLoginMenu.add.text_input('Password: ', default = 'password', onchange= USERPASSWORD)
        accountLoginMenu.add.button('Login', main.login)
        accountLoginMenu.add.button('Back', pygame_menu.events.BACK)

        # sign up button action for account database
        def signup():
            cursor.execute("INSERT INTO [User](userName, userPassword, userEmail) VALUES (?,?,?);", USERNAME, USERPASSWORD, USEREMAIL)
            main.printCredentials(USERNAME, USERPASSWORD, USEREMAIL)
            cursor.commit()

        ### --> Account Create Menu <--- ##
        accountCreateMenu = pygame_menu.Menu('Account Creation', WIDTH, HEIGHT, theme = customMenu_theme)
        accountCreateMenu.add.text_input('Username: ', default = 'user', onchange = main.setUserName)
        accountCreateMenu.add.text_input('Password: ', default = 'password', onchange = main.setUserPass)
        accountCreateMenu.add.text_input('Email Address: ', default = 'user@email.com', onchange = main.setUserEmail)
        accountCreateMenu.add.button('Submit Account', signup)
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





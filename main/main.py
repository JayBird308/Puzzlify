import pygame
import pygame_menu
from customMenu_theme import *
import ctypes
# import MathQuiz as MQ

# GLOBAL VARIABLES
global USER32, WIDTH, HEIGHT
USER32 = ctypes.windll.user32
WIDTH = USER32.GetSystemMetrics(0) # Monitor Resolution Width
HEIGHT = USER32.GetSystemMetrics(1) # Monitor Resolution Height
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

# Math quiz
def math_quiz():
    
    pass

# game selection sub menu
def game_select():
    gameMenu = pygame_menu.Menu('Game Selection', WIDTH, HEIGHT, theme = customMenu_theme)
    gameMenu.add.button('Math Quiz', math_quiz)
    gameMenu.add.button('Back', main)
    gameMenu.mainloop(SCREEN)
    pass

# account sub menu
def account_info():
    accountMenu = pygame_menu.Menu('Account', WIDTH, HEIGHT, theme = customMenu_theme)
    accountMenu.add.button('Account Login', account_login)
    accountMenu.add.button('Create an Account', account_create)
    accountMenu.add.button('Account Statistics', account_stats)
    accountMenu.add.button('Back', main)
    accountMenu.mainloop(SCREEN)
    pass

# account creation sub menu
def account_create():
    accountMenu = pygame_menu.Menu('Account Creation', WIDTH, HEIGHT, theme = customMenu_theme)
    accountMenu.add.text_input('Username: ', default = 'user')
    accountMenu.add.text_input('Password: ', default = 'password')
    accountMenu.add.text_input('Email Address: ', default = 'user@email.com')
    accountMenu.add.button('Submit Account', signup)
    accountMenu.add.button('Back', account_info)
    accountMenu.mainloop(SCREEN)
    pass

# account login sub menu
def account_login():
    accountMenu = pygame_menu.Menu('Account Login', WIDTH, HEIGHT, theme = customMenu_theme)
    accountMenu.add.text_input('Username: ', default = 'user')
    accountMenu.add.text_input('Password: ', default = 'password')
    accountMenu.add.button('Login', login)
    accountMenu.add.button('Back', account_info)
    accountMenu.mainloop(SCREEN)
    pass

# account statistics sub menu
def account_stats():
    accountMenu = pygame_menu.Menu('Account Statistics', WIDTH, HEIGHT, theme = customMenu_theme)
    accountMenu.add.button('Back', account_info)
    accountMenu.mainloop(SCREEN)
    pass

# login button action for account database
def login():
    
    pass

# sign up button action for account database
def signup():
    
    pass

def main():
    # database connection
    # myconn = mysql.connector.connect(host = "mysql.play.planbook.xyz", user = "play_dev0", passwd = "Play_Dev_0")
    # print(myconn)

    # initialize the pygame module
    pygame.init()

    # load and set pygame window and clock
    clock = pygame.time.Clock()

    # adds menu options
    menu = pygame_menu.Menu('Welcome to Puzzlify!', WIDTH, HEIGHT, theme = customMenu_theme)
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
        menu.mainloop(SCREEN)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":

    # call main
    main()

    # object = MQ.quiz()

    # MQ.__init__()






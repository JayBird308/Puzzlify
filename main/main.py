import pygame
import pygame_menu
from customMenu_theme import *
import ctypes
import MathQuiz as MQ
from random import randrange
import random
from typing import Tuple, Any, Optional, List
import button

# GLOBAL VARIABLES
global USER32, WIDTH, HEIGHT, SCREEN
USER32 = ctypes.windll.user32
# WIDTH = USER32.GetSystemMetrics(0) # Monitor Resolution Width
# HEIGHT = USER32.GetSystemMetrics(1) # Monitor Resolution Height

WIDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

FPS = 60
clock: Optional['pygame.time.Clock'] = None
main_menu: Optional['pygame_menu.Menu'] = None

# call back functions
def fn1():
    print('button1')
def fn2():
    print('button2')

def random_color() -> Tuple[int, int, int]:
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)

def play_function(font: 'pygame.font.Font', test: bool = False) -> None:
    # Define globals
    global main_menu
    global clock

    # Get initial values
    question = MQ.quiz.generate_question()
    num1 = random.randint(0, 10)
    num2 = MQ.quiz.get_solution()
    print("Num1: " + num1.__str__())
    print("Num2: " + num2.__str__())

    # Draw random color and text
    # bg_color = random_color()
    bg_color = (0, 120, 120)

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.full_reset()

    frame = 0
    while True:

        # noinspection PyUnresolvedReferences
        clock.tick(60)
        frame += 1

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    main_menu.enable()
                    return
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    pos = pygame.mouse.get_pos()
                    for b in button_list:
                        if b.rect.collidepoint(pos):
                            b.call_back()

        # Pass events to main_menu
        if main_menu.is_enabled():
            main_menu.update(events)

        center_w = WIDTH/2
        center_h = HEIGHT/2

        # Continue playing
        SCREEN.fill(bg_color)
        button1 = button.button(
            position=(center_w, center_h), 
            size=(125, 60), 
            clr=(220, 220, 220), 
            cngclr=(255, 0, 0), 
            func=fn1, 
            text='button1'
        )

        button2 = button.button(
            (center_w, center_h+100), 
            (125, 60), 
            (220, 220, 220), 
            (255, 0, 0), 
            fn2, 
            'button2'
        )
        button_list = [button1, button2]
        for b in button_list:
            b.draw(SCREEN)

        pygame.display.flip()

        # If test returns
        if test and frame == 2:
            break
pass

# login button action for account database
def login():
    pass

# sign up button action for account database
def signup():
    pass

def main_background() -> None:
    """ Function used by menus, draw on background while menu is active."""
    SCREEN.fill((128, 0, 128))

def main(test: bool = False) -> None:
    global clock
    global main_menu

    # initialize the pygame module
    pygame.init()

    # load and set pygame window and clock
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
                         play_function,
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
    accountLoginMenu.add.text_input('Username: ', default = 'user')
    accountLoginMenu.add.text_input('Password: ', default = 'password')
    accountLoginMenu.add.button('Login', login)
    accountLoginMenu.add.button('Back', pygame_menu.events.BACK)

    ### --> Account Create Menu <--- ##
    accountCreateMenu = pygame_menu.Menu('Account Creation', WIDTH, HEIGHT, theme = customMenu_theme)
    accountCreateMenu.add.text_input('Username: ', default = 'user')
    accountCreateMenu.add.text_input('Password: ', default = 'password')
    accountCreateMenu.add.text_input('Email Address: ', default = 'user@email.com')
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
            main_menu.mainloop(SCREEN, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break

if __name__ == "__main__":
    main()





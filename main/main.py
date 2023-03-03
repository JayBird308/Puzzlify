import pygame, pygame_menu, pygame_menu.widgets, pygame_menu.locals
import customMenu_theme as ct
import MathQuiz as MQ
import memory as memGame
import trizzleGame as triGame
import Sliding_Puzzle as sliGame
from databaseConnection import *
from user import *
import constants

# GLOBAL VARIABLES
WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT
SCREEN = constants.SCREEN
FPS = constants.FPS
previous_value = 0

clock = constants.clock
main_menu = constants.main_menu
customMenu_theme = ct.customMenu_theme

# main class
class main:
    def setUserName(username):
        UserAccount.username = username
        return UserAccount.username

    def setUserPass(userpassword):
        UserAccount.password = userpassword
        return UserAccount.password

    def setUserEmail(useremail):
        UserAccount.email = useremail
        return UserAccount.email

    # login button action for account database
    def login():
        print(UserAccount.email)
        print(UserAccount.password)
        pass

    # sign up button action for account database
    def signup():
        UserAccount.memGamesPlayed = 0
        UserAccount.memHighScore = 0
        UserAccount.trizGamesPlayed = 0
        UserAccount.trizHighScore = 0
        UserAccount.mqGamesPlayed = 0
        UserAccount.mqHighScore = 0
        UserAccount.slidingGamesPlayed = 0
        UserAccount.slidingHighScore = 0

        userdata = UserAccount(UserAccount.username, UserAccount.password, UserAccount.email,UserAccount.memGamesPlayed, UserAccount.memHighScore, UserAccount.trizGamesPlayed, UserAccount.trizHighScore, UserAccount.mqGamesPlayed, UserAccount.mqHighScore, UserAccount.slidingGamesPlayed, UserAccount.slidingHighScore)
        userJson = json.dumps(userdata, indent=4, cls=UserEncoder)
        users_ref = ref.child('users')
        users_ref.push(userJson)
        pass           

    def set_difficulty_type():
        difficulty = 0

    def print_value(value):
        global previous_value
        if value != previous_value:
            print(f'Value changed to {value}.')
            previous_value = value

    def main(test: bool = False) -> None:
        global main_menu, clock
        global previous_value

        # initialize
        pygame.init()
        clock = pygame.time.Clock()

        # ---------------------------------
        # Create menus: Sub Menus
        # ---------------------------------
        ### --> Game Selection Menu <--- ##
        gameMenu = pygame_menu.Menu('Game Selection', WIDTH, HEIGHT, theme = customMenu_theme)
        # gameMenu.add.button('Math Quiz', MQ.quiz.play_function)

        selector = pygame_menu.widgets.Selector(
            'Difficulty:',
            [('     Easy    ', 0), ('Advanced', 1)],
            default=0,
            onchange=lambda widget, value: main.print_value(value)
        )
        previous_value = selector.get_value()

        gameMenu.add.selector(selector._title, selector._items,
                                    onchange=selector._onchange,
                                    default=selector._default_value)

        gameMenu.add.button("Math Quiz", MQ.quiz.test)
        gameMenu.add.button('Memory Game', memGame.main)
        gameMenu.add.button('Trizzle', triGame.run)
        gameMenu.add.button('Sliding Puzzle', sliGame.main)
        gameMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Login Menu <--- ##
        accountLoginMenu = pygame_menu.Menu('Account Login', WIDTH, HEIGHT, theme = customMenu_theme)
        accountLoginMenu.add.text_input('E-mail: ', default = 'user@email.com', onchange = main.setUserEmail)
        accountLoginMenu.add.text_input('Password: ', default = 'password', onchange= main.setUserPass)
        accountLoginMenu.add.button('Login', main.login)
        accountLoginMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Create Menu <--- ##
        accountCreateMenu = pygame_menu.Menu('Account Creation', WIDTH, HEIGHT, theme = customMenu_theme)
        accountCreateMenu.add.text_input('Username: ', default = 'user', onchange = main.setUserName)
        accountCreateMenu.add.text_input('Password: ', default = 'password', onchange = main.setUserPass)
        accountCreateMenu.add.text_input('Email Address: ', default = 'user@email.com', onchange = main.setUserEmail)
        accountCreateMenu.add.button('Submit Account', main.signup)
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
            'Welcome to Puzzlify!', 
            WIDTH, HEIGHT, 
            theme = customMenu_theme
        )

        main_menu.add.button('Game Selection', gameMenu)
        main_menu.add.button('Account', accountInfoMenu)
        main_menu.add.button('Quit', pygame_menu.events.EXIT)

        # ---------------------------------
        # pygame.mixer.init()
        # pygame.mixer.music.load('main/track1.mp3')
        # pygame.mixer.music.play()
        # pygame.mixer.music.set_volume(0.2)

        # Set the menu
        current_menu = main_menu

        # Main Loop
        while True:
            clock.tick(FPS)

            # Event Handling
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit(0)
            current_menu.update(events)

            # Enable current menu & Force render
            current_menu.enable()
            if current_menu != gameMenu:
                gameMenu.disable()
            if current_menu != accountLoginMenu:
                accountLoginMenu.disable()
            if current_menu != accountCreateMenu:
                accountCreateMenu.disable()
            if current_menu != accountStatsMenu:
                accountStatsMenu.disable()
            if current_menu != accountInfoMenu:
                accountInfoMenu.disable()

            # If NOT enabled, enable it
            # If enabled, draw to SCREEN
            if current_menu.is_enabled() == False:
                current_menu.enable()
            if current_menu.is_enabled() == True:
                current_menu.draw(SCREEN)

            pygame.display.update()

            # At first loop returns
            if test:
                break

if __name__ == "__main__":
    main.main()





import pygame, pygame_menu, pygame_menu.widgets, pygame_menu.locals
import customMenu_theme as ct
import json
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
    
    def setUserStats(user: UserAccount):
        pass

    # login button action for account database
    def login():
        updatedUsersRefString = refString + "/" + UserAccount.username
        userRef = db.reference(updatedUsersRefString)
        userData = userRef.get()
        userKeys = list(userData.keys())
        json_key = userData[userKeys[0]]
        user_data_dict = json.loads(json_key)
        UserAccount.username = user_data_dict['username']
        UserAccount.password = user_data_dict['password']
        UserAccount.key = userKeys[0]
        UserAccount.memGamesPlayed = user_data_dict['memGamesPlayed']
        UserAccount.memHighScore = user_data_dict['memHighScore']
        UserAccount.trizGamesPlayed = user_data_dict['trizGamesPlayed']
        UserAccount.trizHighScore = user_data_dict['trizHighScore']
        UserAccount.mqGamesPlayed = user_data_dict['mqGamesPlayed']
        UserAccount.mqHighScore = user_data_dict['mqHighScore']
        UserAccount.slidingGamesPlayed = user_data_dict['slidingGamesPlayed']
        UserAccount.slidingHighScore = user_data_dict['slidingHighScore']
        print(UserAccount.username)
        print(UserAccount.password)
        print(UserAccount.key)
        return UserAccount

    # sign up button action for account database
    def signup():
        UserAccount.key = ""
        UserAccount.memGamesPlayed = 0
        UserAccount.memHighScore = 0
        UserAccount.trizGamesPlayed = 0
        UserAccount.trizHighScore = 0
        UserAccount.mqGamesPlayed = 0
        UserAccount.mqHighScore = 0
        UserAccount.slidingGamesPlayed = 0
        UserAccount.slidingHighScore = 0

        userdata = UserAccount(UserAccount.username, UserAccount.password, UserAccount.key, UserAccount.memGamesPlayed, UserAccount.memHighScore, UserAccount.trizGamesPlayed, UserAccount.trizHighScore, UserAccount.mqGamesPlayed, UserAccount.mqHighScore, UserAccount.slidingGamesPlayed, UserAccount.slidingHighScore)
        userJson = json.dumps(userdata, indent=4, cls=UserEncoder)
        users_ref = ref.child(UserAccount.username)
        users_ref.push(userJson)
        pass

    def set_difficulty_type(num):
        difficulty = num
        print('Difficulty set:', difficulty)

    def print_value(value):
        global previous_value
        if value != previous_value:
            # print(f'Value changed to {value}.')
            previous_value = value
            main.set_difficulty_type(previous_value)

    def main(test: bool = False) -> None:
        UserAccount.username = ""
        UserAccount.password = ""
        UserAccount.key = ""
        UserAccount.memGamesPlayed = 0
        UserAccount.memHighScore = 0
        UserAccount.trizGamesPlayed = 0
        UserAccount.trizHighScore = 0
        UserAccount.mqGamesPlayed = 0
        UserAccount.mqHighScore = 0
        UserAccount.slidingGamesPlayed = 0
        UserAccount.slidingHighScore = 0

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
        accountLoginMenu.add.text_input('Username: ', default = 'user', onchange = main.setUserName)
        accountLoginMenu.add.text_input('Password: ', default = 'password', onchange= main.setUserPass)
        accountLoginMenu.add.button('Login', main.login)
        accountLoginMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Create Menu <--- ##
        accountCreateMenu = pygame_menu.Menu('Account Creation', WIDTH, HEIGHT, theme = customMenu_theme)
        accountCreateMenu.add.text_input('Username: ', default = 'user', onchange = main.setUserName)
        accountCreateMenu.add.text_input('Password: ', default = 'password', onchange = main.setUserPass)
        accountCreateMenu.add.button('Submit Account', main.signup)
        accountCreateMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Stats Menu <--- ##
        accountStatsMenu = pygame_menu.Menu('Account Statistics', WIDTH, HEIGHT, theme = customMenu_theme)
        accountStatsMenu.add.label('Memory Game High Schore: ' + str(UserAccount.memHighScore))
        accountStatsMenu.add.label('Trizzle High Score: ' + str(UserAccount.trizHighScore))
        accountStatsMenu.add.label('Math Quiz High Score: ' + str(UserAccount.mqHighScore))
        accountStatsMenu.add.label('Sliding Game High Score: ' + str(UserAccount.slidingHighScore))
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
            'Welcome to Puzzlify' + UserAccount.username + "!", 
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

            # Enable current menu
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





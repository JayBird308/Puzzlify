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
from tkinter import *

#-----------------------------
# FOR TESTING ACCOUNT STUFF USE:
# username: Jay
# password: pass
# memHighScore should be = 100
#-----------------------------

# GLOBAL VARIABLES
WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT
SCREEN = constants.SCREEN
FPS = constants.FPS
previous_value = 0

clock = constants.clock
main_menu = constants.main_menu
customMenu_theme = ct.customMenu_theme

# ---------------------------------
# Create menus: Main Menu
# ---------------------------------
main_menu = pygame_menu.Menu(
    'Welcome to Puzzlify!',
    WIDTH, HEIGHT,
    theme = customMenu_theme)
# ---------------------------------
# Create menus: Account Stats
# ---------------------------------
accountStatsMenu = pygame_menu.Menu(
    'Account Statistics', 
    WIDTH, HEIGHT, 
    theme = customMenu_theme)
# ---------------------------------
# Create menus: Account
# ---------------------------------
accountInfoMenu = pygame_menu.Menu(
    'Account', 
    WIDTH, HEIGHT, 
    theme = customMenu_theme)
# ---------------------------------
# Create menus: Account Signup
# ---------------------------------
accountCreateMenu = pygame_menu.Menu(
    'Account Creation', 
    WIDTH, HEIGHT, 
    theme = customMenu_theme)
# ---------------------------------
# Create menus: Account Login
# ---------------------------------
accountLoginMenu = pygame_menu.Menu(
    'Account Login',
    WIDTH, HEIGHT,
    theme = customMenu_theme)
# ---------------------------------
# Create menus: Game Selection
# ---------------------------------
gameMenu = pygame_menu.Menu(
    'Game Selection', 
    WIDTH, HEIGHT, 
    theme = customMenu_theme)

# main class
class main:
    # pop up window for bad username
    def bad_user_popup():
        window = Tk()
        window.title('Incorrect Username Warning')
        msg = Label(window, text="Incorrect Username", fg='red', font=("Helvetica", 16))
        msg.place(x=60, y=50)
        window.geometry("300x200+700+400")
        window.mainloop()
        pass

    # pop up window for good username but bad password credentials
    def bad_pass_popup():
        window = Tk()
        window.title('Incorrect Password Warning')
        msg = Label(window, text="Incorrect Password", fg='red', font=("Helvetica", 16))
        msg.place(x=60, y=50)
        window.geometry("300x200+700+400")
        window.mainloop()
        pass

    # pop up window for good login credentials 
    def good_login_popup():
        window = Tk()
        window.title('Log In Success')
        msg = Label(window, text="Successful Log In!", fg='green', font=("Helvetica", 16))
        msg.place(x=60, y=50)
        window.geometry("300x200+700+400")
        window.mainloop()
        pass

    def setUserName(username):
        tempUser.username = username
        return tempUser.username

    def setUserPass(userpassword):
        tempUser.password = userpassword
        return tempUser.password

    # login button action for account database
    def login():
        updatedUsersRefString = refString + "/" + tempUser.username
        try:
            userRef = db.reference(updatedUsersRefString)
            userData = userRef.get()
            userKeys = list(userData.keys())
            json_key = userData[userKeys[0]]
            user_data_dict = json.loads(json_key)
            currentLoggedInUser.username = user_data_dict['username']
            currentLoggedInUser.password = user_data_dict['password']
            if currentLoggedInUser.username == tempUser.username and currentLoggedInUser.password == tempUser.password:
                currentLoggedInUser.key = userKeys[0]
                currentLoggedInUser.memGamesPlayed = user_data_dict['memGamesPlayed']
                currentLoggedInUser.memHighScore = user_data_dict['memHighScore']
                currentLoggedInUser.trizGamesPlayed = user_data_dict['trizGamesPlayed']
                currentLoggedInUser.trizHighScore = user_data_dict['trizHighScore']
                currentLoggedInUser.mqGamesPlayed = user_data_dict['mqGamesPlayed']
                currentLoggedInUser.mqHighScore = user_data_dict['mqHighScore']
                currentLoggedInUser.slidingGamesPlayed = user_data_dict['slidingGamesPlayed']
                currentLoggedInUser.slidingHighScore = user_data_dict['slidingHighScore']
                main_menu.set_title('Welcome to Puzzlify, ' + currentLoggedInUser.username + "!")
                accountInfoMenu.set_title(currentLoggedInUser.username + "'s" + ' Account')
                accountStatsMenu.set_onwidgetchange(accountStatsMenu, '1')
                print("Memory High Score: " + str(currentLoggedInUser.memHighScore))
                main.good_login_popup()
                return currentLoggedInUser
            else:
                main.bad_pass_popup()
                print("Incorrect Password")
            return currentLoggedInUser
        except:
            main.bad_user_popup()
            print("Incorrect Username")
        return currentLoggedInUser

    # sign up button action for account database
    def signup():
        tempUser.key = ""
        tempUser.memGamesPlayed = 0
        tempUser.memHighScore = 0
        tempUser.trizGamesPlayed = 0
        tempUser.trizHighScore = 0
        tempUser.mqGamesPlayed = 0
        tempUser.mqHighScore = 0
        tempUser.slidingGamesPlayed = 0
        tempUser.slidingHighScore = 0
        userJson = json.dumps(tempUser, indent=4, cls=UserEncoder)
        users_ref = ref.child(tempUser.username)
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
        
        global main_menu, clock
        global previous_value

        # initialize
        pygame.init()
        clock = pygame.time.Clock()

        
        ### --> Game Select Buttons <-- ###
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

        ### --> Account Login Buttons <-- ###
        accountLoginMenu.add.text_input('Username: ', default = 'user', onchange = main.setUserName)
        accountLoginMenu.add.text_input('Password: ', default = 'password', onchange= main.setUserPass)
        accountLoginMenu.add.button('Login', main.login)
        accountLoginMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Create Buttons <-- ###
        accountCreateMenu.add.text_input('Username: ', default = 'user', onchange = main.setUserName)
        accountCreateMenu.add.text_input('Password: ', default = 'password', onchange = main.setUserPass)
        accountCreateMenu.add.button('Submit Account', main.signup)
        accountCreateMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Stats Buttons <-- ###
        accountStatsMenu.add.label('Memory Game High Schore: ' + str(currentLoggedInUser.memHighScore), '1')
        accountStatsMenu.add.label('Trizzle High Score: ' + str(currentLoggedInUser.trizHighScore), '2')
        accountStatsMenu.add.label('Math Quiz High Score: ' + str(currentLoggedInUser.mqHighScore), '3')
        accountStatsMenu.add.label('Sliding Game High Score: ' + str(currentLoggedInUser.slidingHighScore), '4')
        accountStatsMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Menu Buttons <-- ###
        accountInfoMenu.add.button('Account Login', accountLoginMenu)
        accountInfoMenu.add.button('Create an Account', accountCreateMenu)
        accountInfoMenu.add.button('Account Statistics', accountStatsMenu)
        accountInfoMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Main Menu Buttons <--- ###
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





import pygame
import pygame_menu
import pygame_menu.widgets
import pygame_menu.locals
import customMenu_theme as ct
import json
import unscramble
import memory as memGame
import Sliding_Puzzle as sliGame
import Minesweeper as MS
from databaseConnection import *
from user import *
import constants
from tkinter import *

# -----------------------------
# FOR TESTING ACCOUNT STUFF USE:
# username: Jay
# password: pass
# -----------------------------

# GLOBAL VARIABLES
WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT
SCREEN = constants.SCREEN
FPS = constants.FPS
diff_value = 0

clock = constants.clock
main_menu = constants.main_menu
customMenu_theme = ct.customMenu_theme
customStats_theme = ct.customStats_theme
customLb_theme = ct.customLB_theme

# ---------------------------------
# Create menus: Main Menu
# ---------------------------------
main_menu = pygame_menu.Menu(
    'Welcome to Puzzlify!',
    WIDTH, HEIGHT,
    theme=customMenu_theme)
# ---------------------------------
# Create menus: Account Stats
# ---------------------------------
accountStatsMenu = pygame_menu.Menu(
    'Account Statistics',
    WIDTH, HEIGHT,
    theme=customStats_theme)
# ---------------------------------
# Create menus: Account
# ---------------------------------
accountInfoMenu = pygame_menu.Menu(
    'Account',
    WIDTH, HEIGHT,
    theme=customMenu_theme)
# ---------------------------------
# Create menus: Account Signup
# ---------------------------------
accountCreateMenu = pygame_menu.Menu(
    'Account Creation',
    WIDTH, HEIGHT,
    theme=customMenu_theme)
# ---------------------------------
# Create menus: Account Login
# ---------------------------------
accountLoginMenu = pygame_menu.Menu(
    'Account Login',
    WIDTH, HEIGHT,
    theme=customMenu_theme)
# ---------------------------------
# Create menus: Game Selection
# ---------------------------------
gameMenu = pygame_menu.Menu(
    'Game Selection',
    WIDTH, HEIGHT,
    theme=customMenu_theme)
# ---------------------------------
# Create menus: Leaderboards
# ---------------------------------
leaderboardMenu = pygame_menu.Menu(
    'Puzzle Leaderboards',
    WIDTH, HEIGHT,
    theme=customLb_theme)

# widget manager for buttons
WidgetManager = pygame_menu._widgetmanager.WidgetManager(gameMenu)
# loads in images for each game's button:
# memory game image
memory_image_file = 'main\\images\\memory.png'
memory_image = pygame_menu.baseimage.BaseImage(memory_image_file, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
memory_image.scale(0.30, 0.30, True)

# unscramble game image
unscramble_image_file = 'main\\images\\unscramble.png'
unscramble_image = pygame_menu.baseimage.BaseImage(unscramble_image_file, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
unscramble_image.scale(0.30, 0.30, True)

# minesweeper game image
minesweeper_image_file = 'main\\images\\minesweeper.png'
minesweeper_image = pygame_menu.baseimage.BaseImage(minesweeper_image_file, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
minesweeper_image.scale(0.30, 0.30, True)

# sliding game image
sliding_image_file = 'main\\images\\sliding.png'
sliding_image = pygame_menu.baseimage.BaseImage(sliding_image_file, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
sliding_image.scale(0.15, 0.15, True)

# main class

class main:

    def close_window(root, event):
        root.destroy()

    # pop up window for bad username
    def bad_user_popup():
        window = Tk()
        window.title('Incorrect Username Warning')
        msg = Label(window, text="Incorrect Username",
                    fg='red', font=("Helvetica", 16))
        msg.place(x=60, y=50)
        window.geometry("300x200+700+400")
        window.bind("<Escape>", lambda event: main.close_window(window, event))
        window.mainloop()

    # pop up window for good username but bad password credentials
    def bad_pass_popup():
        window = Tk()
        window.title('Incorrect Password Warning')
        msg = Label(window, text="Incorrect Password",
                    fg='red', font=("Helvetica", 16))
        msg.place(x=60, y=50)
        window.geometry("300x200+700+400")
        window.bind("<Escape>", lambda event: main.close_window(window, event))
        window.mainloop()

    # pop up window for good login credentials
    def good_login_popup():
        window = Tk()
        window.title('Log In Success')
        msg = Label(window, text="Successful Log In!",
                    fg='green', font=("Helvetica", 16))
        msg.place(x=60, y=50)
        window.geometry("300x200+700+400")
        window.bind("<Escape>", lambda event: main.close_window(window, event))
        window.mainloop()

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
                currentLoggedInUser.msGamesPlayed = user_data_dict['msGamesPlayed']
                currentLoggedInUser.msHighScore = user_data_dict['msHighScore']
                currentLoggedInUser.unscrambleGamesPlayed = user_data_dict['unscrambleGamesPlayed']
                currentLoggedInUser.unscrambleHighScore = user_data_dict['unscrambleHighScore']
                currentLoggedInUser.slidingGamesPlayed = user_data_dict['slidingGamesPlayed']
                currentLoggedInUser.slidingHighScore = user_data_dict['slidingHighScore']
                main_menu.set_title(
                    'Welcome to Puzzlify, ' + currentLoggedInUser.username + "!")
                accountInfoMenu.set_title(
                    currentLoggedInUser.username + "'s" + ' Account')
                print("Memory High Score: " +
                      str(currentLoggedInUser.memHighScore))
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

    # sign out function
    def signout():
        def bad_sign_out_popup():
            window = Tk()
            window.title('Sign out Failure')
            msg = Label(window, text="No account signed in",
                        fg='red', font=("Helvetica", 16))
            msg.place(x=60, y=50)
            window.geometry("300x200+700+400")
            window.bind(
                "<Escape>", lambda event: main.close_window(window, event))
            window.mainloop()

        def sign_out_popup():
            window = Tk()
            window.title('Sign out Success')
            msg = Label(window, text="Sign out Successful!",
                        fg='green', font=("Helvetica", 16))
            msg.place(x=60, y=50)
            window.geometry("300x200+700+400")
            window.bind(
                "<Escape>", lambda event: main.close_window(window, event))
            window.mainloop()

        if currentLoggedInUser.username == "":
            bad_sign_out_popup()
        else:
            currentLoggedInUser.reset()
            accountInfoMenu.set_title("Account")
            main_menu.set_title("Welcome to Puzzlify!")
            sign_out_popup()

    # sign up button action for account database
    def signup():

        # pop up window for successful signup
        def good_signup():
            window = Tk()
            window.title('Sign up Success')
            msg = Label(window, text="Sign up Successful!",
                        fg='green', font=("Helvetica", 16))
            msg.place(x=60, y=50)
            window.geometry("300x200+700+400")
            window.bind(
                "<Escape>", lambda event: main.close_window(window, event))
            window.mainloop()

        # pop up window for successful signup
        def bad_signup():
            window = Tk()
            window.title('Sign up Warning')
            msg = Label(window, text="Sign up Failed, Please Try Again.",
                        fg='red', font=("Helvetica", 16))
            msg.place(x=60, y=50)
            window.geometry("300x200+700+400")
            window.bind(
                "<Escape>", lambda event: main.close_window(window, event))
            window.mainloop()

        tempUser.key = ""
        tempUser.memGamesPlayed = 0
        tempUser.memHighScore = 0
        tempUser.msGamesPlayed = 0
        tempUser.msHighScore = 0
        tempUser.unscrambleGamesPlayed = 0
        tempUser.unscrambleHighScore = 0
        tempUser.slidingGamesPlayed = 0
        tempUser.slidingHighScore = 0
        try:
            userJson = json.dumps(tempUser, indent=4, cls=UserEncoder)
            users_ref = ref.child(tempUser.username)
            users_ref.push(userJson)
            good_signup()
        except:
            bad_signup()

    def set_difficulty_type(num):
        difficulty = num
        print('Difficulty set:', difficulty)

    def print_value(value):
        global diff_value
        if value != diff_value:
            # print(f'Value changed to {value}.')
            diff_value = value
            constants.DIFFICULTY = diff_value
            main.set_difficulty_type(diff_value)

    def main(test: bool = False) -> None:

        global main_menu, clock
        global diff_value

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
        diff_value = selector.get_value()
        gameMenu.add.selector(selector._title, selector._items,
                              onchange=selector._onchange,
                              default=selector._default_value)
        
        # game buttons with images:
        # memory button
        memory_banner = WidgetManager.banner(
        image=memory_image,
        action=memGame.main,
        align=pygame_menu.locals.ALIGN_CENTER,
        border_inflate=(5,5),
        button_id='memory_banner_id',
	    float=True,
        selection_color=[125,0,0,255],
        padding=(0,25,0,25),
        shadow_type='rectangular',
        shadow_radius=100,
        shadow_width=25
    )
        # unscramble button
        unscramble_banner = WidgetManager.banner(
        image=unscramble_image,
        action=unscramble.play,
        align=pygame_menu.locals.ALIGN_CENTER,
        border_inflate=(5,5),
        button_id='unscramble_banner_id',
	    float=True,
        selection_color=[125,0,0,255],
        padding=(0,25,0,25),
        shadow_type='rectangular',
        shadow_radius=100,
        shadow_width=25
    )
        #minesweeper button
        minesweeper_banner = WidgetManager.banner(
        image=minesweeper_image,
        action=MS.gameLoop,
        align=pygame_menu.locals.ALIGN_CENTER,
        border_inflate=(5,5),
        button_id='minesweeper_banner_id',
	    float=True,
        selection_color=[125,0,0,255],
        padding=(0,25,0,25),
        shadow_type='rectangular',
        shadow_radius=100,
        shadow_width=25
    )
         #sliding puzzle button
        sliding_banner = WidgetManager.banner(
        image=sliding_image,
        action=sliGame.main,
        align=pygame_menu.locals.ALIGN_CENTER,
        border_inflate=(5,5),
        button_id='sliding_banner_id',
	    float=True,
        selection_color=[125,0,0,255],
        padding=(0,25,0,25),
        shadow_type='rectangular',
        shadow_radius=100,
        shadow_width=25
    )

        gameMenu.add.button('Back', pygame_menu.events.BACK)

        # positions the picture along the banner
        memory_banner.translate(-350,250)
        unscramble_banner.translate(-150,250)
        minesweeper_banner.translate(100,250)
        sliding_banner.translate(350,250)
        

        ### --> Account Login Buttons <-- ###
        accountLoginMenu.add.text_input(
            'Username: ', default='user', onchange=main.setUserName)
        accountLoginMenu.add.text_input(
            'Password: ', default='password', onchange=main.setUserPass)
        accountLoginMenu.add.button('Login', main.login)
        accountLoginMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Create Buttons <-- ###
        accountCreateMenu.add.text_input(
            'Username: ', default='user', onchange=main.setUserName)
        accountCreateMenu.add.text_input(
            'Password: ', default='password', onchange=main.setUserPass)
        accountCreateMenu.add.button('Submit Account', main.signup)
        accountCreateMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Stats Buttons <--- ##

        def refresh_stats():
            memLabel.set_title('Easy Memory Game High Score: ' +
                               str(currentLoggedInUser.memHighScore))
            advMemLabel.set_title('Advanced Memory Game High Score: ' +
                               str(currentLoggedInUser.advMemHighScore))
            msLabel.set_title('Easy Minesweeper High Score: ' +
                              str(currentLoggedInUser.msHighScore))
            advMsLabel.set_title('Advanced Minesweeper High Score: ' +
                              str(currentLoggedInUser.advMsHighScore))
            unscrambleLabel.set_title('Easy Unscramble High Score: ' +
                                      str(currentLoggedInUser.unscrambleHighScore))
            advUnscrambleLabel.set_title('Advanced Unscramble High Score: ' +
                                      str(currentLoggedInUser.advUnscrambleHighScore))
            sliLabel.set_title('Easy Sliding Game High Score: ' +
                               str(currentLoggedInUser.slidingHighScore))
            advSliLabel.set_title('Advanced Sliding Game High Score: ' +
                               str(currentLoggedInUser.advSlidingHighScore))
            accountStatsMenu.render()

        memLabel = accountStatsMenu.add.label(
            'Easy Memory Game High Score: ' + str(currentLoggedInUser.memHighScore))
        advMemLabel = accountStatsMenu.add.label(
            'Advanced Memory Game High Score: ' + str(currentLoggedInUser.advMemHighScore))
        msLabel = accountStatsMenu.add.label(
            'Minesweeper High Score: ' + str(currentLoggedInUser.msHighScore))
        advMsLabel = accountStatsMenu.add.label(
            'Advanced Minesweeper High Score: ' + str(currentLoggedInUser.advMsHighScore))
        unscrambleLabel = accountStatsMenu.add.label(
            'Unscramble High Score: ' + str(currentLoggedInUser.unscrambleHighScore))
        advUnscrambleLabel = accountStatsMenu.add.label(
            'Advanced Unscramble High Score: ' + str(currentLoggedInUser.advUnscrambleHighScore))
        sliLabel = accountStatsMenu.add.label(
            'Sliding Game High Score: ' + str(currentLoggedInUser.slidingHighScore))
        advSliLabel = accountStatsMenu.add.label(
            'Advanced Sliding Game High Score: ' + str(currentLoggedInUser.advSlidingHighScore))
        
        accountStatsMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Account Menu Buttons <-- ###
        accountInfoMenu.add.button('Account Login', accountLoginMenu)
        accountInfoMenu.add.button('Create an Account', accountCreateMenu)
        accountInfoMenu.add.button('Account Statistics', accountStatsMenu)
        accountInfoMenu.add.button('Sign Out', main.signout)
        accountInfoMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Leaderboard Menu labels <-- ###
        def refresh_lb_stats():
            memLBLabel.set_title(
                'Memory Game Easy Leader:   ' + str(memHighestScore) + ' - ' + str(memHighestScorePlayer))
            advMemLBLabel.set_title(
                'Memory Game Adv. Leader:   ' + str(advMemHighestScore) + ' - ' + str(advMemHighestScorePlayer))
            msLBLabel.set_title(
                'Minesweeper Easy Leader:   ' + str(msHighestScore) + ' - ' + str(msHighestScorePlayer))
            advMsLBLabel.set_title(
                'Minesweeper Adv. Leader:   ' + str(advMsHighestScore) + ' - ' + str(advMsHighestScorePlayer))
            unscrambleLBLabel.set_title(
                'Unscramble Easy Leader:    ' + str(unscrambleHighestScore) + ' - ' + str(unscrambleHighestScorePlayer))
            advUnscrambleLBLabel.set_title(
                'Unscramble Adv. Leader:    ' + str(advUnscrambleHighestScore) + ' - ' + str(advUnscrambleHighestScorePlayer))
            sliLBLabel.set_title(
                'Sliding Game Easy Leader: ' + str(slidingHighestScore) + ' - ' + str(slidingHighestScorePlayer))
            advSliLBLabel.set_title(
                'Sliding Game Adv. Leader: ' + str(advSlidingHighestScore) + ' - ' + str(advSlidingHighestScorePlayer))
            leaderboardMenu.render()

        memLBLabel = leaderboardMenu.add.label(
                'Memory Game Easy Leader:   ' + str(memHighestScore) + ' - ' + str(memHighestScorePlayer))
        advMemLBLabel = leaderboardMenu.add.label(
                'Memory Game Adv. Leader:   ' + str(advMemHighestScore) + ' - ' + str(advMemHighestScorePlayer))
        msLBLabel = leaderboardMenu.add.label(
                'Minesweeper Easy Leader:   ' + str(msHighestScore) + ' - ' + str(msHighestScorePlayer))
        advMsLBLabel = leaderboardMenu.add.label(
                'Minesweeper Adv. Leader:   ' + str(advMsHighestScore) + ' - ' + str(advMsHighestScorePlayer))
        unscrambleLBLabel = leaderboardMenu.add.label(
                'Unscramble Easy Leader:    ' + str(unscrambleHighestScore) + ' - ' + str(unscrambleHighestScorePlayer))
        advUnscrambleLBLabel = leaderboardMenu.add.label(
                'Unscramble Adv. Leader:    ' + str(advUnscrambleHighestScore) + ' - ' + str(advUnscrambleHighestScorePlayer))
        sliLBLabel = leaderboardMenu.add.label(
                'Sliding Game Easy Leader: ' + str(slidingHighestScore) + ' - ' + str(slidingHighestScorePlayer))
        advSliLBLabel = leaderboardMenu.add.label(
                'Sliding Game Adv. Leader: ' + str(advSlidingHighestScore) + ' - ' + str(advSlidingHighestScorePlayer))
        
        leaderboardMenu.add.button('Back', pygame_menu.events.BACK)

        ### --> Main Menu Buttons <--- ###
        main_menu.add.button('Game Selection', gameMenu)
        main_menu.add.button('Account', accountInfoMenu)
        main_menu.add.button('Leaderboards', leaderboardMenu)
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

            # If NOT enabled, enable it
            # If enabled, draw to SCREEN
            if current_menu.is_enabled() == False:
                current_menu.enable()
            if current_menu.is_enabled() == True:
                current_menu.draw(SCREEN)

            # If accountStatsMenu is called,
            # Refresh the stats for the user that logged in
            if accountStatsMenu.is_enabled() == True:
                refresh_stats()
            if leaderboardMenu.is_enabled() == True:
                refresh_lb_stats()

            pygame.display.update()

            # At first loop returns
            if test:
                break


if __name__ == "__main__":
    main.main()

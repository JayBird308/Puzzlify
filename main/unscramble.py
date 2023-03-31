
# Author: Chris Aromando - s1171536

import pygame, pygame.locals
import pygame_menu, pygame_menu.font, pygame_menu.themes, pygame_menu.widgets
import pygame_menu.locals, pygame_menu.widgets.core.selection, pygame_menu.baseimage
import random, constants

# Define constants
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
POINTS = 0
LIST_TITLE = ''
LIST_SELECTED = []
LAST_LIST = []
FIRST_RUN = 0
HINT_VALUE = 0
HINT_COUNTER = 5
main_menu = constants.main_menu
main_menu.disable()
DIFFICULTY = constants.DIFFICULTY

def random_small_list(difficulty_value):
    global LIST_SELECTED, LIST_TITLE, LAST_LIST, FIRST_RUN

    if (difficulty_value == 0):
        list_titles = ['animals', 'fruits', 'colors', 'countries', 'drinks', 'planets', 'sports', 'vehicles', 'flowers', 'jobs']

        animals = ['lion', 'tiger', 'leopard', 'gazelle', 'monkey']
        fruits = ['apple', 'pear', 'peach', 'kiwi', 'mango']
        colors = ['red', 'blue', 'green', 'yellow', 'pink']
        countries = ['italy', 'japan', 'brazil', 'india', 'china']
        drinks = ['coffee', 'tea', 'juice', 'soda', 'water']
        planets = ['venus', 'mars', 'jupiter', 'neptune', 'saturn']
        sports = ['soccer', 'tennis', 'boxing', 'golf', 'hockey']
        vehicles = ['car', 'truck', 'bus', 'bike', 'boat']
        flowers = ['tulip', 'rose', 'daisy', 'lily', 'lotus']
        jobs = ['doctor', 'teacher', 'engineer', 'chef', 'writer']

        while LAST_LIST == LIST_SELECTED or FIRST_RUN == 0:
            if FIRST_RUN == 0:
                LIST_TITLE = random.choice(list_titles)
                if LIST_TITLE == 'animals':
                    LIST_SELECTED = animals
                elif LIST_TITLE == 'fruits':
                    LIST_SELECTED = fruits
                elif LIST_TITLE == 'colors':
                    LIST_SELECTED = colors
                elif LIST_TITLE == 'countries':
                    LIST_SELECTED = countries
                elif LIST_TITLE == 'drinks':
                    LIST_SELECTED = drinks
                elif LIST_TITLE == 'planets':
                    LIST_SELECTED = planets
                elif LIST_TITLE == 'sports':
                    LIST_SELECTED = sports
                elif LIST_TITLE == 'vehicles':
                    LIST_SELECTED = vehicles
                elif LIST_TITLE == 'flowers':
                    LIST_SELECTED = flowers
                elif LIST_TITLE == 'jobs':
                    LIST_SELECTED = jobs
                else:
                    print ('Error: list_titles is not defined')
                break

            LIST_TITLE = random.choice(list_titles)

            if LIST_TITLE == 'animals':
                LIST_SELECTED = animals
            elif LIST_TITLE == 'fruits':
                LIST_SELECTED = fruits
            elif LIST_TITLE == 'colors':
                LIST_SELECTED = colors
            elif LIST_TITLE == 'countries':
                LIST_SELECTED = countries
            elif LIST_TITLE == 'drinks':
                LIST_SELECTED = drinks
            elif LIST_TITLE == 'planets':
                LIST_SELECTED = planets
            elif LIST_TITLE == 'sports':
                LIST_SELECTED = sports
            elif LIST_TITLE == 'vehicles':
                LIST_SELECTED = vehicles
            elif LIST_TITLE == 'flowers':
                LIST_SELECTED = flowers
            elif LIST_TITLE == 'jobs':
                LIST_SELECTED = jobs
            else:
                print ('Error: list_titles is not defined')

        # print(LAST_LIST)
        LAST_LIST = LIST_SELECTED
        # print(LIST_SELECTED)
    else:
        # Difficult Mode!
        list_titles = ['cities', 'desserts', 'languages', 'instruments', ' vegetables',
                       'landmarks', 'art styles', 'oceans', 'dog breeds', 'cat breeds']

        cities = ['new york', 'chicago', 'tokyo', 'sydney', 'paris']
        desserts = ['pastries', 'ice cream', 'brownies', 'cheesecake', 'cupcakes']
        languages = ['english', 'spanish', 'french', 'german', 'chinese']
        instruments = ['guitar', 'piano', 'violin', 'drums', 'trumpet']
        vegetables = ['carrots', 'broccoli', 'zucchini', 'spinach', 'tomatoes']
        landmarks = ['taj mahal', 'eiffel tower', 'great wall of china', 'statue of liberty', 'washington monument']
        art_styles = ['impressionism', 'cubism', 'surrealism', 'realism', 'abstract']
        oceans = ['atlantic', 'pacific', 'indian', 'arctic', 'southern']
        dog_breeds = ['bulldog', 'beagle', 'golden retriever', 'german shepard', 'poodle']
        cat_breeds = ['calico' , 'siamese', 'tabby', 'persian', 'bengal']

        while LAST_LIST == LIST_SELECTED or FIRST_RUN == 0:
            if FIRST_RUN == 0:
                LIST_TITLE = random.choice(list_titles)
                if LIST_TITLE == 'cities':
                    LIST_SELECTED = cities
                elif LIST_TITLE == 'desserts':
                    LIST_SELECTED = desserts
                elif LIST_TITLE == 'languages':
                    LIST_SELECTED = languages
                elif LIST_TITLE == 'instruments':
                    LIST_SELECTED = instruments
                elif LIST_TITLE == 'vegetables':
                    LIST_SELECTED = vegetables
                elif LIST_TITLE == 'landmarks':
                    LIST_SELECTED = landmarks
                elif LIST_TITLE == 'art styles':
                    LIST_SELECTED = art_styles
                elif LIST_TITLE == 'oceans':
                    LIST_SELECTED = oceans
                elif LIST_TITLE == 'dog breeds':
                    LIST_SELECTED = dog_breeds
                elif LIST_TITLE == 'cat breeds':
                    LIST_SELECTED = cat_breeds
                else:
                    print ('Error: list_titles is not defined')
                break

            LIST_TITLE = random.choice(list_titles)

            if LIST_TITLE == 'cities':
                LIST_SELECTED = cities
            elif LIST_TITLE == 'desserts':
                LIST_SELECTED = desserts
            elif LIST_TITLE == 'languages':
                LIST_SELECTED = languages
            elif LIST_TITLE == 'instruments':
                LIST_SELECTED = instruments
            elif LIST_TITLE == 'vegetables':
                LIST_SELECTED = vegetables
            elif LIST_TITLE == 'landmarks':
                LIST_SELECTED = landmarks
            elif LIST_TITLE == 'art styles':
                LIST_SELECTED = art_styles
            elif LIST_TITLE == 'oceans':
                LIST_SELECTED = oceans
            elif LIST_TITLE == 'dog breeds':
                LIST_SELECTED = dog_breeds
            elif LIST_TITLE == 'cat breeds':
                LIST_SELECTED = cat_breeds
            else:
                print ('Error: list_titles is not defined')

        # print(LAST_LIST)
        LAST_LIST = LIST_SELECTED
        # print(LIST_SELECTED)


# Main play method to drive the program
def play():
    global SCREEN_WIDTH, SCREEN_HEIGHT, POINTS, main_menu
    global LIST_TITLE, LIST_SELECTED, HINT_VALUE, HINT_COUNTER, DIFFICULTY
    POINTS = 0
    HINT_VALUE = 0
    HINT_COUNTER = 5

    # Initialize Pygame
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("")
    FPSCLOCK = pygame.time.Clock()

    # Create a menu
    menu = pygame_menu.Menu('Word Unscramble', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_SOLARIZED)
    menu.set_attribute('widget_selection_effect', pygame_menu.widgets.RightArrowSelection)

    # ensure menu is reset and clear
    menu.clear()

    DIFFICULTY = constants.DIFFICULTY
    # print(f'Generating game... Difficulty: {DIFFICULTY}')
    # Generate and set the list
    random_small_list(DIFFICULTY)

    # Lists and Dictionary
    words = LIST_SELECTED
    words_dict = {}
    scrambled_words_widgets = [0,1,2,3,4]

    for word in words:
        retrieved_word = list(word)                 # Retrieves each word by its letters as a list ['c', 'a', 'r']
        regular_spelling = "".join(retrieved_word)

        random.shuffle(retrieved_word)      # Shuffles the list of letters of the word
        scrambled = "".join(retrieved_word) # Join the shuffled letters into a string

        # print(regular_spelling)
        # print(scrambled)

        # If the scrambled word was the same as it was,
        # Attempt to shuffle the letters again
        if scrambled == regular_spelling:
            
            random.shuffle(retrieved_word)
            scrambled = "".join(retrieved_word)
            
        words_dict[word] = scrambled    # Add the scrambled word as a key value pair to a dictionary

    # Points Label
    diff_label = ''
    if DIFFICULTY == 0:
        diff_label = 'Easy'
    elif DIFFICULTY == 1:
        diff_label = 'Advanced'
    points = menu.add.label(f'Difficulty: {diff_label} | Points: {POINTS}')

    def hint_button_action():
        global HINT_VALUE, HINT_COUNTER, POINTS

        name_list = list(words_dict.keys())
        scrambled_list = list(words_dict.values())

        choice = random.choice(scrambled_list)

        loop = True
        while loop:
            for widget in menu.get_widgets():
                print(f'Checking for {choice}')
                index = scrambled_list.index(choice)
                name = name_list[index]

                if widget.get_title() == name and widget.get_font_color_status(check_selection=True) == (220, 30, 30, 255) or widget.get_font_color_status(check_selection=True) == (0, 120, 30, 255):
                    # print('PREVIOUSLY: ', name, ', ', choice)
                    choice = random.choice(scrambled_list)
                    index = scrambled_list.index(choice)
                    name = name_list[index]
                    # print('Reshuffled to: ', name, ', ', choice)

                elif choice == widget.get_title() and widget.get_font_color_status(check_selection=True) != (220, 30, 30, 255):
                    widget.set_title(name)
                    widget.update_font({'color': (220, 30, 30)})
                    POINTS = POINTS - 50
                    points.set_title('Points:' + str(POINTS))
                    menu.render()
                    HINT_COUNTER = HINT_COUNTER - 1
                    HINT_VALUE = 0
                    use_hint.set_title(f'Reveal a Word (-50 pts) {HINT_COUNTER}')
                    loop = False
                    print('CHANGED LABEL ON THE MENU: ', choice)
                    break
                else:
                    print(f'Skipping this widget: {widget.get_title()}')

    use_hint = menu.add.button(title=f'Reveal a Word (-50 pts) {HINT_COUNTER}', action=hint_button_action, button_id='hint_id')
    use_hint.set_border(2, (25, 25, 25), position=(pygame_menu.locals.POSITION_NORTH, pygame_menu.locals.POSITION_SOUTH,
                                                    pygame_menu.locals.POSITION_EAST, pygame_menu.locals.POSITION_WEST))

    # add the 5 hidden words to the screen
    instructions = menu.add.label('Correct -> +100 pts! Wrong -> -20 pts!')
    instructions1 = menu.add.label(f'Unscramble these words ({LIST_TITLE}): ')
    instructions1.set_border(2, (25, 25, 25), position=pygame_menu.locals.POSITION_SOUTH)

    num = 0
    for scrambled in words_dict:
        # add scrambled word values
        widget = menu.add.label(words_dict[scrambled])
        # add the widgets to a scrambled_words_widgets list
        scrambled_words_widgets[num] = widget
        num = num + 1

    # functions to check guess
    def check_guess(value):
        global POINTS

        widgets = menu.get_widgets()
        answer = False
        for name, scrambled in words_dict.items():
            if name == value:
                
                # Used for debug
                print(f"Correct! {value} matches with {name}")

                # If the guessed word was correct,
                # Change to correct spelling & GREEN
                for widget in widgets:
                    # Check if guessed already for loopholes
                    if widget.get_font_color_status(check_selection=True) == (0, 120, 30, 255) and widget.get_title() == name:
                        print("BREAKING OUT! ALREADY GUESSED")
                        break
                    elif isinstance(widget, pygame_menu.widgets.Label) and scrambled == widget.get_title():
                        widget.set_title(name)
                        widget.update_font({'color': (0, 120, 30)})

                        # Add the points and update the Points label
                        POINTS = POINTS + 100
                        print(f"Points: {POINTS}")
                        points.set_title('Points:' + str(POINTS))
                    input.set_value('')
                    menu.select_widget(input)
                    menu.render()
                    answer = True
                break

        for name, scrambled in words_dict.items():
            if name != value and answer != True:
                # Used for debug
                # print(f"Wrong! {value} + Should be {name}")
                POINTS = POINTS - 20
                print(f"Points: {POINTS}")
                points.set_title('Points:' + str(POINTS))
                input.set_value('')
                menu.select_widget(input)
                menu.render()
                break

    # --- ADD INPUT BOX AND BUTTONS ---
    input = menu.add.text_input(
        'Enter your guess: ', 
        default='',
        input_type=pygame_menu.locals.INPUT_TEXT,
        maxchar=20,
        textinput_id='input_id'
    )
    input.set_onreturn(lambda value='': check_guess(value))
    input.set_border(4, (50, 50, 50), position=(pygame_menu.locals.POSITION_NORTH, pygame_menu.locals.POSITION_SOUTH))

    # Add a Back button
    menu.add.label('To go back to game selection, hit ESC.', label_id='back_id')

    # Add a Quit button
    menu.add.button('Exit (Closes Application)', pygame_menu.events.EXIT)  

    def check_end_game():
        global FIRST_RUN
        FIRST_RUN += 1

        guessed_correct = 0
        for name, scrambled in words_dict.items():
            for widget in menu.get_widgets():
                if widget.get_title() == name:
                    guessed_correct += 1
        # print("Guessed Correct:" + str(guessed_correct))

        if guessed_correct == 5:
            pygame.time.delay(3000)
            # If all words are used up, then remove them...
            for name, scrambled in words_dict.items():
                for widget in scrambled_words_widgets:
                    if name == widget.get_title():
                        menu.remove_widget(widget)
            menu.remove_widget(instructions)
            menu.remove_widget(instructions1)
            menu.remove_widget(input)
            menu.render()

            # Show a statistics page...
            # Show Total Points & How many Reveals used.
            hint_widget = menu.get_widget('hint_id')
            hint_widget.hide()
            hint_num = 5 - HINT_COUNTER
            menu.add.label(title=('You completed the game with ' + str(hint_num) + ' reveals used!'))

            # Show Congratulations for Completion
            menu.add.label('Congratulation! You\'ve completed the game!', 'congrats_id')
            widget = menu.get_widget('congrats_id')
            widget.update_font({'color': (0, 120, 30), 'size': 32})

            # Add a Replay button & Focus
            menu.add.button('Play Again', play, button_id = 'play_again')
            menu.select_widget('play_again')
            menu.render()

    menu.select_widget('input_id')

    while True:
        FPSCLOCK.tick(15)

        check_end_game()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_ESCAPE:
                            main_menu.enable()
                            return
        menu.update(events)

        # Draw the menu on the surface
        menu.draw(surface)

        # Update the display
        pygame.display.flip()

# play()
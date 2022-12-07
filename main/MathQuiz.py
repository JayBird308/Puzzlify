# @author: Chris
import pygame, pygame_menu
import random, label
import button, constants
from typing import Tuple, Any, Optional, List

' Global variables '
global USER32, WIDTH, HEIGHT, SCREEN, FPS
USER32 = constants.USER32
WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT
SCREEN = constants.SCREEN
FPS = constants.FPS

global clock, main_menu
clock = constants.clock
main_menu = constants.main_menu

center_w = WIDTH/2
center_h = HEIGHT/2

questionsTotal = 3
wrong = 0
correct = 0

# Choices and Solution
global choice_num, num1, num2, sol, array, btn1, btn2
num1 = 0
num2 = 0
sol = 0

btn1 = False
btn2 = False

# create array of choices & shuffle
array = [num1, num2]

class quiz():

    def set_btn1():
        global btn1
        btn1 = True
        quiz.check_choice(array[0])
        print("Check " + array[0].__str__())
        return btn1

    def set_btn2():
        global btn2
        btn2 = True
        quiz.check_choice(array[1])
        print("Check " + array[1].__str__())
        return btn2

    def play_function(font: 'pygame.font.Font', test: bool = False) -> None:
        global main_menu, clock, choice_num, num1, num2, array, btn1, btn2

        # Get initial values
        question = quiz.generate_question()
        array[0] = quiz.gen_rand_num()
        array[1] = quiz.get_solution()
        random.shuffle(array)
        print("Num1: " + num1.__str__())
        print("Num2: " + num2.__str__())
        bg_color = (0, 120, 120)

        # Reset main menu and disable
        # You also can set another menu, like a 'pause menu', or just use the same
        # main_menu as the menu that will check all your input.
        main_menu.disable()
        main_menu.full_reset()

        def regen():
            pygame.display.flip()
            pygame.time.delay(1250)
            quiz.play_function(
                font=pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30),
                test=False)

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
                            if (b.rect.collidepoint(pos)):
                                b.call_back()
                                regen()
                                return

            # Pass events
            if main_menu.is_enabled():
                main_menu.update(events)

            # Continue playing
            SCREEN.fill(bg_color)

            # Hint Label - To Exit Game to Main Menu
            hint_l = label.Label(
                SCREEN,
                "Hint : To go back to MAIN MENU, Hit the (ESC) key.",
                center_w - 200,
                center_h - 275,
                size=20
            )

            # Math Question
            question_l = label.Label(
                screen=SCREEN,
                text=question,
                x=center_w - 100,
                y=center_h - 200,
                size=48
            )

            # Button 1 - num1
            button_num1 = button.button(
                position=(center_w, center_h), 
                size=(125, 60), 
                clr=(220, 220, 220), 
                cngclr=(50, 130, 255), 
                func=quiz.set_btn1, 
                text=array[0].__str__()
            )

            # Button 2 - num2
            button_num2 = button.button(
                (center_w, center_h+100), 
                (125, 60), 
                (220, 220, 220), 
                (50, 130, 255), 
                func=quiz.set_btn2, 
                text=array[1].__str__()
            )

            # Draw labels and buttons
            label.Label.draw(question_l)
            label.Label.draw(hint_l)
            button_list = [button_num1, button_num2]
            for b in button_list:
                b.draw(SCREEN)


            # update the display to show widgets
            pygame.display.flip()

            # If test returns
            if test and frame == 2:
                break

    def check_choice(num):

        if (num != sol):
            wrong_l = label.Label(
                screen=SCREEN,
                text="Incorrect!!",
                x=center_w - 100,
                y=center_h+220,
                size=60,
                color="red"
            )
            label.Label.draw(wrong_l)
        elif (num == sol):
            correct_l = label.Label(
                screen=SCREEN,
                text="Correct!!",
                x=center_w - 100,
                y=center_h+220,
                size=60,
                color="green"
            )
            label.Label.draw(correct_l)

    def gen_rand_num():
        num = random.randint(0, 10)
        return num

    def get_num1():
        global num1
        return num1

    def get_num2():
        global num2
        return num2

    def get_solution():
        global num1, num2, sol
        sol = num1 + num2
        return sol

    def generate_question():
        global num1, num2, sol

        num1 = quiz.gen_rand_num()
        num2 = quiz.gen_rand_num()
        sol = num1 + num2

        question = (num1.__str__() + ' + ' + num2.__str__() + ' = ?')
        
        print('Math Question: ', end='')
        print(question)
        return question
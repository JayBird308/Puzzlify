# @author: Chris
import pygame, pygame_menu
import random, label
import button, constants

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

questionCounter = 1
questionsTotal = 4
wrong = 0
correct = 0

# Choices and Solution
global choice_num, num1, num2, sol, array, btn1, btn2
num1 = 0
num2 = 0
num3 = 0
num4 = 0
sol = 0

# create array of choices & shuffle
array = [num1, num2, num3, num4]

class quiz():

    def set_btn1():
        quiz.check_choice(array[0])

    def set_btn2():
        quiz.check_choice(array[1])

    def set_btn3():
        quiz.check_choice(array[2])
        
    def set_btn4():
        quiz.check_choice(array[3])
        
    def reset_values():
        global questionCounter, wrong, correct
        questionCounter = 1
        wrong = 0
        correct = 0

    def show_stats():
        global main_menu, clock, questionsTotal, wrong, correct

        main_menu.disable()
        main_menu.full_reset()

        frame = 0
        while True:
            # noinspection PyUnresolvedReferences
            clock.tick(60)
            frame += 1

            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        main_menu.enable()
                        return
                    if e.key == pygame.K_0:
                        exit()
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        pos = pygame.mouse.get_pos()
                        if (back.rect.collidepoint(pos)):
                            back.call_back()
                            return

            # Pass events
            if main_menu.is_enabled():
                main_menu.update(events)

            SCREEN.fill((0, 160, 160))

            # Title
            title_l = label.Label(
                SCREEN,
                "Statistics:",
                center_w - 150,
                center_h - 300,
                size=60
            )

            # Incorrect
            wrong_l = label.Label(
                screen=SCREEN,
                text="Incorrect: " + wrong.__str__(),
                x=center_w - 150,
                y=center_h - 200,
                size=48
            )

            # Correct
            correct_l = label.Label(
                screen=SCREEN,
                text="Correct: " + correct.__str__(),
                x=center_w - 150,
                y=center_h - 100,
                size=48
            )

            # Counter
            total_l = label.Label(
                screen=SCREEN,
                text="Total: " + (questionsTotal-1).__str__(),
                x=center_w - 150,
                y=center_h,
                size=48
            )

            # Back to Menu
            back = button.button(
                (center_w, center_h+200), 
                (125, 60), 
                (220, 220, 220), 
                (50, 130, 255), 
                func=main_menu.enable, 
                text="Back to Menu"
            )

            # Draw labels and buttons
            label.Label.draw(title_l)
            label.Label.draw(wrong_l)
            label.Label.draw(correct_l)
            label.Label.draw(total_l)
            back.draw(SCREEN)

            # update the display to show widgets
            pygame.display.flip()

    def check_choice(num):
        global wrong, correct, questionCounter
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
            wrong = wrong + 1
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
            correct = correct + 1
        pygame.display.flip()
        questionCounter = questionCounter + 1

    def play_function(font: 'pygame.font.Font', test: bool = False) -> None:
        global main_menu, clock, choice_num, num1, num2, array, questionCounter
        global btn1, btn2, btn3, btn4, questionsTotal, wrong, correct

        # Get initial values
        question = quiz.generate_question()
        
        array[0] = quiz.gen_rand_num()
        array[1] = quiz.gen_rand_num()
        array[2] = quiz.gen_rand_num()
        array[3] = quiz.get_solution()

        # while loops to ensure unique values
        while True:
            if array[0] == array[1]:
                array[0] = quiz.gen_rand_num()
            elif array[0] == array[2]:
                array[0] = quiz.gen_rand_num()  
            elif array[0] == array[3]:
                array[0] = quiz.gen_rand_num()
            elif array[0] != array[1] and array[0] != array[2] and array[0] != array[3]:
                break
            
        while True:
            if array[1] == array[0]:
                array[1] = quiz.gen_rand_num()
            elif array[1] == array[2]:
                array[1] = quiz.gen_rand_num()
            elif array[1] == array[3]:
                array[1] = quiz.gen_rand_num()
            if array[1] != array[0] and array[1] and array[2] and array[1] != array[3]:
                break

        while True:
            if array[2] == array[0]:
                array[2] = quiz.gen_rand_num()
            elif array[2] == array[1]:
                array[2] = quiz.gen_rand_num()
            elif array[2] == array[3]:
                array[2] = quiz.gen_rand_num()
            if array[2] != array[0] and array[2] != array[1] and array[2] != array[3]:
                break

        # shuffle options
        for x in range(50):
            random.shuffle(array)

        main_menu.disable()
        main_menu.full_reset()

        # regenerate a question by calling overall function
        def regen():
            pygame.time.delay(1500)
            quiz.play_function(
                font=pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30),
                test=False)

        # while 1 < 4 : counter should iterate 3 times before resetting on exit
        while questionCounter < questionsTotal:
            # noinspection PyUnresolvedReferences
            clock.tick(15)

            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        main_menu.enable()
                        return
                    if e.key == pygame.K_0:
                        exit()
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        pos = pygame.mouse.get_pos()
                        for b in button_list:
                            if (b.rect.collidepoint(pos)):
                                b.call_back()
                                regen()
                                # resets counter on exit
                                if questionCounter == questionsTotal:
                                    quiz.show_stats()
                                    quiz.reset_values()
                                return

            # Pass events
            if main_menu.is_enabled():
                main_menu.update(events)

            # Continue playing
            SCREEN.fill((0, 120, 120))

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
                position=(center_w - 100, center_h), 
                size=(125, 60), 
                clr=(220, 220, 220), 
                cngclr=(50, 130, 255), 
                func=quiz.set_btn1, 
                text=array[0].__str__()
            )

            # Button 2 - num2
            button_num2 = button.button(
                (center_w - 100, center_h+100), 
                (125, 60), 
                (220, 220, 220), 
                (50, 130, 255), 
                func=quiz.set_btn2, 
                text=array[1].__str__()
            )

            # Button 3 - num3
            button_num3 = button.button(
                position=(center_w + 100, center_h), 
                size=(125, 60), 
                clr=(220, 220, 220), 
                cngclr=(50, 130, 255), 
                func=quiz.set_btn3, 
                text=array[2].__str__()
            )

            # Button 4 - num4
            button_num4 = button.button(
                (center_w + 100, center_h+100), 
                (125, 60), 
                (220, 220, 220), 
                (50, 130, 255), 
                func=quiz.set_btn4, 
                text=array[3].__str__()
            )

            # Draw labels and buttons
            label.Label.draw(question_l)
            label.Label.draw(hint_l)
            button_list = [button_num1, button_num2, button_num3, button_num4]
            for b in button_list:
                b.draw(SCREEN)

            # update the display to show widgets
            pygame.display.flip()

            # If test returns
            if test and frame == 2:
                break

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
        print("Solution: " + sol.__str__())
        return question
import random
# @author: Chris
' Global variables '
questionsTotal = 3
wrong = 0
correct = 0

num1 = 0
num2 = 0
sol = 0


class quiz():
    # def __init__(self):
    #     global questionsTotal
    #     global wrong
    #     global correct

    #     loopNum = 0
    #     while loopNum < questionsTotal:
    #         self.generate_question()
    #         loopNum = loopNum + 1
    #     print('-- Final Statistics --')
    #     print('Number of Questions: ' + questionsTotal.__str__())
    #     print('Wrong: ' + wrong.__str__())
    #     print('Correct: ' + correct.__str__())
    #     print('---------------')

    def gen_num1():
        global num1
        num1 = random.randint(0, 10)
        return num1

    def get_num1():
        global num1
        return num1

    def get_num2():
        global num2
        return num2

    def get_solution():
        global num1
        global num2
        global sol
        sol = num1 + num2
        return sol

    def generate_question():
        global num1
        global num2
        global sol

        num1 = quiz.gen_num1()
        num2 = random.randint(0, 10)
        sol = num1 + num2
        question = (num1.__str__() + ' + ' + num2.__str__() + ' = ?')

        print('Math Question: ', end='')
        print(question)
        return question
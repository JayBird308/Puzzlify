import random
# @author: Chris
' Global variables '
questionsTotal = 3
wrong = 0
correct = 0
 
'''
Class quiz() : __init__() , generate_question() , user_answer()
'''
class quiz():
 
    '''
    __init__ function :
    -----------------------------------------------
    - has access to read global variables.
    - runs a loop of how many questions to ask
    - once loop ends, it prints statistics
    '''
    def __init__(self):
        global questionsTotal
        global wrong
        global correct

        loopNum = 0
        while loopNum < questionsTotal:
            self.generate_question()
            loopNum = loopNum + 1
        print('-- Final Statistics --')
        print('Number of Questions: ' + questionsTotal.__str__())
        print('Wrong: ' + wrong.__str__())
        print('Correct: ' + correct.__str__())
        print('---------------')
        exit(0)
   
    '''
    generate_question() function :
    ------------------------------
    - has access to global variables for modifications
    - gets two random numbers for a simple addition problem
    - grabs an input from the user...
        - checks the input by processing it through if else statements
    '''
    def generate_question(self):
        global wrong
        global correct
        print('Math Question: ', end='')
       
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        s = num1 + num2
       
        print(num1.__str__() + ' + ' + num2.__str__() + ' = ?')
        ans = self.user_answer()
       
        if (ans.isdigit()):
            ans = int(ans)
            if (ans == s):
                correct = correct + 1
                print('You are correct!')
            else:
                wrong = wrong + 1
                print('Your answer is incorrect...')
        else:
            wrong = wrong + 1
            print('Your answer is not even a number!')
        print('---------------')
   
    '''
    user_answer() function :
    ------------------------
    simply grabs an input from the user...
    - returns the input
    '''
    def user_answer(self):
        ans = input()
        return ans
       
quiz()
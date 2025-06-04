class QuizBrain():
    def __init__(self, ql):
        self.qn = 0
        self.ql = ql
        self.score = 0
    
    def nq(self):
        question = self.ql[self.qn]
        self.qn += 1
        ua = input(f'Q{self.qn}: {question.text}, True/False: ')
        self.ca(ua, question.answer)

    def kaq(self):
        if self.qn < len(self.ql):
            return True
        else:  
            return False
    
    def ca(self, users_answer, real_answer):
        if users_answer.lower() == real_answer.lower():
            print('You got it right')
            self.score += 1
            print(f'Your current score is: {self.score}/{self.qn}')
            print('\n\n\n\n\n\n\n\n\n')
        else:
            print("That is wrong")
            print(f'The actual answer was: {real_answer}')
            print(f'Your current score is: {self.score}/{self.qn}')
            print('\n\n\n\n\n\n\n\n\n')
from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.user_score = 0
        self.other_score = 0
        self.goto(-50, 300)
        self.write(self.user_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(50, 300)
        self.write(self.other_score, align='center', font=('Courier', 80, 'normal'))
    
    def add_to_user1(self):
        self.clear()
        self.user_score += 1
        self.goto(-100, 300)
        self.write(self.user_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(50, 300)
        self.write(self.other_score, align='center', font=('Courier', 80, 'normal'))

    def add_to_user2(self):
        self.clear()
        self.other_score += 1
        self.goto(-100, 300)
        self.write(self.user_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(50, 300)
        self.write(self.other_score, align='center', font=('Courier', 80, 'normal'))    
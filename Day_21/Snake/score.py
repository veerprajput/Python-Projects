from turtle import Screen, Turtle
import time
from food import Food

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.write(f'Score: {self.score}', font=('Courier', 24, 'normal'))
        
    
    # def reset(self):
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #     self.score = 0
    #     self.write_score()
    def game_over(self, score):
        self.goto((-400, 0))
        self.write(f'Game Over!!! Your score was {score}', font=('Bold', 40))
    
    def write_score(self, coordinates, text):
        self.goto(coordinates)
        self.pendown()
        self.screen.update()
        self.clear()
        self.write(f'{text} {self.score}' , font=('Courier', 24, 'normal'))
        self.score += 1
        self.penup()
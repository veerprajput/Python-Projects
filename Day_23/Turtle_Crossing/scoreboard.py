from turtle import Turtle
import random
import time

FONT = ('Courier', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-320, 320)
        self.write(f'Level: {self.level}', font=('Courier', 10, 'normal'))  
    
    def next_level(self):
        self.hideturtle()
        self.penup()
        self.clear()
        self.goto(-320, 320)
        self.level += 1
        self.color('Black')
        self.write(f'Level: {self.level}', font=('Courier', 10, 'normal'))
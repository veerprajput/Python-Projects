from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

    def refresh(self, screen):
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('orange')
        self.speed('fastest')
        random_x = random.randint(-450, 450)
        random_y = random.randint(-220, 220)
        self.goto(random_x, random_y)
        screen.setup(width=1000, height=700)
        screen.bgcolor('black')
        screen.title('Snake Game')
        screen.tracer(0)


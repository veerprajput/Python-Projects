from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.x = 10
        self.y = 10
        self.time = 0.1
    
    def move(self):
        self.penup()
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)
    
    def move_x_negative(self):
        self.penup()
        x = self.xcor() - self.x
        y = self.ycor() - self.y
        self.goto(x, y)
    
    def bounce_ball_y(self):
        self.speed(0)
        self.y *= -1
    
    def bounce_ball_x(self):
        self.speed(0)
        self.x *= -1
        self.time * 0.8
    
    def reset(self):
        self.color('white')
        self.shape('circle')
        self.x = 10
        self.y = 10
        self.penup()
        self.goto(0, 0)
        self.bounce_ball_x()
        self.time *= 1.1
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('skyblue')
        self.shape('circle')
        self.speed(0)
        self.penup()
        self.x_move = 20
        self.y_move = 20
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.y_move *= -1
    
    def bouncex(self):
        self.x_move *= -1
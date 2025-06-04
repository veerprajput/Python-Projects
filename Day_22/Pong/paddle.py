from turtle import Turtle, Screen
class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.speed(0)
        self.color('white')
        self.penup()
        self.goto(coordinates)
        self.shape('square')
        self.right(90)
        self.shapesize(None, 5)

    def up(self):
        y = self.ycor()
        self.goto(self.xcor(), y + 100)

    def down(self):
        y = self.ycor()
        self.goto(self.xcor(), y - 100)
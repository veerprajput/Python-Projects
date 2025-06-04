from turtle import Turtle

STARTING_POSITION = (0, -330)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 335

class Player(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape('turtle')
        self.screen = screen
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
    
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def move_backward(self):
        self.backward(MOVE_DISTANCE - 5)
    
    def check(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.color('black')
            self.goto(STARTING_POSITION)
            self.screen.tracer(0)
            return True
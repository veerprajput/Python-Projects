from turtle import Screen, Turtle
import time
from food import Food

food = Food()


class Snake():
    global food
    def __init__(self, position, parts, screen1):
        self.positions = position
        self.parts1 = parts
        self.screen = screen1
        self.head = 0

    def add_segment(self, position):
        new_part = Turtle('square')
        new_part.goto(position)
        new_part.penup()
        self.parts1.append(new_part)
        new_part.goto(position)
        new_part.color('white')
    
    def first_add_segment(self, position):
        new_part = Turtle('square')
        new_part.goto(position)
        new_part.penup()
        self.parts1.append(new_part)
        new_part.goto(position)
        new_part.color('cyan')

    def extend(self):
        self.add_segment(self.parts1[-1].position())
    
    def create(self):
        self.screen.tracer(0)
        for position in self.positions:
            if position == (0, 0):
                self.first_add_segment(position)
            else:
                self.add_segment(position)
    
    def slower(self):
        for part in self.parts1:
            part.speed('fastest')
            self.head = self.parts1[0]
    
    
    ###Remove parentheses on heading function to go back on itself as a cheat.
    
    def right(self):
        for part in self.parts1:
            if part.heading() != 180:
                part.setheading(0)

    def up(self):
        for part in self.parts1:
            if part.heading() != 270:
                part.setheading(90)
    
    def down(self):
        for part in self.parts1:
            if part.heading() != 90:
                part.setheading(270)

    def left(self):
        for part in self.parts1:
            if part.heading() != 0:
                part.setheading(180)
    
    def move(self):
        for sn in range(len(self.parts1) - 1, 0, -1):
            newx = self.parts1[sn - 1].xcor()
            newy = self.parts1[sn -1].ycor()
            self.parts1[sn].goto(newx, newy)
            self.screen.onkeypress(key='Right', fun=self.right)
            self.screen.onkeypress(key='Left', fun=self.left)
            self.screen.onkeypress(key='Up', fun=self.up)
            self.screen.onkeypress(key='Down', fun=self.down)
        self.parts1[0].forward(20)




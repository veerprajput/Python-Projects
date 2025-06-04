from turtle import Turtle, Screen

jack = Turtle()
screen = Screen()

jack.speed('fastest')

def forward():
    jack.forward(20)

def backward():
    jack.right(180)
    jack.forward(20)

def right():
    jack.right(10)

def left():
    jack.left(10)

def clear():
    jack.home()
    jack.clear()

screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='a', fun=right)
screen.onkey(key='s', fun=backward)
screen.onkey(key='d', fun=left)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
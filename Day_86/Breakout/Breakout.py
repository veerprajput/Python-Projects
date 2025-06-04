from turtle import Screen, Turtle
from ball import Ball
from hit import Hit
import time
import winsound

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Breakout')
screen.tracer(0)

paddle =  Turtle()
paddle.shape('square')
paddle.color('blue')
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.speed(0)
paddle.goto(0, -200)
ball = Ball()
hit = Hit(ball)
hit.add_hit()

def left():
    paddle.goto(paddle.xcor() - 100, paddle.ycor())

def right():
    paddle.goto(paddle.xcor() + 100, paddle.ycor())

screen.listen()
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    hit.show()
    hit.check_collision()
    hit.check_for_win()
    
    if ball.ycor() > 275:
        ball.bounce()
    elif ball.xcor() > 375 or ball.xcor() < -375:
        ball.bouncex()
    if ball.distance(paddle) <= 60 and ball.ycor() < -179:
        ball.bounce()
    elif ball.ycor() < -250:
        galldibad = Turtle()
        galldibad.color('red')
        galldibad.penup()
        galldibad.goto(-200, 0)
        galldibad.hideturtle()
        galldibad.pendown()
        galldibad.write('GAME OVER', font=('Arial',50))

screen.exitonclick()
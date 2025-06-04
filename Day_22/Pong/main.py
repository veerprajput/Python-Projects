from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.setup(1000, 800)
screen.tracer(0)

paddle = Paddle((450, 0))
computer_paddle = Paddle((-450, 0))
ball = Ball()
score = Score()



screen.listen()
screen.onkeypress(key='Up', fun=paddle.up)
screen.onkeypress(key='Down', fun=paddle.down)
screen.onkeypress(key='q', fun=computer_paddle.up)
screen.onkeypress(key='a', fun=computer_paddle.down)

game_on = True
while game_on:
    time.sleep(ball.time)
    screen.update()
    ball.move()
    if ball.ycor() > 380 or ball.ycor() < -380 :
        ball.bounce_ball_y()
    if ball.xcor() > 425 and ball.distance(paddle) < 50 or ball.xcor() < -425 and ball.distance(computer_paddle) < 50:
        ball.bounce_ball_x()
    if ball.xcor() > 480:
        ball.reset()
        score.add_to_user1()
    if ball.xcor() < -480:
        ball.reset()
        ball.bounce_ball_x()
        score.add_to_user2()

screen.exitonclick()
from turtle import Screen, Turtle
import time
from food import Food
from snake import Snake
from score import Score

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

game_over_writer = Turtle()

snake = Snake([(0,0), (-20, 0), (-40, 0)], [], screen)
food = Food()
score = Score()
# pratik = Snake([(0,-30), (-20, -30), (-40, -30)], [], screen)

snake.create()
# pratik.create()

game_score = 0

snake.slower()
# pratik.slower()
score.write_score((0, 300), 'Score: ')
food.refresh(screen)

screen.listen()

is_moving = True
while is_moving:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    if snake.parts1[0].distance(food) < 20:
        food.refresh(screen)
        snake.extend()
        game_score += 1
        score.write_score((0, 300), 'Score: ')
    if snake.parts1[0].xcor() > 485 or snake.parts1[0].xcor() < -485:
        score.game_over(game_score)
        time.sleep(3)
        exit()
    elif snake.parts1[0].ycor() > 330 or snake.parts1[0].ycor() < -330:
        score.game_over(game_score)
        time.sleep(3)
        exit()
    for segment in snake.parts1[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over(game_score)
            time.sleep(3)
            exit()




screen.exitonclick()
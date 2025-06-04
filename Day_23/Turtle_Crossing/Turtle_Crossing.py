import time
from turtle import Turtle, Screen
from player import Player
from carmanager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=700, height=700)
# screen.bgpic('background.gif')
screen.tracer(0)

player = Player(screen)
carmanager = CarManager(screen)
scoreboard = ScoreBoard()

screen.listen()

distance = 15

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # if player.check() == True:
    #     carmanager.move_cars(player)
    screen.onkey(key='Up', fun=player.move_forward)
    screen.onkey(key='Down', fun=player.move_backward)
    time.sleep(0.09)
    carmanager.create()
    carmanager.move_cars(distance, player)
    if player.check() == True:
        distance += 5
        scoreboard.next_level()
        carmanager.move_cars(distance, player)

screen.exitonclick()
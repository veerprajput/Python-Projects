from turtle import Turtle
import random
import time

COLORS = ['red', 'orange', 'yellow', 'green', 'cyan', 'violet']
CARS = []

class CarManager(Turtle):
    STARTING_MOVE_DISTANCE = 25
    MOVE_INCREMENT = 10
    
    def __init__(self, screen):
        super().__init__()
        self.STARTING_MOVE_DISTANCE = 25
        self.MOVE_INCREMENT = 10
    def create(self):
            car = Turtle()
            car.shape('square')
            car.shapesize(None, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(360, random.randint(-300, 300))
            CARS.append(car)
    
    def check_Y(self, player):
        if player.ycor() >= 335:
            self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT

    
    def move_cars(self, move_distance, player):
        for car in CARS:
            car.backward(move_distance)

            if car.distance(player) < 20:
                car.goto(-250, 0)
                car.write('Game over!', font=('Courier', 64, 'normal'))
                time.sleep(2)
                exit()
                
    
    
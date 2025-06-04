from turtle import Turtle, Screen
import random

jack = Turtle()
tim = Turtle()
tom = Turtle()
timmy = Turtle()
tommy = Turtle()
money = Turtle()
screen = Screen()

turtles = (jack, tim, tom, timmy, tommy, money)
colors = ('red', 'dark orange', 'gold', 'chartreuse', 'cyan', 'medium purple')
positions = (100, 50, 0, -50, -100, -150)

def go_to_start(name, y_position):
    name.goto(-487, y_position)
def penup2(name):
    name.penup()
def change_shape(name):
    name.shape('turtle')
def change_color(name, color):
    name.color(color)

screen.setup(width=1000, height=700)

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

for turtle in range(0, 6):
    penup2(turtles[turtle])
    change_shape(turtles[turtle])
    change_color(turtles[turtle], colors[turtle])
    go_to_start(turtles[turtle], positions[turtle])

for turtle in range(0, 6):
    race_start = True
    
    while race_start:
        for i in turtles:
            for j in turtles:
                if j.xcor() == 480:
                    for k in range(0, 6):
                        pass
                    if user_bet == colors[k]:
                        print('You win!!! Your bet was correct')
                        race_start = False
                        # screen.bye()
                    else:
                        print('Your bet was wrong....')
                        race_start = False
                        # screen.bye()
            if race_start:
                num = random.randint(0, 10)
                i.forward(num)
            else:
                exit()
    break




screen.exitonclick()
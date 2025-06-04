import colorgram.py
from turtle import Turtle, Screen
import random

# choice = int(input('Enter a number of colors to extract between 0 and 34: '))

# colors = colorgram.extract('Spot_painting.jpg', choice)


# rgb = []
# # hsl = []
# # proportion = []

# for color in range(0, choice):
#     rgb_tuple = (colors[color].rgb.r, colors[color].rgb.g, colors[color].rgb.b)
#     rgb.append(rgb_tuple)
#     # hsl_tuple = (colors[color].hsl.h, colors[color].hsl.s, colors[color].hsl.l)
#     # hsl.append(hsl_tuple)
#     # proportion.append(round(colors[color].proportion, 2))

# print(rgb)
# # print(hsl)
# # print(proportion)


jack = Turtle()
jack.shape('turtle')
jack.color('lime')
jack.penup()
jack.hideturtle()
jack.goto(-300, -370)


colorlist = [(139, 164, 183), (26, 116, 172), (238, 213, 64), (202, 140, 166), (222, 158, 82), (121, 71, 96), (24, 135, 63), (137, 22, 37), (70, 31, 37), (182, 176, 32), (185, 76, 41), (224, 171, 197), (55, 36, 34), (30, 169, 182), (230, 87, 39), (107, 191, 135), (11, 108, 66), (46, 171, 89), (183, 95, 110), (38, 37, 43), (188, 183, 209), (157, 208, 214), (151, 214, 172), (237, 172, 154), (126, 116, 156), (79, 55, 54), (12, 102, 105), (200, 210, 35), (65, 58, 79), (35, 37, 36)]



for i in range(3):
    length = len(colorlist)
    for rgb_values in range(0, length):
        colorlist.append(random.choice(colorlist))


screen = Screen()

screen.colormode(255)

jack.speed('fastest')

def main(rgb_tuple):
    # jack.pendown()
    # r = rgb_tuple[0]
    # g = rgb_tuple[1]
    # b = rgb_tuple[2]
    # rgb = r,g,b
    # jack.color(r, g, b)
    jack.dot(20, random.choice(colorlist))
    # jack.penup()
    jack.forward(50)

num = -370

for color in range(0, 225):
    if color % 15 == 0:
        num += 50
        jack.goto(-300, num)
    main(colorlist[color])

screen.exitonclick()
import turtle
from PIL import Image

screen = turtle.Screen()

image = screen.textinput(title='Upload a image', prompt="Upload a image?")
screen.bgpic(image)
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.goto(230, -200)
drawer.showturtle()
screen.addshape('sub_cropped.gif')

drawer.shape('sub_cropped.gif')

screen.mainloop()


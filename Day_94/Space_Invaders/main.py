import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Space Invaders')
screen.setup(1000, 800)
screen.tracer(0)
screen.register_shape('shooting_ship.gif')
screen.register_shape('Bullet.gif')
screen.register_shape('Bullet - Copy.gif')
screen.register_shape('Enemy_1.gif')
screen.register_shape('Enemy_2.gif')
screen.register_shape('Enemy_3.gif')

class Ship(turtle.Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape('shooting_ship.gif')
        self.coordinates = [coordinates[0], coordinates[1]]
        self.goto(x=coordinates[0], y=coordinates[1])
        self.bullets = []

    def left(self):
        x = self.xcor()
        self.coordinates = [x - 30, self.ycor()]
        self.goto(x - 30, self.ycor())

    def right(self):
        x = self.xcor()
        self.coordinates = [x + 30, self.ycor()]
        self.goto(x + 30, self.ycor())
    
    def shoot(self):
        self.bullet = turtle.Turtle()
        self.bullet.shape('Bullet.gif')
        self.bullets.append(self.bullet)
        self.bullet.speed(0)
        self.bullet.goto(x=self.coordinates[0], y=self.coordinates[1] + 50)

class InitiateEnemy(turtle.Turtle):
    def __init__(self, image_name, coordinates):
        super().__init__()
        self.coordinates = [coordinates[0], coordinates[1]]
        self.shape(image_name)
        self.setpos(coordinates)
        self.bullets = []
    
    def move(self):
        value = self.xcor()
        # self.setx(value + 20)
        self.forward(20)
    
    def move2(self):
        value = self.xcor()
        # self.setx(value - 20)
        self.backward(20)
    
    def hide(self):
        self.hideturtle()
    
    def shoot(self):
        self.bullet = turtle.Turtle()
        self.bullet.shape('Bullet - Copy.gif')
        self.bullets.append(self.bullet)
        self.bullet.speed(0)
        self.bullet.goto(x=self.coordinates[0], y=self.coordinates[1] - 50)

screen.update()
ship = Ship(coordinates=[0, -300])
x = -435
y = 300
enemies = []
for q in range(15):
    enemy_1 = InitiateEnemy('Enemy_3.gif', coordinates=[x, y])
    enemies.append(enemy_1)
    x += 60

y = 250
x -= 60
for q in range(15):
    enemy_1 = InitiateEnemy('Enemy_2.gif', coordinates=[x, y])
    enemies.append(enemy_1)
    x -= 60

y = 200
x += 60
for q in range(15):
    enemy_1 = InitiateEnemy('Enemy_1.gif', coordinates=[x, y])
    enemies.append(enemy_1)
    x += 60

screen.listen()
screen.onkeypress(key='Left', fun=ship.left)
screen.onkeypress(key='Right', fun=ship.right)
screen.onkeypress(key='space', fun=ship.shoot)

game_playing = True
direction_of_enemies = 'left'
while game_playing:
    screen.update()
    for bullet in ship.bullets:
        value = bullet.ycor()
        bullet.sety(value + 60)
        for enemy in enemies:
            if enemy.distance(bullet) < 50:
                enemy.hide()
                enemies.remove(enemy)
                ship.bullets.remove(bullet)
                bullet.hideturtle()
                for bullet in enemy.bullets:
                    bullet.hideturtle()
                bullet.hideturtle()
                break       
    if direction_of_enemies == 'left':
        for enemy in enemies:
            enemy.move()
            if random.randint(1, 100) == 99 or random.randint(1, 100) == 12:
                enemy.shoot()
                enemy.shoot()
            if len(enemy.bullets) > 0:
                for bullet in enemy.bullets:
                    bullet.sety(bullet.ycor() - 60)
                    if bullet.distance(ship) < 30:
                        ship.hideturtle()
                        for enemy2 in enemies:
                            enemies.remove(enemy2)
                            enemy.hideturtle()
                            for bullet2 in enemy.bullets:
                                bullet2.hideturtle()
                        writer = turtle.Turtle()
                        writer.color('red')
                        writer.hideturtle()
                        writer.penup()
                        writer.goto(-175, 0)
                        writer.pendown()
                        writer.write('GAME OVER', font = ['Arial', 40, 'normal'])
                        game_playing = False
        screen.update()
        time.sleep(0.1)
        direction_of_enemies = 'right'
    if direction_of_enemies == 'right':
        for enemy in enemies:
            enemy.move2()
            if random.randint(1, 100) == 52 or random.randint(1, 100) == 67:
                enemy.shoot()
                enemy.shoot()
            if len(enemy.bullets) > 0:
                for bullet in enemy.bullets:
                    bullet.sety(bullet.ycor() - 60)
                    if bullet.distance(ship) < 30:
                        ship.hideturtle()
                        for enemy2 in enemies:
                            enemies.remove(enemy)
                            enemy2.hideturtle()
                            for bullet2 in enemy.bullets:
                                bullet2.hideturtle()
                        writer = turtle.Turtle()
                        writer.color('red')
                        writer.hideturtle()
                        writer.penup()
                        writer.goto(-175, 0)
                        writer.pendown()
                        writer.write('GAME OVER', font = ['Arial', 40, 'normal'])
                        game_playing = False
        time.sleep(0.1)
        screen.update()
        direction_of_enemies = 'left'
    time.sleep(0.1)
    
    if len(enemies) == 0:
        writer = turtle.Turtle()
        writer.color('light green')
        writer.hideturtle()
        writer.penup()
        writer.goto(-175, 0)
        writer.pendown()
        writer.write('YOU WIN!!!', font = ['Arial', 40, 'normal'])
        game_playing = False


screen.exitonclick()
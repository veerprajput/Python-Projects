from turtle import Turtle

class Hit(Turtle):
    def __init__(self, ball):
        super().__init__()
        self.parts = []
        self.breakout_ball = ball
        self.positions = [(330, 150, 'light green'), (270, 150, 'light green'), (210, 150, 'light green'), (150, 150, 'light green'),(90, 150, 'light green'), (30, 150, 'light green'), (-30, 150, 'light green'), (-90, 150, 'light green'),(-150, 150, 'light green'), (-210, 150, 'light green'), (-270, 150, 'light green'), (-330, 150, 'light green'),(330, 190, 'yellow'), (270, 190, 'yellow'), (210, 190, 'yellow'), (150, 190, 'yellow'),(90, 190, 'yellow'), (30, 190, 'yellow'), (-30, 190, 'yellow'), (-90, 190, 'yellow'),(-150, 190, 'yellow'), (-210, 190, 'yellow'), (-270, 190, 'yellow'), (-330, 190, 'yellow'),(330, 230, 'orange'), (270, 230, 'orange'), (210, 230, 'orange'), (150, 230, 'orange'),(90, 230, 'orange'), (30, 230, 'orange'), (-30, 230, 'orange'), (-90, 230, 'orange'),(-150, 230, 'orange'), (-210, 230, 'orange'), (-270, 230, 'orange'), (-330, 230, 'orange'),(330, 270, 'red'), (270, 270, 'red'), (210, 270, 'red'), (150, 270, 'red'),(90, 270, 'red'), (30, 270, 'red'), (-30, 270, 'red'), (-90, 270, 'red'),(-150, 270, 'red'), (-210, 270, 'red'), (-270, 270, 'red'), (-330, 270, 'red')]
    
    def add_hit(self):
        for i in self.positions:
            self.paddle =  Turtle()
            self.paddle.hideturtle()
            self.paddle.goto(i[0], i[1])
            self.paddle.color(i[2])
            self.parts.append(self.paddle)
    
    def check_collision(self):
        for paddle in self.parts:
            if paddle.distance(self.breakout_ball) <= 60:
                self.parts.remove(paddle)
                paddle.hideturtle()
                self.breakout_ball.bounce()
    
    def show(self):
        for paddle in self.parts:
            paddle.shape('square')
            paddle.showturtle()
            paddle.shapesize(stretch_wid=1, stretch_len=2)
            paddle.penup()
            paddle.speed(0)
    
    def check_for_win(self):
        if len(self.parts) == 0:
            galldibad = Turtle()
            galldibad.color('light green')
            galldibad.penup()
            galldibad.goto(-200, 0)
            galldibad.hideturtle()
            galldibad.pendown()
            galldibad.write('YOU WIN!!!', font=('Arial',50, 'bold'))
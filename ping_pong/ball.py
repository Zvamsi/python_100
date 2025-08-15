from turtle import Turtle

STRAIGHT_UP=(1,4)
STRAIGHT_DOWN=(1,-4)


direction=STRAIGHT_UP

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

    def move_ball(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def bounce(self):
        self.y_move*=-1

    def pitch(self):
        self.x_move*=-1
        self.move_speed*=0.9

    def miss(self):
        self.setpos(0,0)
        self.move_speed=0.1
        self.pitch()



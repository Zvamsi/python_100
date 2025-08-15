from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.teleport(0,-280)
        self.left(90)

    def move__(self):
        self.forward(MOVE_DISTANCE)

    def is_at_end(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.teleport(0,-280)




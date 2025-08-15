from turtle import Turtle
ALIGNMENT='center'
FONT=("Courier", 12, "bold")

class ScoreBoard(Turtle):

    def __init__(self,score):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
            self.high_score=int(file.read())
        # self.high_score=0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setpos(0, 230)
        self.write_to()

    def write_to(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open('high_score.txt',mode='w') as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.write_to()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def update(self):
        self.score+=1

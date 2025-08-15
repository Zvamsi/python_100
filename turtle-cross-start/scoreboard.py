from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.setpos(-280,250)

    def display_score(self):
        self.write(f'Level: {self.score}',font=FONT)
    def update_score(self):
        self.clear()
        self.score+=1
        self.display_score()

    def game_over(self):
        self.setpos(-90,0)
        self.write("GAME OVER",font=FONT)




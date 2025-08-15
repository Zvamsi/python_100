import random
import time
from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600,starty=25)
screen.tracer(0)
p1=Player()
car_manager=CarManager()
score_board=Scoreboard()
over=Scoreboard()

screen.listen()
screen.onkey(p1.move__,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Create car and move them
    car_manager.create_cars()
    car_manager.go_to()
    # car_manager.gen_car_color_check()

    #Detect collision and Stop the game
    for car in car_manager.all_cars:
        if car.distance(p1)<25:
            game_is_on=False

    #Detect when player reached the end
    if p1.is_at_end():
        p1.go_to_start()
        car_manager.increase_speed()
        score_board.update_score()
    #Display score
    score_board.display_score()

    #Display Game Over
    if not game_is_on:
        over.game_over()
        game_is_on=True





screen.exitonclick()

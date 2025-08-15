import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT: int = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]

    def create_cars(self):
        if random.randint(0,6)==6:
            new_car=Turtle('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.speed(STARTING_MOVE_DISTANCE)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.setposition(300,random_y)
            self.all_cars.append(new_car)

    def go_to(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def gen_car_color_check(self):
        for car in self.all_cars:
            print(car.color())

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE+=MOVE_INCREMENT

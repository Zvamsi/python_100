import turtle as t
import random

my_turtle=t.Turtle()
t.colormode(255)


def custom_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b

my_turtle.speed(40)

def turtle_movement():
    my_turtle.color(custom_color())
    my_turtle.circle(100)
    my_turtle.left(10)


for _ in range (36):
    turtle_movement()

screen=t.Screen()
screen.exitonclick()
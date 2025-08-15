import random
import turtle as t
colors=[(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202)]

my_turtle=t.Turtle()
t.colormode(255)
my_turtle.color('white')
my_turtle.speed(20)

my_turtle.setpos(-200,-200)
my_turtle.hideturtle()
for _ in range(10):
    for _ in range(10):
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.dot(20,random.choice(colors))
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(500)
    my_turtle.right(180)





screen=t.Screen()
screen.exitonclick()
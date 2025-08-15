import random
import turtle
is_race_on=False
screen=turtle.Screen()
screen.setup(height=400,width=500)
user_bid=screen.textinput("Coin Betting","Which color turtle will win ?")

colors=['violet','blue','green','indigo','yellow','orange','red']
direction=[0,90,180,270,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
y_pos=[-140,-97,-54,-1,52,105,150]
turtle_list=[]
for i in range(0,6):
    new_turtle=turtle.Turtle(shape='turtle')
    new_turtle.speed(20)
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.setpos(-230, y_pos[i])
    turtle_list.append(new_turtle)

if user_bid:
    is_race_on=True
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor()>230:
            is_race_on=False
            winner=turtle.pencolor()
            if user_bid == winner:
                print(f"You won, the winning color is {winner}")
            else:
                print(f"You loose, the winning color is {winner}")
        if turtle.ycor()>230 or turtle.ycor()<-230:
            turtle_list.remove(turtle)

        rand_dist=random.randint(0,10)
        turtle.right(random.choice(direction))
        turtle.forward(rand_dist)

screen.exitonclick()
from turtle import Screen
import time

from scoreboard import ScoreBoard
from snake import Snake
from food import Food

SCORE=0

screen=Screen()
screen.setup(height=500,width=500)
screen.bgcolor('black')
screen.title('Snack game !')
screen.tracer(0)

scoreboard=ScoreBoard(0)
snake=Snake(screen)
food=Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update()
        scoreboard.write_to()

    #Detect Collision with the wall
    if snake.head.xcor() > 240 or snake.head.ycor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() < -240:

        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10 :

            scoreboard.reset()
            snake.reset()


















screen.exitonclick()
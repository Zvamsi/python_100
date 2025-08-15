import time
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball_speed=1
is_game_on=True
score_board=Scoreboard()
ball=Ball()


screen=Screen()
screen.title('PING PONG')
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800,height=600,startx=250,starty=20)

screen.listen()

screen.onkey(lambda :r_paddle.move__(20),'Up')
screen.onkey(lambda :r_paddle.move__(-20),'Down')
screen.onkey(lambda:l_paddle.move__(20),'w')
screen.onkey(lambda:l_paddle.move__(-20),'s')

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    #Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    #Detect collision with r_paddle
    if (ball.distance(r_paddle)< 50 and ball.xcor() > 320) or (ball.distance(l_paddle)< 50 and ball.xcor() < -320):
        ball.pitch()

    #Paddle misses the ball
    if ball.xcor() > 380:
        ball.miss()
        score_board.l_point()

    if ball.xcor() < -380:
        ball.miss()
        score_board.r_point()































screen.exitonclick()
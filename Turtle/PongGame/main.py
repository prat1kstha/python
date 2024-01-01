from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(1400, 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-650, 0))
r_paddle = Paddle((650, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor()>380 or ball.ycor()<-380:
        ball.y_bounce()

    # Detect collision with paddle
    if (ball.distance(r_paddle)<50 and ball.xcor()>630 and ball.xcor()<=650) or (ball.distance(l_paddle)<50 and ball.xcor()<-630 and ball.xcor()>=-650):
        ball.x_bounce()

    # Detect R paddle misses    
    if ball.xcor()>700:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses    
    if ball.xcor()<-700:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
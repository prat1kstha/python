from turtle import Turtle, Screen
from snake import Snake
import random
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake.create_snake()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
        
        

screen.exitonclick()
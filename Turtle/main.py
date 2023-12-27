from turtle import Screen, Turtle

timmy = Turtle()
timmy.shape("turtle")

screen = Screen()

# timmy.color("red")

# Drawing a square
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screen.clear()

# Drawing a dashed line
for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen.exitonclick()

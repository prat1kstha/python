from turtle import Screen, Turtle

timmy = Turtle()
timmy.shape("turtle")

screen = Screen()

# timmy.color("red")

# # Drawing a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# screen.clear()

# # Drawing a dashed line
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# screen.clear()

# Drawing shapes


def draw_shape(sides):
    RADIUS = 360

    for _ in range(sides):
        timmy.forward(100)
        timmy.right(RADIUS/sides)


for no_of_shape in range(3, 9):
    draw_shape(no_of_shape)

screen.exitonclick()

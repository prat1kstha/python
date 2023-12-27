from turtle import Screen, Turtle
import random

from networkx import draw

timmy = Turtle()
# timmy.shape("turtle")

screen = Screen()
screen.colormode(255)

timmy.pensize(2)
timmy.speed(5)


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

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


# def draw_shape(sides):
#     RADIUS = 360

#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(RADIUS/sides)

# for no_of_shape in range(3, 9):
#     draw_shape(no_of_shape)


# Random Walk

# while True:
#     walk_len = random.randint(20, 60)
#     turn_side = random.choice([0, 90, 180, 270])

#     timmy.color(get_random_color())
#     timmy.forward(walk_len)
#     timmy.right(turn_side)

# screen.clear()

# Making a Spirograph
radius = 80
gap_size = 10


def draw_spirograph(radius, gap):
    timmy.speed(15)
    TOTAL_RADIUS = 360

    for _ in range(int(TOTAL_RADIUS / gap)):
        timmy.color(get_random_color())
        timmy.circle(radius)

        timmy.right(gap)


draw_spirograph(radius, gap_size)

screen.exitonclick()

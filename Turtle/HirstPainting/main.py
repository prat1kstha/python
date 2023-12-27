import colorgram
import random
from turtle import Turtle, Screen, position

colors = colorgram.extract("Turtle\\HirstPainting\\th.jpg", 30)
pallette = []

for color in colors:
    rgb = color.rgb
    pallette.append((rgb.r, rgb.g, rgb.b))


t = Turtle()
s = Screen()

s.colormode(255)

win_height = s.window_height()
win_width = s.window_width()

s.setworldcoordinates(-1, -1, win_width-1, win_height-1)

y_coordinate = 0

t.speed(20)
while (t.position()[1] <= s.window_height()):

    random_color = random.choice(pallette)

    t.dot(15, random_color)

    t.penup()
    t.fd(int(win_width / 10)-1)
    t.pendown()

    if t.position()[0] >= win_width:
        y_coordinate += int(win_height/10)

        t.penup()
        t.sety(y_coordinate)
        t.setx(-1)

s.exitonclick()

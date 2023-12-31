from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y_coordinate = -100

for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])

    turtle.penup()
    turtle.goto(x=-230, y=y_coordinate)

    turtles.append(turtle)
    y_coordinate += 30

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color.lower() == user_bet.lower():
                print("You have won!")
            else:
                print(f"You have lost! The {winner_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

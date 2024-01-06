import turtle
import pandas

image_file = "Panda/USStatesGame/blank_states_img.gif"
csv_file = "Panda/USStatesGame/50_states.csv"
remaining_states_file = "Panda/USStatesGame/RemainingStates.csv"

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(image_file)
turtle.shape(image_file)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv(csv_file)
all_states = data["state"].to_list()

is_game_on = True
guessed_states = []

while (is_game_on):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} states correct", prompt="What's another state's name?")

    data_row = data[data["state"].str.lower() == answer_state]

    if len(data_row) != 0:
        x_cor = data_row["x"].iloc[0]
        y_cor = data_row["y"].iloc[0]
        state_name = data_row["state"].iloc[0]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(state_name)

        guessed_states.append(state_name)

    if answer_state is None or answer_state.lower() == "exit" or len(guessed_states) == len(all_states):
        is_game_on = False

        missing_states = [state for state in all_states if state not in guessed_states]
        
        new_data = pandas.DataFrame(missing_states)    
        print(new_data)
        new_data.to_csv(remaining_states_file)


turtle.mainloop()
screen.exitonclick()
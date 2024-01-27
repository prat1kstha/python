import tkinter

window = tkinter.Tk()

window.title("My Program")
window.minsize(width=500, height=500)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
input = tkinter.Entry(width=10)

input.pack()

# import turtle

# tim = turtle.Turtle()
# # tim.write()

window.mainloop()
import tkinter

window = tkinter.Tk()

window.title("My Program")
window.minsize(width=500, height=300)

window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()

my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button1 = tkinter.Button(text="Click Me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = tkinter.Button(text="Click Me 2", command=button_clicked)
button2.grid(column=2, row=0)


# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
# input.pack()

window.mainloop()
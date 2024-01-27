from tkinter import *

window = Tk()

window.title("Widgets Examples")
window.minsize(width=500, height=500)


# Labels
my_label = Label(text="This is old text")
my_label.config(text="This is new text")
my_label.pack()


# Buttons
def action():
    print("Do sth")

button = Button(text="Click Me", command=action)
button.pack()


# Entries
entry = Entry(width=30)
entry.insert(END, string="Some text to being with.")

print(entry.get())
entry.pack()


# Text
text = Text(height=5, width=30)

text.focus()
text.insert(END, "Example of multi-line text entry")
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)

spinbox.pack()


# Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Mango", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
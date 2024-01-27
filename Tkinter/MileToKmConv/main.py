from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
# window.minsize(width=600, height=300)

miles_input = Entry(width=10)
miles_input.insert(END, "0")
miles_input.grid(column=1, row=0)

miles_lbl = Label(text="Miles")
miles_lbl.grid(column=2, row=0)

equals_to_lbl = Label(text="is equal to")
equals_to_lbl.grid(column=0, row=1)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

km_lbl = Label(text="Km")
km_lbl.grid(column=2, row=1)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_output.config(text=km)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
from tkinter import *

def milesToKilometers():
    miles = float(miles_input.get())
    km = miles*1.60934
    kilometers_result.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kilometers_result = Label(text="0")
kilometers_result.grid(row=1, column=1)

kilometers_label = Label(text="Km")
kilometers_label.grid(row=1, column=2)

button_calculate = Button(text="Calculate", command=milesToKilometers)
button_calculate.grid(row=2, column=1)

window.mainloop()
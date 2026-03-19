import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


#Label
my_label = tkinter.Label(text="My first GUI", font=("Arial", 25))
my_label.config(text="New text")
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

#button

button = tkinter.Button(text="Click me!")
button.grid(row=1, column=1)

#new button

new_button = tkinter.Button(text="Click me!")
new_button.grid(row=0, column=2)



#Entry

input = tkinter.Entry(width=10)
print(input.get())
input.grid(row=2, column=3)



window.mainloop()
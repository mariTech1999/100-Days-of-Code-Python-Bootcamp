from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    entry_password.delete(0, "end")

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message="Confirm your email and password")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                entry_web.delete(0, "end")
                entry_email.delete(0, "end")
                entry_password.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_pass = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_pass)
canvas.grid(row=0, column=1)

label_web = Label(text="Website")
label_web.grid(row=1, column=0)

label_email = Label(text="Email")
label_email.grid(row=2, column=0)

label_password = Label(text="Password")
label_password.grid(row=3, column=0)


entry_web = Entry(width=35)
entry_web.grid(row=1, column=1, columnspan=2,sticky="EW")
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2,sticky="EW")
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1, sticky="EW")


generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2,sticky="EW", padx=(3,0))
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
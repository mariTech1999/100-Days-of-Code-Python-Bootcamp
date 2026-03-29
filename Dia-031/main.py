from textwrap import fill
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
df = {}

try:
    database = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_df = pd.read_csv("data/english_words.csv")
    df = original_df.to_dict("records")
else:
    df = database.to_dict("records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(df)

    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    window.after(3000, func=show_answer)

def show_answer():
    canvas.itemconfig(card_title, text="Portuguese", fill="white")
    canvas.itemconfig(card_word, text=current_card["Portuguese"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    print(len(df))
    df.remove(current_card)
    data = pd.DataFrame(df)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=show_answer)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400,150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()



window.mainloop()
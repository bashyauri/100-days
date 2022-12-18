import os
import time
from tkinter import *
import pandas as pd
from random import *
from tkinter import messagebox


# -----Read Data-----------------------
path = os.getcwd()
try:
    df = pd.read_csv(os.path.join(
        path, "flash-cards/data", "words_to_learn.csv"))
except FileNotFoundError:
    try:
        df = pd.read_csv(os.path.join(
            path, "flash-cards/data", "french_words.csv"))
    except FileNotFoundError:
        messagebox.showerror("File Not found: ")
    else:
        data = df.to_dict(orient="records")
else:
    data = df.to_dict(orient="records")
selected_word = {}


def random_word():
    global selected_word
    selected_word = choice(data)
    canvas.itemconfig(language, text=f"French")
    canvas.itemconfig(word, text=f"{selected_word['French']}")
    canvas.itemconfig(canvas_image, image=front_img)
    window.after(3000, to_english)


def to_english():

    canvas.itemconfig(language, text=f"English")
    canvas.itemconfig(word, text=f"{selected_word['English']}")
    canvas.itemconfig(canvas_image, image=back_img)


def check_word():
    global selected_word
    data.remove(selected_word)
    data_dict = pd.DataFrame(data)

    data_dict.to_csv(os.path.join(
        path, "flash-cards/data", "words_to_learn.csv"), index=False)


BACKGROUND_COLOR = "#B1DDC6"

# UI
# windows
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas

front_img = PhotoImage(file=os.path.join(
    path, "flash-cards/images", "card_front.png"))
back_img = PhotoImage(file=os.path.join(
    path, "flash-cards/images", "card_back.png"))
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_img)
# labels
language = canvas.create_text(
    400, 150, text="Language", font=("Ariel", 40, "italic"))
word = canvas.create_text(
    400, 263, text="words", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file=os.path.join(
    path, "flash-cards/images", "wrong.png"))
wrong_button = Button(
    image=wrong_img, command=random_word, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file=os.path.join(
    path, "flash-cards/images", "right.png"))
right_button = Button(
    image=right_img, command=check_word, highlightthickness=0)
right_button.grid(column=1, row=1)


window.mainloop()

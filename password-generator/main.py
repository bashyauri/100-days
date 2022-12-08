# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas

canvas = Canvas(width=200, height=200)


key_img = PhotoImage(file="key.png")
canvas.create_image(100, 100, image=key_img)
canvas.grid(row=2, column=2)


window.mainloop()

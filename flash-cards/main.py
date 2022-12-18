from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# UI
# windows
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526)
canvas.grid(column=0, row=0)


window.mainloop()

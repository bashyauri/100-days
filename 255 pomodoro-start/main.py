import time
import os
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = int(WORK_MIN * 60)
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(fg=RED, text="Break")
    elif reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(fg=GREEN, text="Work")
    else:
        count_down(short_break_sec)
        timer_label.config(fg=PINK, text="Break")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if (count > 0):
        global timer
        timer = window.after(1000, count_down, count-1)
    else:

        start_timer()
        work_count = math.floor(reps/2)

        check_label.config(text="✔" * work_count)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(
    FONT_NAME, 50, "bold"), highlightthickness=0)
timer_label.grid(row=0, column=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(
    FONT_NAME, 8, "bold"), highlightthickness=0)
check_label.grid(row=4, column=2)
# buttons
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=3, column=1)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=3, column=3)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
path = os.getcwd()

tomato_img = PhotoImage(
    file=os.path.join(path, "255 pomodoro-start", "tomato.png"))

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


window.mainloop()

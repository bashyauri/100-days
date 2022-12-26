from tkinter import *
from quiz_brain import QuizBrain
import os
THEME_COLOR = "#375362"


file_path = os.path.dirname(__file__)


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.quiz = quiz
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some question", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_img = PhotoImage(
            file=os.path.join(file_path, 'images/true.png'))
        self.false_img = PhotoImage(file=os.path.join(
            file_path, 'images/false.png'))
        self.yes_button = Button(
            image=self.true_img, highlightthickness=0, command=self.is_true)
        self.yes_button.grid(row=2, column=0)
        self.no_button = Button(image=self.false_img,
                                highlightthickness=0, command=self.is_false)
        self.no_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You have reached the end of the quiz")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

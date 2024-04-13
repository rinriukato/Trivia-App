from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, "italic")
PADDING = 20
TRUE_BUTTON = "images/true.png"
FALSE_BUTTON = "images/false.png"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=PADDING, pady=PADDING, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=2, row=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='default', fill=THEME_COLOR, font=FONT, width=280)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        true_image = PhotoImage(file=TRUE_BUTTON)
        false_image = PhotoImage(file=FALSE_BUTTON)
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.on_true_button)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.on_false_button)

        self.true_button.grid(column=1, row=3)
        self.false_button.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def on_true_button(self):
        is_correct = self.quiz_brain.check_answer('True')
        self.show_answer_status(is_correct)

    def on_false_button(self):
        is_correct = self.quiz_brain.check_answer('False')
        self.show_answer_status(is_correct)

    def show_answer_status(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score :{self.quiz_brain.score}")

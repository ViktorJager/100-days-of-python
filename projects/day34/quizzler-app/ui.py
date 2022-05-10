from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score
        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font=("Courier, 14")
        )
        self.score_label.grid(row=0, column=1)

        # display
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="question",
            font=("Arial", 16, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        true_img = PhotoImage(file="./images/true.png")
        self.btn_true = Button(
            image=true_img, highlightthickness=0, command=self.true_pressed
        )
        self.btn_true.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.btn_false = Button(
            image=false_img,
            highlightthickness=0,
            command=self.false_pressed,
        )
        self.btn_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")
            self.canvas.itemconfig(
                self.question_text, text="You be done with quiz nao."
            )

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

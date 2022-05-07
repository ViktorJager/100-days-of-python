from tkinter import *
import pandas as pd
import random


# Constants
BACKGROUND_COLOR = "#B1DDC6"
ENGLISH = "English"
FRENCH = "French"

to_learn = {}
current_card = {}


# ------------------------ Data ------------------------ #

# Read data once
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except (FileNotFoundError, ValueError):
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas_flashcard.itemconfigure(card_title, text=FRENCH, fill="black")
    canvas_flashcard.itemconfigure(card_text, text=current_card["French"], fill="black")
    canvas_flashcard.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


# data = DataFrame(orient="records")

# Flip card
def flip_card():
    canvas_flashcard.itemconfig(card_title, text=ENGLISH, fill="white")
    canvas_flashcard.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas_flashcard.itemconfig(canvas_image, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)

    next_card()


# ------------------------- UI ------------------------- #

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

# Flashcard
canvas_w = 800
canvas_h = 526
canvas_flashcard = Canvas(
    width=canvas_w,
    height=canvas_h,
    highlightthickness=0,
    background=BACKGROUND_COLOR,
)
canvas_image = canvas_flashcard.create_image(
    canvas_w / 2, canvas_h / 2, image=card_front
)
canvas_flashcard.grid(column=0, row=0, columnspan=2)

# Flashcard text
card_title = canvas_flashcard.create_text(
    400, 150, text=ENGLISH, font=("Arial", 40, "italic")
)
card_text = canvas_flashcard.create_text(
    400, 256, text="sample", font=("Arial", 60, "bold")
)


# Buttons
img_right = PhotoImage(file="./images/right.png")
img_wrong = PhotoImage(file="./images/wrong.png")
btn_right = Button(image=img_right, highlightthickness=0, bd=0, command=is_known)
btn_wrong = Button(image=img_wrong, highlightthickness=0, bd=0, command=next_card)
btn_right.grid(column=1, row=1)
btn_wrong.grid(column=0, row=1)


# tmp


# Mainloop
next_card()
window.mainloop()

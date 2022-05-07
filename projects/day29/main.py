from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pw_entry.delete(0, END)
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = []
    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pw_entry.delete(0, END)


# ------------------------- SEARCH PASSWORD --------------------------- #


def search():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        try:
            email = data[website]["email"]
            pw = data[website]["password"]
        except KeyError:
            messagebox.showinfo(
                title="Error", message="No data saved for this website."
            )
        else:
            messagebox.showinfo(
                title="Password", message=f"{website}\nEmail: {email}\nPassword: {pw}"
            )


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("PWManager")
window.config(padx=20, pady=20)
lock_img = PhotoImage(file="logo.png")
window.iconphoto(False, lock_img)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
pw_label = Label(text="Password:")

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
pw_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
email_entry = Entry()
pw_entry = Entry()

website_entry.grid(column=1, row=1, columnspan=1, sticky="NSEW")
email_entry.grid(column=1, row=2, columnspan=2, sticky="NSEW")
pw_entry.grid(column=1, row=3, sticky="NSEW")

website_entry.focus()
email_entry.insert(0, "viktor@mail.com")

# Buttons
generate_pw_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", command=save)
search_button = Button(text="Search", command=search)

generate_pw_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2, sticky="NSEW")
search_button.grid(column=2, row=1, columnspan=2, sticky="NSEW")

window.mainloop()

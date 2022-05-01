from tkinter import *

# Placement managers: Pack, Place, Grid


def button_clicked():
    entry_text = input.get()
    my_label.config(text=entry_text)


window = Tk()
window.title("GUI Application")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="I am a Label!", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
my_label.grid(column=0, row=0)
# my_label["text"] = "New Text"
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click me too", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()

from tkinter import *

# Placement managers: Pack, Place, Grid


def convert_miles_to_km():
    miles = float(input.get())
    km = str(round(miles * 1.60934, 1))
    answer_label.config(text=km)


window = Tk()
window.title("Miles to KM converter")
window.config(padx=20, pady=20)
# window.minsize(width=200, height=100)


# Labels
km_label = Label(text="Km", font=("Arial", 14))
km_label.grid(column=2, row=1)

miles_label = Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 14))
equal_label.grid(column=0, row=1)

answer_label = Label(text="x", font=("Arial", 14))
answer_label.grid(column=1, row=1)


# Button
button = Button(text="Calculate", command=convert_miles_to_km)
button.grid(column=1, row=2)


# Entry
input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()

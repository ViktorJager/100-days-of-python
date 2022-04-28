import pandas as pd
import turtle
from turtle import Turtle

NUMBER_OF_STATES = 50

# Screen setup
screen = turtle.Screen()
screen.setup(1000,800)
screen.screensize(bg="cornsilk")
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Write states on screen
pen = Turtle(shape="circle")
pen.shapesize(stretch_wid=0.3, stretch_len=0.3)
pen.penup()


data = pd.read_csv("50_states.csv")
# all_states = data.state.to_list()

guessed_states = []

correct_states = 0
game_is_on = True
while game_is_on:
    if correct_states >= NUMBER_OF_STATES:
        game_is_on = False
        print("You won!")

    # Get user answer
    answer_state = screen.textinput(title=f"{correct_states}/{NUMBER_OF_STATES} Guess the State", prompt="Name another state: ")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        game_is_on = False
    # Check answer, write on screen if correct
    elif answer_state in data.state.unique() and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        pen.goto(int(state_data.x), int(state_data.y))
        pen.write(arg=f"{answer_state}", align='center')
        correct_states += 1
    else:
        print("invalid state")


# states to learn
states_to_learn_dict = {
    "state": [],
    "x": [],
    "y": [],
}

all_states = data.state.to_list()
states_to_learn = all_states.copy()
for state in guessed_states:
    if state in states_to_learn:
        states_to_learn.remove(state)


for state in states_to_learn:
    temp_state = data[data.state == state]
    states_to_learn_dict["state"].append(state)
    states_to_learn_dict["x"].append(temp_state.x.to_string())
    states_to_learn_dict["y"].append(temp_state.y.to_string())


df = pd.DataFrame(states_to_learn_dict)
df.to_csv("states_to_learn.csv")

turtle.mainloop()

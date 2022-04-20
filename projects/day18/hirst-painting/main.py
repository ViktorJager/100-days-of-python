# import colorgram

""" # Extract 6 colors from an image.
colors = colorgram.extract("pkmn.jpg", 15)

rgb_colors = []

for color in colors:
    current_color = color
    rgb_colors.append((current_color.rgb.r, current_color.rgb.g, current_color.rgb.b))

print(rgb_colors) """

color_list = [
    (227, 230, 237),
    (188, 158, 118),
    (138, 157, 179),
    (140, 96, 63),
    (178, 149, 166),
    (150, 176, 164),
    (82, 100, 122),
    (125, 82, 107),
    (232, 217, 88),
    (174, 144, 56),
    (171, 96, 120),
    (197, 90, 74),
]

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(75, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

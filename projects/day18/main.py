import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

heading = 3.6
for _ in range(100):
    tim.color(random_color())
    tim.circle(200 - heading)
    tim.setheading(heading)
    heading += 3.6

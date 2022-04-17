from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "green")

angle = 0
for _ in range(100):

    timmy.forward(2 + angle * 2)
    timmy.right(angle)
    angle += 1

my_screen = Screen()
my_screen.exitonclick()

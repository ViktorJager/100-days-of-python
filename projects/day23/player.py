from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 100
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_player(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def finished_level(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset_position(self):
        self.goto(STARTING_POSITION)

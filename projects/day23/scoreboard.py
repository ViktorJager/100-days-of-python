from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "Center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()

        self.hideturtle()
        self.goto(x=-150, y=265)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            arg=f"Level: {self.level}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def update_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(
            arg="GAMEOVER!",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            arg=f"Score: {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def update_score(self):
        self.score += 1
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

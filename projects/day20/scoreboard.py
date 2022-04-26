from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} | High score: {self.highscore}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.set_highscore()
            self.highscore = self.get_highscore()
        self.score = 0
        self.update_scoreboard()

    def get_highscore(self):
        with open("data.txt", mode='r') as file:
            return int(file.read())

    def set_highscore(self):
        with open("data.txt", mode='w') as file:
            file.write(str(self.score))


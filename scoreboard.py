from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.update_scoreboard()
        with open("data.txt", mode="r") as data:
            self.high_score = data.read()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", mode="r") as data: 
            self.high_score = data.read()
            self.write(arg=f"score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

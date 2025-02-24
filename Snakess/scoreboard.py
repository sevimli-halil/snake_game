from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 130)
        self.pencolor("white")


    def write_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}  HIGH SCORE:{self.high_score}", font=FONT, align=ALIGNMENT)
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score-1
        self.score = 0
        self.write_score()
# Scoreboard Class

from turtle import Turtle

FONTNAME = "Courier"
FONTSIZE = 15
FONTTYPE = "normal"
SCORE_COORDINATES = (-280, 275)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_COORDINATES[0], SCORE_COORDINATES[1])
        self.write(f"Level: {self.level}", font=(FONTNAME, FONTSIZE, FONTTYPE))
        self.penup()

    def increment_level(self):
        self.level += 1

    def print_game_over(self):
        self.goto(0, -20)
        self.write("GAME OVER!", align="center", font=(FONTNAME, 40, FONTTYPE))

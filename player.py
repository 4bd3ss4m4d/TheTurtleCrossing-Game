# Player class

from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_Y_POSITION = 280
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.shapesize(1, 1, 1)
        self.setheading(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_Y_POSITION:
            return True
        else:
            return False

    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)

    def go_right(self):
        self.setheading(RIGHT)
        self.forward(MOVE_DISTANCE)

    def go_left(self):
        self.setheading(LEFT)
        self.forward(MOVE_DISTANCE)

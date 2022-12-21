import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
Y_POSITION = []
for y in range(-240, 240, 10):
    Y_POSITION.append(y)


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(x=320, y=random.choice(Y_POSITION))

    def move(self, speed_level):
        self.bk(STARTING_MOVE_DISTANCE + speed_level)

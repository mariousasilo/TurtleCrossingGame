from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=260)
        self.write(arg=f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align="center", font=FONT)

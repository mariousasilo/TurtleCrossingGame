import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import choice


NUMBER_OF_CARS = [0, 0, 0, 0, 1]

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Player()
car_groups = []
speed_level = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    num_of_cars = choice(NUMBER_OF_CARS)
    for car in range(num_of_cars):
        car_groups.append(CarManager())
    for group in car_groups:
        group.move(speed_level)
        if player.distance(group) <= 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        player.reset()
        scoreboard.level_up()
        speed_level += 10

    screen.onkey(key="w", fun=player.move)

screen.exitonclick()

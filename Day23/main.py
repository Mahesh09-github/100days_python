import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Road Crossing")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    #turtle should not go out of screen
    if player.ycor() > 280:
        player.go_to_start()





screen.exitonclick()
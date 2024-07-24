import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.generate_car()
    car_manager.move_cars()
    screen.update()
    # Detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
            break

    # Detect if reached other side
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.level_up()


screen.exitonclick()

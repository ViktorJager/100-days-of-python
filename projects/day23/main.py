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
screen.onkeypress(player.move_player, "Up")

car_spawner = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    # Spawn new cars
    if car_spawner % 10 == 0:
        car_manager.create_cars()
    car_spawner += 1

    # Finished level
    if player.finished_level():
        scoreboard.update_level()
        car_manager.increase_carspeed()
        player.reset_position()

    # Check collision
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

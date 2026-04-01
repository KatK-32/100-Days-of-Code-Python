import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# game controls
screen.listen()
screen.onkeypress(player.go_up,"Up")

# play game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect car - turtle collision w/
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect crossing
    if player.at_finish_line():
        player.return_to_start()
        car_manager.raise_level()
        scoreboard.increase_level()

screen.exitonclick()
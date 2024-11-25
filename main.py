import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.move_up, "w")

run = True
loop = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop += 1

    if player.ycor() == FINISH_LINE_Y:
        player.start_position()
        score.next_level()

    if loop % 6 == 0:
        cars.create_car()

    for position in range(len(cars.cars) - 1):
        if cars.cars[position].distance(player) < 20:
            game_is_on = False
            score.game_over()


    cars.cars_move(score.level - 1)

screen.exitonclick()
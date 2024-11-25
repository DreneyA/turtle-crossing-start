import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        random_y = random.randint(-250, 250)
        new_car.goto(350, random_y)
        self.cars.append(new_car)

    def cars_move(self, level):
        for position in range(len(self.cars) - 1):
            new_x = self.cars[position].xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT * level
            self.cars[position].goto(new_x, self.cars[position].ycor())



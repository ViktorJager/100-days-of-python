from hashlib import new
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Car spawn range = (-250, 250)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 1
        self.cars = []
        self.create_cars()

    def create_cars(self):
        for _ in range(6):
            self.add_car()

    def add_car(self):
        car = Turtle(shape="square")
        car.color("black", random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.penup()

        # Randomize position
        x_pos = 310
        y_pos = random.randint(-250, 250)
        car.goto(x_pos, y_pos)
        self.cars.append(car)

    def move_cars(self):
        for car_index in range(len(self.cars)):

            new_x = self.cars[car_index].xcor() - (MOVE_INCREMENT * self.car_speed)
            new_y = self.cars[car_index].ycor()
            self.cars[car_index].goto(new_x, new_y)

    def increase_carspeed(self):
        self.car_speed += 1

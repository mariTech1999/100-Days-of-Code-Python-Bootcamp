from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_pool()

    def create_pool(self):
        for _ in range(20):
            new_car = Turtle("square")
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_x = random.randint(-300, 300)
            random_y = random.randint(-250, 250)
            new_car.goto(random_x, random_y)

            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

            if car.xcor() < -310:
                self.recycle_car(car)

    def recycle_car(self, car):
        rand_y=random.randint(-250, 250)
        car.goto(310, rand_y)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
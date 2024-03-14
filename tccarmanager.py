import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
YAXIS = []

for z in range(-215, 215, 50):
    YAXIS.append(z)

class CarManager:

    def __init__(self):
        """initialises the cars"""
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        """creates the cars in turtle crossing game"""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1.3, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.choice(YAXIS)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """moves the cars"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """according to level increases the cars moving speed"""
        self.car_speed += MOVE_INCREMENT

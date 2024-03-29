import random
from turtle import Turtle
class SnakeFood(Turtle):
    def __init__(self):
        """generates the snake food"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("White")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """after successful consumption changes the position of food"""
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.goto(x, y)

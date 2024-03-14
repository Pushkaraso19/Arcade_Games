from turtle import Turtle

class Display(Turtle):
    def __init__(self):
        """displays the ball"""
        super().__init__()
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.pencolor("White")
        self.hideturtle()
        self.pensize(3)
        for i in range(25):
            self.forward(15)
            self.penup()
            self.forward(10)
            self.pendown()

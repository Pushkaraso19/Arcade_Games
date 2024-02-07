from turtle import Turtle

class Display(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.pensize(50)
        self.goto(-300, -270)
        self.pendown()
        self.forward(600)
        self.penup()
        self.goto(-300, 235)
        self.pensize(45)
        self.pendown()
        self.forward(600)

    def road(self):
        y = -240
        for i in range(8):
            self.penup()
            self.color("White")
            self.pensize(3)
            self.hideturtle()
            y += 50
            self.goto(-290, y)
            for j in range(15):
                self.pendown()
                self.forward(30)
                self.penup()
                self.forward(30)

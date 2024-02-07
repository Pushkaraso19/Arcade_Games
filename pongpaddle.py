from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, direction):
        super().__init__()
        self.color("White")
        self.shape("Rectangle")
        self.penup()
        if direction == "left":
            self.goto(-360, 0)
        else:
            self.goto(350, 0)

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

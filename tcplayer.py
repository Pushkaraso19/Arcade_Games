from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 230

class Player(Turtle):

    def __init__(self):
        """creates the player(turtle)"""
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.5)
        self.color("Red")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        """moves the player(turtle) in forward direction"""
        if self.ycor() < 200:
            self.forward(MOVE_DISTANCE)

    def move_backward(self):
        """moves the player(turtle) in backward direction"""
        if self.ycor() > -270:
            self.backward(MOVE_DISTANCE)

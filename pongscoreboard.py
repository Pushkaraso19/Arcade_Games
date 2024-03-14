from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        """creates the scoreboard of ping pong game"""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        """updates the scoreboard"""
        self.clear()
        self.goto(-60, 200)
        self.write(self.l_score, False, "center", ("Tahoma", 60, "normal"))
        self.goto(60, 200)
        self.write(self.r_score, False, "center", ("Tahoma", 60, "normal"))

    def l_point(self):
        """keeps the track of score of left player"""
        self.l_score += 1
        self.update()

    def r_point(self):
        """keeps the track of score of right player"""
        self.r_score += 1
        self.update()

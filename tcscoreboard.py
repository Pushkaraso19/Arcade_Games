from turtle import Turtle

FONT = ("Courier", 20, "normal")
FONT1 = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.color("White")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level = {self.level}", False, "left", FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(-100, 260)
        self.write(f"GAME OVER!", False, "left", FONT1)

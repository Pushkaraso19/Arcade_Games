from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        """creates the ball"""
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.x_move = 0.3
        self.y_move = 0.3
        self.move_speed = 0.1

    def move(self):
        """moves the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """if the ball touches the paddles then it bounces the ball"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        """if the ball touches the upper or lower wall then it bounces the ball"""
        self.y_move *= -1

    def reset_pos(self):
        """resets the position of ball"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

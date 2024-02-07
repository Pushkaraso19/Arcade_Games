import sys
import time
from turtle import Screen
from pongdisplay import Display
from pongpaddle import Paddle
from pongball import Ball
from pongscoreboard import Score

def pong_main(root):
    pong_screen = Screen()
    pong_screen.setup(800, 600)
    pong_screen.bgcolor("Black")
    pong_screen.title("Ping Pong")
    pong_screen.register_shape("Rectangle", ((50, -10), (50, 10), (-50, 10), (-50, -10)))

    def start():
        inp = pong_screen.numinput("New Game", "\n1.Play New Game\n2.Go to Main Menu\n3.Exit\nEnter Your Choice", minval=1, maxval=3)
        if inp == 1:
            play_game()
        elif inp == 2:
            pong_screen.bye()
            root.deconify()
        else:
            sys.exit()

    def play_game():
        time.sleep(1/60)
        pong_screen.clear()
        pong_screen.bgcolor("Black")
        pong_screen.tracer(0)

        paddle_left = Paddle("left")
        paddle_right = Paddle("right")
        ball = Ball()
        Display()
        score = Score()

        pong_screen.listen()
        pong_screen.onkeypress(paddle_right.go_up, "Up")
        pong_screen.onkeypress(paddle_right.go_down, "Down")
        pong_screen.onkeypress(paddle_left.go_up, "w")
        pong_screen.onkeypress(paddle_left.go_down, "s")
        pong_screen.onkey(start, "Escape")

        game_on = True

        while game_on:
            pong_screen.update()
            ball.move()

            # Detect collision with wall
            if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()

            # Detect collision with paddle
            if (ball.distance(paddle_right) < 50 and ball.xcor() > 330) or (ball.distance(paddle_left) < 50 and ball.xcor() < -340):
                ball.bounce_x()

            # Detect Right paddle misses
            if ball.xcor() > 380:
                ball.reset_pos()
                score.l_point()

            # Detect Left paddle misses
            if ball.xcor() < -380:
                ball.reset_pos()
                score.r_point()

    play_game()

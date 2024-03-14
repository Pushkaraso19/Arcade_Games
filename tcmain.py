import sys
import time
from turtle import Screen
from tcplayer import Player, FINISH_LINE_Y, STARTING_POSITION
from tccarmanager import CarManager
from tcscoreboard import Scoreboard
from tcdisplay import Display

def turtle_crossing_main(root):
    tc_screen = Screen()
    tc_screen.setup(width=600, height=600)
    tc_screen.bgcolor("#2F2F2F")
    tc_screen.title("Turtle Crossing Game")
    tc_screen.tracer(0)

    def start():
        inp = tc_screen.numinput("New Game", "\n1.Play New Game\n2.Go to Main Menu\n3.Exit\nEnter Your Choice", minval=1, maxval=3)
        if inp == 1:
            play_game()
        elif inp == 2:
            tc_screen.setup(startx=10000,starty=10000)
            root.deiconify()
            tc_screen.mainloop()
        else:
            sys.exit()

    def play_game():
        tc_screen.clear()
        tc_screen.bgcolor("#2F2F2F")
        tc_screen.tracer(0)
        tc_screen.listen()

        display = Display()
        display.road()

        player = Player()
        car = CarManager()
        score = Scoreboard()

        tc_screen.onkey(player.move_forward, "Up")
        tc_screen.onkey(player.move_backward, "Down")
        tc_screen.onkey(start, "Escape")

        game_is_on = True

        while game_is_on:
            time.sleep(0.1)
            tc_screen.update()

            car.create_cars()
            car.move_cars()

            for cars in car.all_cars:
                if cars.distance(player) < 30:
                    game_is_on = False
                    score.game_over()
                    start()

            if player.ycor() == FINISH_LINE_Y:
                score.increase_level()
                player.goto(STARTING_POSITION)
                car.increase_speed()

    play_game()

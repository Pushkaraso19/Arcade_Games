import sys
import time
import turtle
from turtle import Screen
from snakestruct import Snake
from snakefood import SnakeFood
from snakescoreboard import SnakeScoreBoard

def snake_main(root):
    """main function of snake game"""
    snake_screen = Screen()
    snake_screen.title("Arcade Games")
    snake_screen.setup(600, 600)
    snake_screen.bgcolor("#2F2F2F")

    def snake_start():
        """shows the main menu for operations of snake game"""
        inp = turtle.numinput("New Game", "\n1.Play New Game\n2.Reset Highscore\n3.Go to Main Menu\n4.Exit\nEnter Your Choice", minval=1, maxval=4)
        if inp == 1:
            snake_play_game()
        elif inp == 2:
            with open("score_record.txt", mode="w") as data:
                data.write(f"0")
            snake_start()
        elif inp == 3:
            snake_screen.setup(startx=10000, starty=10000)
            root.deiconify()
            snake_screen.mainloop()
        else:
            sys.exit()

    def snake_play_game():
        """initiates the snake game"""
        snake_screen.clear()
        snake_screen.bgcolor("#2F2F2F")
        snake_screen.tracer(0)

        snake = Snake()
        food = SnakeFood()
        score = SnakeScoreBoard()

        snake_screen.listen()
        snake_screen.onkey(snake.go_up, "Up")
        snake_screen.onkey(snake.go_down, "Down")
        snake_screen.onkey(snake.go_left, "Left")
        snake_screen.onkey(snake.go_right, "Right")
        snake_screen.onkey(snake_start, "Escape")

        game_on = True

        while game_on:
            snake_screen.update()
            time.sleep(0.1)
            snake.move()
            if snake.head.distance(food) < 15:
                # if the snake hits food the food is placed on other location
                food.refresh()
                snake.extend()
                score.increase_score()

            score.check_highscore()

            if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
                # if the snake hits border then game ends
                game_on = False
                score.game_over()
                snake_start()

            for seg in snake.segments[1:]:
                # ends the game if snake touches its tail
                if snake.head.distance(seg) < 10:
                    game_on = False
                    score.game_over()
                    snake_start()

    snake_play_game()

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
difficulty = screen.textinput(title="Difficulty levels : Easy, Medium, Hard", prompt="Choose your difficulty level : ").lower()


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    #Difficulty level
    time.sleep(scoreboard.difficulty(difficulty))
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.add_point()

        # extend the snake tail
        snake.extend()


    #detect collision with wall
    if snake.wall_coll_check() == 1:
        game_is_on = False
        scoreboard.refresh()
        scoreboard.game_over()

    #detect tail collision
    if snake.tail_collision_check() == 1:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
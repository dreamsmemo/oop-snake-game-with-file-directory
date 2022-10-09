from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake_screen = Screen()
snake_screen.setup(width=600, height=600)
snake_screen.bgcolor("black")
snake_screen.title("Snake Game")
snake_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

snake_screen.listen()
snake_screen.onkey(snake.up, "Up")
snake_screen.onkey(snake.down, "Down")
snake_screen.onkey(snake.left, "Left")
snake_screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    snake_screen.update()
    time.sleep(0.07)
    snake.move()
    # detect snake collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        scoreboard.update_score()
        snake.add_segment()

    # detect snake collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 \
            or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision with snake body
    for i in snake.snake_body[1:]:
        if snake.head.distance(i) < 10:
            scoreboard.reset()
            snake.reset()


snake_screen.exitonclick()

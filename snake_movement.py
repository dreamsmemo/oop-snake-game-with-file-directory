from turtle import Turtle
from snake import Snake

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake_Movement:

    def __init__(self):
        self._snake = Snake()

    def move(self):
        for square in range(len(self._snake.snake_body) - 1, 0, -1):
            new_x = self._snake.snake_body[square - 1].xcor()
            new_y = self._snake.snake_body[square - 1].ycor()
            self._snake.snake_body[square].goto(new_x, new_y)
        self._snake.head.forward(MOVE_DISTANCE)

    def up(self):
        if self._snake.head.heading() != DOWN:
            self._snake.head.setheading(UP)

    def down(self):
        if self._snake.head.heading() != UP:
            self._snake.head.setheading(DOWN)

    def left(self):
        if self._snake.head.heading() != RIGHT:
            self._snake.head.setheading(LEFT)

    def right(self):
        if self._snake.head.heading() != LEFT:
            self._snake.head.setheading(RIGHT)

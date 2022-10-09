from turtle import Turtle

SNAKE_BONE_LENGTH = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """this is to create the main character snake itself."""
        for position in range(0, 3):
            self.add_segment()

    def add_segment(self):
        """this is to lengthen the snake after she ate the food."""
        snake_bone = Turtle()
        snake_bone.penup()
        snake_bone.shape("square")
        snake_bone.color("white")
        self.snake_body.append(snake_bone)

    def move(self):
        """this is to let the snake bone move one by one"""
        for square in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[square - 1].xcor()
            new_y = self.snake_body[square - 1].ycor()
            self.snake_body[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        # move the previous snake off the screen
        for i in self.snake_body:
            i.goto(1000, 1000)
        # initialize the snake
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            

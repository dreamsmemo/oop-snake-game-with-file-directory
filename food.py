import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("sky blue")
        self.speed("fastest")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.new_food()

    def new_food(self):
        xcor = random.randint(-270, 270)
        ycor = random.randint(-270, 250)
        self.goto(xcor, ycor)

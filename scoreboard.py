from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


"""
# import file. default mode ="r": read ; mode = "w": delete original content and write a new line
# mode = "a": append.
file = open("highest_score_list.txt", mode="a")
# function read returns the file contents into str()
contents = file.read()
file.write("\nNew text.")
file.close()
"""

"""
if you don't want to write the "close file" line.
you can write it as "with open() as variable:.
"""


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        with open("highest_score.txt") as f:
            self.highest_score = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", mode="w") as f:
                f.write(f"{self.highest_score}")
        self.score = -1
        self.update_score()


"""
    def game_over(self):
        self.goto(x=-110, y=0)
        self.color("red")
        self.write("GAME OVER", font=("Courier", 30, "bold"))
"""
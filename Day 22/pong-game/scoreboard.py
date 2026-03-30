from turtle import Turtle

class Scoreboard(Turtle):

    # create scoreboard
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # update scores
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # count left player points
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # count right player points
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
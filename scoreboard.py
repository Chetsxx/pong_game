from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.l_score}", False, align="center", font=("Arial", 25, "bold"))
        self.goto(100, 250)
        self.write(f"{self.r_score}", False, align="center", font=("Arial", 25, "bold"))
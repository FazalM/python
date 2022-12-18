from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0,280)
        self.write_to_screen()
        self.hideturtle()

    def write_to_screen(self):
        self.write(f"score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def add_score(self):
        self.score = self.score + 1
        self.clear()
        self.write_to_screen()

        

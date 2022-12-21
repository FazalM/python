from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.write_to_screen()
    
    def add_p1_score(self):
        self.clear()
        self.right_score += 1
        self.write_to_screen()

    def add_p2_score(self):
        self.clear()
        self.left_score += 1
        self.write_to_screen()

    def write_to_screen(self):
        self.goto(-60, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(60, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def end_game(self):
        self.goto(0, 0)
        if self.left_score > self.right_score:
            self.write("Player 2 wins!", align="center", font=("Courier", 80, "normal"))
        else:
            self.write("Player 1 wins!", align="center", font=("Courier", 80, "normal"))


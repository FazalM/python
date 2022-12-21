from turtle import Turtle
from random import randint
import time

class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.speed = 3
        self.shape("circle")
        self.color("white")
        self.goto(x, y)
        self.right(randint(3,10))
    
    def move_ball(self):
        self.forward(self.speed)
        self.goto(round(self.xcor(),0),self.ycor())

    def speed_up(self):
        if self.speed < 15:
            self.speed += 0.5
        self.right(randint(-1,1))

    def ball_bounce(self):
        self.setheading((self.heading() +180) - (self.heading() *2))

    def boundary_bounce(self):
        self.setheading((360-(self.heading()*2))+self.heading())

    def reset(self):
        time.sleep(0.5)
        self.speed = 3
        self.goto(0,0)
        self.color("white")
        self.setheading(0)
        self.right(randint(3,10))
        

        
        




from turtle import Turtle, Screen
import random

class Food():
    
    def __init__(self):
        self.food_locationx = 0
        self.food_locationy = 0
        self.food = Turtle()
        self.food.penup()
        self.food.shape("circle")
        self.food.color("white")
    
    def food_position(self,x,y):
        self.food.goto(x*20,y*20)
        self.food_locationx = self.food.xcor()
        self.food_locationy = self.food.ycor()






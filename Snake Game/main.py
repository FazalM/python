from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random


screen_height = 600
screen_width = 600
screen = Screen()
screen.tracer(0)
screen.setup(screen_width, screen_height)
screen.bgcolor("black")
Size_Of_Block = 20
border_min_x = screen_width/2*-1+Size_Of_Block
border_max_x = screen_width/2-Size_Of_Block
border_min_y = screen_height/2*-1+Size_Of_Block
border_max_y = screen_height/2-Size_Of_Block

print(border_min_x, border_max_x, border_min_y, border_max_y)


s = Snake()
new_food = Food()
def new_food_location():
    new_food.food_position(random.randint(border_min_x/Size_Of_Block,border_max_x/Size_Of_Block),random.randint(border_min_y/Size_Of_Block,border_max_y/Size_Of_Block))
new_food_location()
sb = Scoreboard()

game_on = True
while game_on:
    screen.listen()
    screen.onkey(s.up,"Up")
    screen.onkey(s.down,"Down")
    screen.onkey(s.left,"Left")
    screen.onkey(s.right,"Right")
    
    head_position = (s.segment[0].xcor(), s.segment[0].ycor())
    print(f"if statement is not working: {(head_position)},and {(new_food.food_locationx, new_food.food_locationy)}")

    while (new_food.food_locationx, new_food.food_locationy) == (head_position):
        new_food_location()
        sb.add_score()
        s.add_segment()

        print(f"if statement is working: {(head_position)},and {(new_food.food_locationx, new_food.food_locationy)}")
    
    time.sleep(0.1)
    s.move_snake()
    screen.update()
    if s.segment[0].xcor() < border_min_x or s.segment[0].xcor() > border_max_x or s.segment[0].ycor() < border_min_y or s.segment[0].ycor() > border_max_y:
        game_on = False
    for x in range(1,len(s.segment),1):
        if (s.segment[x].xcor(),s.segment[x].ycor()) == (s.segment[0].xcor(),s.segment[0].ycor()):
            game_on = False
    
screen.exitonclick()

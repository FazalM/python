from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_SIZE_X = 800
SCREEN_SIZE_Y = 600

BOUNDARY_X = SCREEN_SIZE_X/2 - 20
BOUNDARY_Y = SCREEN_SIZE_Y/2 - 20

ball_speed = 1

screen = Screen()
screen.title("Pong")
screen.setup(SCREEN_SIZE_X,SCREEN_SIZE_Y)
screen.bgcolor("black")
screen.tracer(0)

player_one = Paddle(SCREEN_SIZE_X/2-50,0)
player_two = Paddle((SCREEN_SIZE_X/2-50)*-1,0)

score = Scoreboard()

b = Ball(0,0)

screen.listen()
screen.onkey(player_one.up,"Up")
screen.onkey(player_one.down,"Down")

screen.onkey(player_two.up,"w")
screen.onkey(player_two.down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    b.move_ball()

    player_one_x1 = player_one.xcor() - 20
    player_one_x2 = player_one.xcor() + 10
    player_two_x1 = player_two.xcor() + 20
    player_two_x2 = player_two.xcor() - 10

    player_one_y1 = player_one.ycor() + 40
    player_one_y2 = player_one.ycor() - 40
    player_two_y1 = player_two.ycor() + 40
    player_two_y2 = player_two.ycor() - 40
    
    if b.ycor() > player_one_y2 and b.ycor() < player_one_y1:
        if b.xcor() > player_one_x1 and b.xcor() < player_one_x2:
            b.ball_bounce()
            b.speed_up()
            print(b.speed)

    if b.ycor() > player_two_y2 and b.ycor() < player_two_y1:   
        if b.xcor() < player_two_x1 and b.xcor() > player_two_x2:
            b.ball_bounce()
            b.speed_up()
            print(b.speed)

    if b.ycor() > BOUNDARY_Y or b.ycor() < -BOUNDARY_Y:
        b.boundary_bounce()

    if b.xcor() > BOUNDARY_X:
        score.add_p2_score()
        b.reset()
    elif b.xcor() < BOUNDARY_X *-1:
        score.add_p1_score()
        b.reset()

    if score.left_score == 10 or score.right_score == 10:
        game_is_on = False
        score.end_game()

    







screen.exitonclick()
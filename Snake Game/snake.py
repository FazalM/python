from turtle import Turtle

START_POSITION = [(0,0),(-20,0),(-40,0)]
class Snake:

    def __init__(self):
        self.segment = []
        self.start_game()
    
    def start_game(self):
        for x in range(3):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.goto(START_POSITION[x])
            self.segment.append(new_segment)

    def move_snake(self):
        seg_length = len(self.segment)-1
        for x in range(len(self.segment)-1,-1,-1):
            if x > 0:
                new_pos = (self.segment[x-1].xcor(),self.segment[x-1].ycor())
                self.segment[x].goto(new_pos)
            else:
                self.segment[x].forward(20)
                self.s_headx = round(self.segment[x].xcor(),0)
                self.s_heady = round(self.segment[x].ycor(),0)
                self.segment[0].goto(self.s_headx, self.s_heady)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(self.segment[len(self.segment)-1].xcor,self.segment[len(self.segment)-1].ycor)
        self.segment.append(new_segment)

    def up(self):
        if self.segment[0].heading() == 270:
            pass
        else:
            self.segment[0].setheading(90)
    def down(self):
        if self.segment[0].heading() == 90:
            pass
        else:
            self.segment[0].setheading(-90)
    def left(self):
        if self.segment[0].heading() == 0:
            pass
        else:
            self.segment[0].setheading(180)
    def right(self):
        if self.segment[0].heading() == 180:
            pass
        else:
            self.segment[0].setheading(0)
from turtle import Turtle, Screen
from random import randint

#choose your winning turtle
bet = input("Pick the colour of the turtle you think will win ('red','blue','green','purple','orange'): ")

turtle_list = [] #store all the turtle objects
turtle_colour = ["red","blue","green","purple","orange"] #store the colours to auto assign
turtle_start_position_y = [0,100,200,-100,-200] # store the auto start positions
winner = [] #store the winners in order
pos_y = 0 # to loop through the y position for each object made
colour = 0 # to look through the colours for each turtle created
race_is_on = True #to continue the race until the last turtle finishes
all_turtle_finished = 0 # one this reaches 5 race_is_on will become false

Screen().screensize(600,400,"black") #x, y and background colour

for x in range(5): # create each turtle with their own colour, location and store in list
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(turtle_colour[colour]) # new colour from the list each time
    new_turtle.penup()
    new_turtle.goto(-600,turtle_start_position_y[pos_y]) # new position from the list each time
    new_turtle.pendown()
    turtle_list.append(new_turtle)
    pos_y += 1 # next position for the new turtle
    colour += 1 # next colour for the new turtle

while race_is_on: # continue as long as it is true
    for y in range(5):
        if turtle_list[y].xcor() < 600: # stop racing at 600 (this turtle only)
            turtle_list[y].forward(randint(10,100)) # randomly move forward
            if turtle_list[y].xcor() >= 600: #if I have finished
                print(turtle_list[y].fillcolor()) #print out my colour
                winner.append(turtle_list[y].fillcolor()) #save my colour in tbe winners list
                all_turtle_finished += 1 # add 1 to all_turtle_finished
    if all_turtle_finished == 5: # of I am 5
        race_is_on = False #stop the while loop
        
for z in range(len(winner)): #for all the winners
    print(f"position {z+1} : {winner[z]}") # print them out one by one with their positions

if bet == winner[0]: # did the winner match your choice
    print("You win")
else:
    print("You lose")

Screen().exitonclick() # keep the window open until you close it

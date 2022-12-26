import pandas
import turtle

data_set = {}
guessed_states = []
turn = 0
score = 0

screen = turtle.Screen()
screen.setup(725,491)
screen.title(f"US States Game")
screen.bgpic("blank_states_img.gif")
t = turtle.Turtle()
t.penup()

#open the csv file
states_data = pandas.read_csv("50_states.csv")

#convert all data into a list to work with
states_list = states_data["state"].to_list()

while turn < 50:
    #enter an answer
    answer = screen.textinput(f"US State Game - Attempt:{turn}", "Type in the name of the states you know").title()
    turn += 1
    #check to see if the answer is in the list
    if answer in states_list:
        guessed_states.append(answer)
        #get the coordinates for the answer
        current_state = states_data[states_data["state"] == answer]
        current_state_x, current_state_y = current_state["x"].item(), current_state["y"].item()
        t.goto(current_state_x, current_state_y)
        t.write(answer, align="center", font=("arial", 8, "normal"))
        score += 1
        #print(f"name: {current_state['state'].values[0]} x: {current_state_x} y: {current_state_y}")
        states_list.remove(answer)
    elif answer == "exit" or answer == "Exit":
        print("Exit working")
        missing_states = []
        for each_state in states_list:
            if each_state not in guessed_states:
                missing_states.append(each_state)
        print(f"states you didn't guess are: {missing_states}")
        pandas.DataFrame(missing_states).to_csv("missing_states.csv")
        break

    else:
        pass

#turtle.mainloop()
# Image width = 610 px
# Image height = 715 px

# Get states coordinates buy mouse click 

# def mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(mouse_click_coor)

# turtle.mainloop()

import turtle
import pandas
from scoreboard import Scoreboard
screen=turtle.Screen()
screen.title('Indian States Game')
image="Day25/states.gif"
screen.addshape(image)

screen.setup(height=715,width=610)
turtle.shape(image)


data=pandas.read_csv("Day25\states_data.csv")
state_list=data.state.to_list()
correct_guess=[]
score=0

while len(correct_guess)<28:
    answer=screen.textinput(title=f"{score}/29 States Correct",prompt="What's another state's name? ").title()
    if answer=="Exit":
        remaining_states=[state for state in state_list if state not in correct_guess]
        # remaining_states=[]
        # for state in state_list:
        #     if state not in correct_guess:
        #         remaining_states.append(state)
        remaining_csv=pandas.DataFrame(remaining_states)
        remaining_csv.to_csv("Day25\\notguessed_list.csv")
        break
    elif answer in state_list:
        x = int(data[data.state == answer].x)
        y = int(data[data.state == answer].y)
        Scoreboard(answer,x,y)
        if answer not in correct_guess:
            correct_guess.append(answer)
            score+=1
    elif answer=="Answer":
        for state in state_list:
            if state not in correct_guess:
                x = int(data[data.state == state].x)
                y = int(data[data.state == state].y)
                screen.tracer(0)
                Scoreboard(state,x,y,'red')
                screen.update()
        screen.exitonclick()



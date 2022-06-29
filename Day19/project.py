# Turtle Race

from turtle import Turtle,Screen
import random

color_list=["blue","black","yellow","green","orange","red"]
screen=Screen()

screen.setup(width=500,height=400)
user_choice=screen.textinput(title="Make you Bet",prompt="Which turtle will win the race? Enter a color: ")

turtles=[]


for i in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(color_list[i])

def set_position(turtles):
    y=0
    for i in range(6):
        turtles[i].pu()
        turtles[i].goto(-230,y)
        y+=25
set_position(turtles)


if user_choice:
    isRace = True

def check_winner(color):
    if user_choice==color[0]:
        print(f"You guessed correct {color[0]} Turtle won")
    else:
        print(f"You guessed incorrect {color[0]} Turtle won")


while isRace:
    for turtle in turtles:
        if turtle.xcor()>230:
            check_winner(turtle.color())
            isRace=False
            break
        else:
            turtle.pu()
            turtle.fd(random.randint(1,25))



screen.exitonclick()
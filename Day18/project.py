from turtle import Turtle,Screen
from color import color_list
import random

timmy=Turtle()
timmy.shape('arrow')
screen=Screen()
screen.colormode(255)
timmy.shapesize(0.5,0.5)
timmy.setheading(225)
timmy.pu()
timmy.forward(300)
timmy.setheading(0)
# timmy.goto(-100,-100)
# screen.exitonclick()

# timmy.speed('fast')
# timmy.dot(50,(150,240,80))
# timmy.pu()
# timmy.forward(100)
# timmy.dot(50,(100,240,80))

def turn(angle):
    timmy.left(angle)
    timmy.pu()
    timmy.forward(100)
    timmy.left(angle)

def draw(x_limit,y_limit):
    for y in range(y_limit):
        for x in range(x_limit):
            timmy.dot(50,random.choice(color_list))
            if x < x_limit-1:
                timmy.pu()
                timmy.forward(100)
        if y%2==0:
            if y<y_limit-1:
                turn(90)
        else:
            if y<y_limit-1:
                turn(270)


draw(10,5)
screen.exitonclick()
#Etch-A-Sketch

from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def forward():
    tim.fd(5)
def backward():
    tim.bk(5)
def clockwise():
    angle=tim.heading()+2
    tim.setheading(angle)
def counter_clockwise():
    angle=tim.heading()-2
    tim.setheading(angle)

screen.listen()
screen.onkeypress(key="w",fun=forward)
screen.onkeypress(key="s",fun=backward)
screen.onkeypress(key="a",fun=clockwise)
screen.onkeypress(key="d",fun=counter_clockwise)
screen.onkeypress(key="c",fun=screen.resetscreen)
screen.exitonclick()



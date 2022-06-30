from turtle import Turtle
import random
START_POINTS=[(0,0),(-20,0),(-40,0)]
DIRECTIONS=[0,90,180,270]
FORWARD=20

class Snake:
    def __init__(self) -> None:
        self.my_snake=[]
        self.create_snake()
        self.head=self.my_snake[0]
    
    def create_snake(self):
        for i in range(3):
            self.my_snake.append(Turtle("square"))
            self.my_snake[i].color('white')
            self.my_snake[i].pu()
            self.my_snake[i].setpos(START_POINTS[i])
            # my_turtle[i].speed('slow')

    def move(self):
        angle=random.choice(DIRECTIONS)
        for i in range(len(self.my_snake)-1,0,-1):
            self.my_snake[i].goto(self.my_snake[i-1].position())
    
        # self.my_snake[0].setheading(angle)
        self.head.fd(FORWARD)
    
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)


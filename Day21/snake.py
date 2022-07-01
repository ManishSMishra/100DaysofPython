from turtle import Turtle

START_POINTS=[(0,0),(-20,0),(-40,0)]
DIRECTIONS=[0,90,180,270]
FORWARD=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

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
    
    def add_segment(self):
        new_segment=Turtle("square")
        new_segment.color('white')
        new_segment.pu()
        new_segment.setpos(self.my_snake[-1].position())
        self.my_snake.append(new_segment)



    def move(self):
        for i in range(len(self.my_snake)-1,0,-1):
            self.my_snake[i].goto(self.my_snake[i-1].position())
    
        # self.my_snake[0].setheading(angle)
        self.head.fd(FORWARD)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)


from turtle import Turtle
ALIGNMENT='center'
FONT= ('Arial', 8, 'normal')
class Scoreboard(Turtle):
    def __init__(self,answer,x,y,color='black'):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.pu()
        self.color(color)
        self.goto(x,y)
        self.write(arg=f"{answer}", move=False, align=ALIGNMENT, font=FONT)
        
        
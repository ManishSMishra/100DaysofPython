from turtle import Turtle
FINISH_LINE_Y=280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.start_pos()
        self.setheading(90)
    
    def upside(self):
        self.fd(10)
    
    def start_pos(self):
        self.goto(0,-280)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
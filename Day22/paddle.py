from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,xcor) :
        super().__init__()
        self.shape('square')
        self.pu()
        self.color('white')
        self.goto(xcor,0)
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5, outline=None)
        # self.resizemode("user")
    
    def up(self):
        self.setheading(90)
        if self.ycor() <= 235:
            # print(self.ycor())
            self.fd(20)

    
    def down(self):
        self.setheading(270)
        if self.ycor() >= -210:
            # print(self.ycor())
            self.fd(20)
        
            

from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.color('white')
        self.setheading(45)
        self.move_speed= 0.1
    
    def move(self):       
        self.fd(20)
    
    def check_collision(self):
        if self.heading() == 45 and self.ycor() > 280:
            self.setheading(315)
        elif self.heading() == 135 and self.ycor() > 280:
            self.setheading(225)
        elif self.heading() == 315 and self.ycor() < - 280:
            self.setheading(45)
        elif self.heading() == 225 and self.ycor() < - 280:
            self.setheading(135)
    
    def bounce(self):
        if self.heading()==315:
            self.setheading(225)
        elif self.heading()==45:
            self.setheading(135)
        elif self.heading()==225:
            self.setheading(315)
        elif self.heading()==135:
            self.setheading(45)
        self.move_speed*=0.9
        self.move()
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce()

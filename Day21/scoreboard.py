from turtle import Turtle
ALIGNMENT='center'
FONT= ('Arial', 16, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.pu()
        self.color('white')
        self.goto(0,270)
        self.display_score()
        
    
    def score_tracker(self):
        self.score+=1
        self.display_score()
    
    def display_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
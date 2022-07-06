from turtle import Turtle
ALIGNMENT='center'
FONT= ('Arial', 16, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highest_score=0
        # self.write_toFile()
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
        with open('Day21\high_score.txt') as f:
            self.highest_score=int(f.read())
        self.write(arg=f"Score : {self.score} High Score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.highest_score:
            self.highest_score=self.score
            self.write_toFile()
        self.score=0
        self.display_score()
    
    def write_toFile(self):
        with open('Day21\high_score.txt','w') as f:
            f.write(str(self.highest_score))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
from turtle import Turtle
import random
colors=['green','orange','red','blue','yellow','purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Obstacles:
    def __init__(self):
        self.wall=[]
        self.car_speed = STARTING_MOVE_DISTANCE
        # self.generate_obs()
    
    def generate_obs(self):
        delay=random.randint(1,6)
        if delay==1:
            my_wall=Turtle('square')
            my_wall.shapesize(stretch_wid=1, stretch_len=2)
            my_wall.pu()
            my_wall.color(random.choice(colors))
            ycor=random.randint(-250,250)
            my_wall.goto(300,ycor)
            self.wall.append(my_wall)
            
    
    def move(self):
        for walls in self.wall:
            walls.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
# Snake Game : Part1
from turtle import Screen,Turtle

import time
from snake import Snake
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) # Set tracer off

snake=Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

    


game=True

directions=[0,90,180,270]
while game:
    # screen.onkey(snake.up,"Up")
    screen.update()
    time.sleep(0.1)
    
    snake.move()
        

screen.exitonclick()
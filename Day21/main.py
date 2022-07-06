# Snake Game : Part2
from turtle import Screen

import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) # Set tracer off

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

    


game=True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.score_tracker()
        snake.add_segment()
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        # scoreboard.game_over()
        # game=False 
        scoreboard.reset()
        snake.reset()
    for segment in snake.my_snake[1:]:
        if snake.head.distance(segment) < 10:
            # scoreboard.game_over()
            # game=False 
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
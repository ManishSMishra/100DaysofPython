# Ping Pong Game

from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

padr=Paddle(350)
padl=Paddle(-350)
scorel=Scoreboard(-40)
scorer=Scoreboard(40)
ball=Ball()

screen.update()
screen.listen()
screen.onkeypress(padr.up,"Up")
screen.onkeypress(padr.down,"Down")
screen.onkeypress(padl.up,"w")
screen.onkeypress(padl.down,"s")


game=True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.check_collision()
    if ball.xcor() > 340 and ball.distance(padr)<50:
        ball.bounce()

        
    elif ball.xcor() < - 340 and  ball.distance(padl)<50:
        ball.bounce()

        
    if ball.xcor() > 355:
        scorel.score_tracker()
        ball.reset_position()
    elif ball.xcor() < -355:
        # scorel.game_over()
        ball.reset_position()
        scorer.score_tracker()
        # game=False
    
    

    # pad=Paddle()








screen.exitonclick()
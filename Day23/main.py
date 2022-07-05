# Road Cross Game
from turtle import Screen
from player import Player
from obstacles import Obstacles
import time
from scoreboard import Scoreboard

screen=Screen()
screen.setup(height=600,width=600)
screen.tracer(0)
screen.bgcolor('white')

my_player=Player()
obs=Obstacles()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(my_player.upside,"Up")
# screen.onkeypress(my_player.down,"Down")






game=True
while game:
    time.sleep(0.1)
    screen.update()

    obs.generate_obs()
    obs.move()

    for walls in obs.wall:
        if walls.distance(my_player) < 20:
            print("False")
            game=False
            scoreboard.game_over()
        # else:
    
    if my_player.is_at_finish_line():
        my_player.start_pos()
        obs.level_up()
        scoreboard.increase_level()

    



screen.exitonclick()
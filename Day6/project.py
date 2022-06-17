# My version

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not is_facing_north():
    turn_left()
while front_is_clear():
    move()
   
   
while not at_goal():
    if front_is_clear() and right_is_clear():
        while not is_facing_north():
            turn_left()
        if front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
            move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


# Instructor Version

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()
   
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
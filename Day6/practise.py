# Functions:

def my_function():
    print("Something")
    print("Another Line")

my_function()

# link for Practise

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# Solution for both below levels:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

def turn_around():
        turn_left()
        turn_left()
        turn_left()
def hurdle():
        move()
        turn_left()
        move()
        turn_around()
        move()
        turn_around()
        move()
        turn_left()
    
while not at_goal():
        hurdle()


# for variable wall steps:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_around():
        turn_left()
        turn_left()
        turn_left()
def hurdle():
        turn_left()
        move()
        turn_around()
        move()
        turn_around()
        move()
        turn_left()
    
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()

# Hurdle 4
# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_around():
        turn_left()
        turn_left()
        turn_left()
def hurdle():
        turn_around()
        move()
        turn_around()
        move()


    
while not at_goal():
    if front_is_clear() and not right_is_clear():
        move()
    elif not front_is_clear() and not right_is_clear():
        turn_left()
    else:
        hurdle()
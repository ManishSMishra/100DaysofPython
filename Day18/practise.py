from turtle import Screen, Turtle


timmy= Turtle()

timmy.shape("turtle")
timmy.color("red")

# Make a square
# for i in range(0,4):
#     timmy.forward(100)
#     timmy.left(90)

# # draw Dashed line
# for i in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# Draw Polygon

# screen = Screen()
# screen.colormode(255)
# # screen.exitonclick()

# angle=0
# import random
# for i in range (3,11):
#     angle=round(360/i,2)
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     timmy.pencolor((r,g,b))
#     for num in range(0,i):
#         timmy.forward(100)
#         timmy.right(angle)

# Random Walk

# angle=[0,90,180,270]
# import random

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# screen = Screen()
# screen.colormode(255)
# # screen.exitonclick()
# timmy.pensize(10)
# while True:
#     rand_angle=random.choice(angle)
#     timmy.pencolor(random_color())
#     timmy.forward(40)
#     timmy.right(rand_angle)

# Spirograph

import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

timmy.speed('fastest')
timmy.shape('arrow')
screen = Screen()
screen.colormode(255)
def draw_spirograph(gap):
    angle=0
    while angle<360:
        timmy.pencolor(random_color())
        timmy.setheading(angle)
        timmy.circle(100)
        angle+=gap

draw_spirograph(3)
screen.exitonclick()
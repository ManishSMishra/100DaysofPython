# functions:




def greet(Name,Location):
    print(f"Hello {Name}")
    print("Welcome")
    print(f"How's weather in {Location}")

greet(Location="Bhayandar",Name="Manish")

# Surface area calculator:
import math
def paint_calc(height,width,cover):
    cans = (math.ceil((height*width)/cover))
    print(f"You will need {cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# prime number checker
def prime_checker(number):
    if number in [1,2,3,5,7]:
        print(f"{number} is a Prime Number")
    elif number%2 ==0 or number%3==0 or number%5==0 or number%7==0:
        print(f"{number} is not a Prime Number")
    else:
        print(f"{number} is a Prime Number")


n = int(input("Check this number: "))
prime_checker(number=n)



# Control Flow and Logical Operaors:
# > , < , >= , <= , == , != 

# odd even :

# number = int(input("Enter number you want to check? "))

# if number % 2 ==0:
#     print(f"{number} is an Even number")
# else:
#     print(f"{number} is an Odd number")

# BMI Calculator:

# height = float(input("Enter your weight in m: "))
# weight = float(input("Enter your weight in Kgs: "))

# BMI = weight/height**2
# # math.floor() ; math.ceil()

# if BMI <= 18.5:
#     print("Underweight")
# elif BMI <=25:
#     print("normal weight")
# elif BMI <=30:
#     print("Overweight")
# elif BMI<=35:
#     print("Obese")
# else:
#     print("Clinically Obese")
# print(round(BMI))

## LEAP YEAR:

# year = int(input("Enter the year you want to check for leap year: "))

# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(f"{year} is a Leap Year")
#         else:
#             print(f"{year} is not a leap Year")
#     else:
#         print(f"{year} is a Leap Year")
# else:
#     print(f"{year} is not a leap Year")

# Pizza toppings:

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == 'S':
    bill = 15
    if add_pepperoni=='Y':
        bill+=2
elif size =='M':
    bill= 20
    if add_pepperoni=='Y':
        bill+=3
else:
    bill=25
    if add_pepperoni=='Y':
        bill+=3

if extra_cheese=='Y':
    bill+=1

print(f" You totala payout amount is: {bill}")


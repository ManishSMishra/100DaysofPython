# Data Types

    # Strings : "Hello"[0] -> H

    # Integer : 1234
    
    # Float : 10.3245

    # Boolean : True / False

# type conversion

# str() ; int () ; float ()

# Sum do two digit number:

# number = input("Enter two digit number: ")
# print(int(number[0]) / int(number[1]))

# Math operation : + , - , * , / (give floating point) , ** to the power, PEMD(left to right)AS , // , %

# BMI Calculator



height = float(input("Enter your weight in m: "))
weight = float(input("Enter your weight in Kgs: "))

BMI = weight/height**2
# math.floor() ; math.ceil()
print(round(BMI))

# # Life in week

age = int(input("enter your age in years: "))
years_left = 90 - age
month = years_left * 12
days = years_left * 365
weeks = years_left * 52

print(f"You have {days} Days , {weeks} Weeks, {month} Months left.")
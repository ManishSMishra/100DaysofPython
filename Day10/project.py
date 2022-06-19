# Calculator 


import os
from art import logo

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

print(logo)
operation={'+': add,'-': subtract , '*' : multiply , '/' : divide}

isCalculate=True

first_no=int(input("What's the first number?: "))
while isCalculate:
    choice=input("Pick an operation: \n+ \n-\n*\n/\n")
    if choice not in operation.keys():
        print("Invalid Operation")
        print("Type again")
        continue
    else:
        second_no=int(input("Enter Next number: "))
        first_no=operation[choice](first_no,second_no)
        print(f"Value: {first_no:.2f}")
    isPlay=input(f"Type 'y' to keep calculating with {first_no:.2f}, or 'n' to start a new calculation, 's' to stop ").lower()
    if isPlay=='y':
        continue
    elif isPlay=='n':
        os.system('cls')
        print(logo)
        first_no=int(input("What's the first number?: "))
    else:
        break


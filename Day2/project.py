# Tip Calculator
print("Welcome to Tip calculator.")
bill_amount = float(input("What was the total bill amount? "))
tip = float(input("What tip percentage would you like to give? "))
total_person = int(input("How many people to split the bill? "))

total_amount = bill_amount + (tip/100)*bill_amount
per_person= total_amount/total_person

print(f"Each person should pay: $ {per_person:.2f}")

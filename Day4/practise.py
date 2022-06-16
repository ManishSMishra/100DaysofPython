# Randomization and Lists

import random

# random.randint(1,100)
# print(random.random()) # range is 0 to 1 not including 1 

# Coins toss:

toss = random.randint(0,1)
if toss== 0:
    print("Head")
else:
    print("Tails")

# LISTS
States = ["MH","UP","AP","TN","KR"]

States.append("BH")
States.extend(["JK","MZ","PB"])
print(States)
print(States[-1])

# Roulette

names = input("enter list of name separeted by comma: ")
name_list = names.split(",")
payee = name_list[random.randint(0,len(name_list)-1)]
print(name_list)

# can use 
# print(random.choice(name_list))
print(f" {payee} pays the Bill")

# nested lists
States = ["MH","UP","AP","TN","KR"]
names = ['Manish', 'Rohan', 'Yusuf', 'Pavitr']
combined= [States,names]
print(combined)

# Treasure Map

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
column = int(position[0]) - 1
row = int(position[1]) - 1
map[row][column]="X"
print(f"{row1}\n{row2}\n{row3}")
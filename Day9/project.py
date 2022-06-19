# Secret Auction
import os
from art import logo
print(logo)
print("welcome to secret acution")

isNext=True
bids=[]
def highest_bidder(bids):
    highest=0
    bidder_name=""
    for i in bids:
            if i['bid']>highest:
                highest=i['bid']
                bidder_name=i['name']

    print(f"The winner is {bidder_name} with a winning bid of {highest}$ ")

while isNext:
    name= input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids.append({'name':name,'bid':bid})
    choice=input("Are there any other bidders? Type 'Y' or 'N'.\n").lower()
    os.system('cls')
    if choice != 'y':
        isNext=False
        highest_bidder(bids)
    

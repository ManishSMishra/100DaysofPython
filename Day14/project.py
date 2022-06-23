from appdata import data 
from art import logo,vs
import os
score=0
def compare(user_choice,comp_choice):
    global score
    if user_choice['follower_count']> comp_choice['follower_count']:
        score+=1
        return True
    else:
        return False

def game():
    isGame=True
    global score
    while isGame:
        for i in range(0,len(data)-1):
            os.system('clear')
            print(logo)
            print(f"Compare A: {data[i]['name']}, a {data[i]['description']}, from {data[i]['country']}.")
            print(vs)
            print(f"Compare B: {data[i+1]['name']}, a {data[i+1]['description']}, from {data[i+1]['country']}.")
            choice=input("Who has more followers? Type 'A' or 'B':").lower()
            if choice=='a':
                return_value = compare(data[i],data[i+1])
            else:
                return_value = compare(data[i+1],data[i])
            if return_value:
                if i+2 == len(data):
                    print(f"You Won!, Final Score: {score}")
                    break
                else:
                    print(f"You Guessed Correct. Current Score: {score}")
                    continue
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                break
        isGame=False
            


game()



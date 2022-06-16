import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
printing= {'r': rock , 'p' :paper , 's' : scissors}

#Write your code below this line 👇

print("Welcome to ROCK, Paper, Scissors game! ")
user_choice = input("Choose R for Rock, S for Scissors, P for Paper: ").lower()
computer_choice = random.choice(['r','p','s'])
# print(user_choice)
# print(computer_choice)

if user_choice== computer_choice:
    print(f"User choice: \n {printing[user_choice]}")
    print(f"Computer choice:  \n {printing[computer_choice]}")
    print("Draw")
elif (user_choice=='r' and computer_choice=='s') or (user_choice=='s' and computer_choice=='p') or (user_choice=='p' and computer_choice=='r'):
    print(f"User choice: \n {printing[user_choice]}")
    print(f"Computer choice:  \n {printing[computer_choice]}")
    print("You Won")
elif(user_choice=='s' and computer_choice=='r') or (user_choice=='p' and computer_choice=='s') or (user_choice=='r' and computer_choice=='p'):
    print(f"User choice: \n {printing[user_choice]}")
    print(f"Computer choice:  \n {printing[computer_choice]}")
    print("Computer won")
else:
    print("Opps! you gave a wrong input")



import random
from hangmanart import stages,logo
from wordlist import word_list
import os

word=random.choice(word_list).upper()
word=list(word)
# print(word)

print(logo)
game_word=[]

for i in range(0,len(word)):
    game_word.append('_')


lives=7

while lives>0 and word !=game_word:
    print(' '.join(game_word))
    user_guess= input("\nGuess a letter: ").upper()
    os.system('cls')
    if user_guess in game_word:
        print(f"You've already guessed {user_guess}")
    if user_guess in word:
        for i in range(0,len(word)):
            if user_guess==word[i]:
                game_word[i]=user_guess
    
    else:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        lives-=1
    if len(stages)>lives:    
        print(stages[lives])

if word ==game_word:
    print(' '.join(game_word))
    print("You win.")
else:
    print("You lose. The Word was:")
    print(' '.join(word))


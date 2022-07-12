# NATO phonetic alphabet

import pandas

data = pandas.read_csv("Day26\\nato_phonetic_alphabet.csv")



phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

user_word=list(input("Enter a word: ").upper())

def check(user_word):
    try:
        for word in user_word:
            phonetic_dict[word]
    except:
        print("Sorry, only letters in alphabet please")
        return False
    else:
        return True

while not check(user_word):
    user_word=list(input("Enter a word: ").upper())

nato_list=[phonetic_dict[letter] for letter in user_word]
print(nato_list)
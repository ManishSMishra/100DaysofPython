# NATO phonetic alphabet

import pandas

data = pandas.read_csv("Day26\\nato_phonetic_alphabet.csv")



phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(nato_disct)


user_word=list(input("Enter a word: ").upper())
# print(user_word)

nato_list=[phonetic_dict[letter] for letter in user_word]
print(nato_list)
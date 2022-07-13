from cgitb import text
from email.mime import image
from msilib.schema import File
from tkinter import *
import pandas
import random


HEXCODE='#b5ddc5' 
LANGUAGE_FONT=("Ariel",40,"italic")
WORD_FONT=("Ariel",55,"bold")
known_index_list=[]
window = Tk()
window.title("Flash Card App")
window.config(bg=HEXCODE)
window.config(padx=50,pady=50)
known_words={
    'hindi':[],
    'english':[]
}
unknown_words={
    'hindi':[],
    'english':[]
}


def random_word(answer):
    global my_data
    global my_index
    global hindi_word
    global english_word
    my_data=pandas.read_csv('Day31\\unknown_data.csv',encoding="utf8")
    rows=len(my_data.index)
    my_data_dict=my_data.to_dict()
    my_index=random.randint(0,rows-1)
    if len(known_index_list)!=rows:
        while my_index in known_index_list:
            my_index=random.randint(0,rows-1)
            print("trye")
    else:
        print("exiting")
        return False
    hindi_word=my_data_dict['hindi'][my_index]
    english_word=my_data_dict['english'][my_index]
    bg.itemconfigure(word_text,text=hindi_word)
    bg.itemconfigure(language_text,text="Hindi")
    window.after(3000,reveal_translation)
    if answer=='yes':
        known_words['hindi'].append(hindi_word)
        known_words['english'].append(english_word)
        know_data=pandas.DataFrame(known_words)
        know_data.to_csv('Day31\known_data.csv',encoding="utf8")
        known_index_list.append(my_index)
        print(my_index)
        print(known_index_list)
        my_data=my_data.drop(my_data.index[my_index])
        my_data.to_csv('Day31\\unknown_data.csv',encoding="utf8",index=False)
    else:
        unknown_words['hindi'].append(hindi_word)
        unknown_words['english'].append(english_word)
        unknow_data=pandas.DataFrame(unknown_words)
        unknow_data.to_csv('Day31\\unknown_data.csv',encoding="utf8")
    
def reveal_translation():
    bg.itemconfigure(word_text,text=english_word,fill='white')
    bg.itemconfigure(image_container,image=fg_image)
    bg.itemconfigure(language_text,text="English",fill='white')


################### CANCVAS #######################

bg_image=PhotoImage(file="Day31\images\card_front.png")
fg_image=PhotoImage(file="Day31\images\card_back.png")
bg=Canvas(height=526,width=800,highlightthickness=0,bg=HEXCODE)
image_container=bg.create_image(400,263,image=bg_image)
language_text=bg.create_text(400,150,text="Hindi",fill='black',font=LANGUAGE_FONT)
word_text=bg.create_text(400,263,text="राम",fill='black',font=WORD_FONT)
bg.grid(row=0, column=0,columnspan=3)


################ BUTTON #################
# Right Button
right_image = PhotoImage(file="Day31\images\\right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=HEXCODE, command=lambda:random_word('yes'))
right_button.grid(row=1, column=0)

# Left Button
wrong_image = PhotoImage(file="Day31\images\\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0 , bg=HEXCODE, command=lambda:random_word('no'))
wrong_button.grid(row=1, column=2)

window.mainloop()




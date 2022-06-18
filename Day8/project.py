from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text,shift):
    text=list(text)
    for i in range(0,len(text)):
        if text[i] in alphabet:
            index_value=(alphabet.index(text[i])+shift)%26
            if index_value>26:
                index_value=index_value-26
            text[i]=alphabet[index_value]
    print(''.join(text))



def decrypt(text,shift):
    text=list(text)
    for i in range(0,len(text)):
        if text[i] in alphabet:
            index_value=(alphabet.index(text[i])-shift)%26
            if index_value<0:
                text[i]=alphabet[-shift]
            text[i]=alphabet[index_value]
    print(''.join(text))   

print(logo)
isYes=True
while isYes:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text=text,shift=shift)
    elif direction == 'decode':
        decrypt(text=text,shift=shift)
    else:
        print("You typed wrong Direction!. Try again")
    choice=input("Type 'yes' if you want to go again. Otherwise type 'no'").lower()
    if choice != "yes":
        isYes=False
        print("GoodBye!")



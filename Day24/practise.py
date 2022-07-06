# File Operations

# file = open('Day24\my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

########### OR ###############

# mode 'a' will append the files that are to be written , mode 'w' will flush the file and add the new lines
with open('Day24\\new_file.txt', mode='a') as file:
    file.write("\nNew text.")
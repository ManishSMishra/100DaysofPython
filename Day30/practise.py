#file not found error
# try:
#     file = open("day30\\a_file.txt")
#     a_dictionay={'key': 'value'}
#     print(a_dictionay['key'])
# except FileNotFoundError: # runs if there is an exception of particular type, in this case if the file is not present this code will run
#     file = open("day30\\a_file.txt","w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exists")
# else: # runs only if there is no exception
#     content=file.read()
#     print(content)
# finally: # This runs no matter what happens
#     raise KeyError("This is a forced Exception")


height=float(input("Enter yout height in meter's: "))
weight= int(input("Enter yout weight in kg's: "))

if height >3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / pow(height,2)
print(bmi)



# basic print function
print("Hello World")
print("One String" + "   " +"Another String")

# input function and varaiables
name = input("What is your name?: ")
# print("Your name contains: {0} ".format(len(name))  )
print("Your name contains: " + str(len(name)) + " Characters" )

# swap variable values:
a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))

a = a + b
b = a - b
a = a - b

print("A: {0} & B: {1}".format(a,b))
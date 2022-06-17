# For loops

my_list=["manish","mishra","pavitra","rohan","yusuf"]
for item in my_list:
    print(item)
    print(item + " Gupta")

# Average Heights:

height=[180,120,164,178,116,134,185]
heights=input("enter student heights")
height_list = heights.split(",")
sum=0
count=0
for i in height_list:
    sum+=int(i)
    count+=1
print(f"Average height is {round(sum/count)}")

# easy way : sum(list_name) and len(list_name)

# highest Score
score = input("Enter Students score: ").split(",")
for i in range(0,len(score)):
    score[i]=int(score[i])
print(score)

highest=0
for i in range(0,len(score)-1):
    if score[i]>score[i+1]:
        highest=score[i]
    else:
        highest=score[i+1]

print(f"Highest Score= {highest}")

# easy way: min() ; max()

# Range function:
sum=0
for i in range(2,101,2):
    sum += i
print(sum)

# FizzBuzz

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
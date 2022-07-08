

# List Comprehension example
# with open("Day26/file1.txt") as f1:
#     file1_data=f1.readlines()
# with open("Day26/file2.txt") as f2:
#     file2_data=f2.readlines()

# file1_data=[item.strip() for item in file1_data]
# file2_data=[item.strip() for item in file2_data]

# common_num=[int(item) for item in file2_data if item in file1_data]
# print(file1_data)
# print(file2_data)
# print(common_num)

# dictionary comprehension example

# new_dict= {key:value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# names=["Manish","Yusuf","Rohan"]

# import random

# new_dict={name:random.randint(1,100) for name in names}
# # passed_student= { key:new_dict[key] for key in new_dict.keys() if new_dict[key]>=60 }
# ### OR ###
# passed_student= { student:score for (student,score) in new_dict.items() if score >= 60 }
# print(new_dict)
# print(passed_student)


# Exercise 1: 

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# result = {word:len(word) for word in sentence.split(' ')}

# print(result)

# Exercise 2: 

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# weather_f = {key:(value*1.8)+32 for (key,value) in weather_c.items()}
# print(weather_f)

# loop through data frame

import pandas

student_dict ={
    'names' : ['Manish','Yusuf',"Rohan",'Srikanth','Shakti'],
    'score' : [80, 82 , 84 , 86, 88 ]
}

student_df=pandas.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    print(row.names, row.score)
print(student_df)
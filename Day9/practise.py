#dictionary

# my_dict={"I":1 , "V":5}
# print(my_dict)
# my_dict["X"]=10
# print(my_dict)


# # my_dict = {}
# # print(my_dict)

# my_keys=my_dict.keys()
# print(my_keys)

# ####Grade ##########

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades={}


# #TODO-2: Write your code below to add the grades to student_grades.👇
# for keys in student_scores:
#     if student_scores[keys]>90:
#         student_grades[keys]="Outstanding"
#     elif student_scores[keys]>80:
#         student_grades[keys]="Exceeds Expectations"
#     elif student_scores[keys]>70:
#         student_grades[keys]="Acceptable"
#     else:
#         student_grades[keys]="Fail"
# # 🚨 Don't change the code below 👇
# print(student_grades)


# Nesting List in Dictionary


# travel_log=[
#     {
#     "country":"France", 
#     'cities_visited':["Paris","Monaco","Lille","Dijon"],
#     "total_visited":12
#     },
#     {
#         "country":"Germany",
#         'cities_visited':["Berlin","Hamburg","Stuttgart"],
#         "total_visited":5
#     }

# ]

# print(travel_log['Germany']['cities_visited'])
# # nesting Dictionary in Dictionary:

# travel_log


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
new_country={}
def add_new_country(country,visits,cities):
    new_country={}
    new_country['country']=country
    new_country['visits']=visits
    new_country['cities']=cities
    travel_log.append(new_country)
    print(travel_log)





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)




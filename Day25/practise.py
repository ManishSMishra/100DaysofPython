# Pandas

# with open("Day25/weather_data.csv") as data:
#     print(data.readlines())

# import csv

# with open("Day25/weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data= pandas.read_csv("Day25/weather_data.csv")
# print(data)
# get data by column name
# print(data["temp"])
######## OR #############
# print(data.condition)
# pandas uses two datatype Series (1-D) and Dataframe (2-D)
# print(type(data)) 

# convert to data dictionary
# data_dict = data.to_dict()
# print(data_dict)

# convert data series to List
# temp_list=data["temp"].to_list()
# print(temp_list)

# get max value
# print(data["temp"].max())

# # print(data["condition"])
# print(data.condition)

# # get data in a row

# print(data[data.temp == data.temp.max()])

# # get a row with a condition where row day= Monday
# monday=data[data.day=="Monday"]
# mon_temp=(monday.temp*1.8)+32
# print(int(mon_temp))

# create a dataframe

data_dict= {
    "students" : ["Manish", "Rohan", "Yusuf"],
    "scores"   : [100,100,100]

}

data = pandas.DataFrame(data_dict)
data.to_csv("Day25\\newdata.csv")
print(data)
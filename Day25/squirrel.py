import pandas

data = pandas.read_csv("Day25\squirrel_data.csv")


gray_squir= len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squir= len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squir= len(data[data["Primary Fur Color"]=="Black"])

data_dict ={}

# print(type(grey_squir))

data_dict["Fur color"] = ['Gray','Cinnamon','Black']
data_dict['Count'] = [gray_squir,cinnamon_squir,black_squir]

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Day25\squirrel_count.csv")
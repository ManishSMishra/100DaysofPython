# OOP

import turtle


# timmy = turtle.Turtle()
# myScreen = turtle.Screen()
# timmy.shape("turtle")
# print(myScreen.canvheight)
# timmy.forward(100)
# myScreen.exitonclick()

import prettytable

table=prettytable.PrettyTable()

table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
print(table)
pokemon_table=prettytable.PrettyTable()

pokemon_table.add_column("Name",["Spearow","Raticate","Vulpix","Oddish"])
pokemon_table.add_column("Type",["Flying","Normal","Fire","Grass"])
pokemon_table.align='l'
print(pokemon_table)
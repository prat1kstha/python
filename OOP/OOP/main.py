# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
#
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()

# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Bulbasaur", "Grass"])
# table.add_row(["Charmandar", "Fire"])


table.add_column("Pokemon Name", ["Pikachu", "Bulbasaur", "Charmandar"])
table.add_column("Type", ["Electric", "Grass", "Fire"])
table.align = "l"
print(table)
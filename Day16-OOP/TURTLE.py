# from turtle import Turtle,Screen
#
#
# nina = Turtle()
# nina.color("cyan")
# nina.shape("turtle")
# nina.forward(120)
# print(nina)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
import sqlite3
table = PrettyTable()
table.field_names = ["Pokeman", "Type"]
table.add_rows([["Pikachu", "ELECTRIC"],["Sqirtle", "WATER"],
              ["Charmander", "FIRE"]])
table.align = "l"

print(table)




# from turtle import Turtle,Screen
# colors=['blue','green','orange','red','white','gray']
# my_turtle=Turtle()
# my_turtle.shape('turtle')
# my_turtle.color('chartreuse2')
# for i in colors:
#     my_turtle.color(i)
#     my_turtle.forward(100)
#     my_turtle.left(90)
#     my_turtle.forward(100)
#     my_turtle.left(90)
#     my_turtle.home()
#
# print(my_turtle)
#
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon Name",['pikachu','squirtie','charmander'])
table.add_column("Type",['electric','Water','Fire'])
table.add_column("power rating",[1,5,3])
table.add_row(["another pikachu",'land',7])
table.align='l'
table.border=True
table.header=True
print(table.get_string(sortby='power rating',reversesort=True))
# print(string,type(string))
print(table.align)
print(table,type(table))
print(table)
print(dir(table))

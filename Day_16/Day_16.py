# from turtle import Turtle, Screen

# jack = Turtle()
# print(jack)
# jack.shape('turtle')
# jack.color('chartreuse3')
# jack.forward(100)

# screen = Screen()
# print(screen.canvheight)

# screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ['Pokemon Names', 'Pokemon Types']

# table.add_row(['Pikachu', 'Electric'])
# table.add_row(['Squirtle', 'Water'])
# table.add_row(['Charmander', 'Fire'])

table.add_column('Pokemon Name', ['Pikachu', 'Raichu', 'Squirtle', 'Wartotle', 'Blastoise', 'Bulbasaur', 'Ivysaur', 'Venasaur', 'Charmander', 'Charmeleon', 'Charizard'])
table.add_column('Type', ['Electric', 'Electric', 'Water', 'Water', 'Water', 'Grass', 'Grass', 'Grass', 'Fire', 'Fire', 'Fire'])


table.align = 'l'


print(table)


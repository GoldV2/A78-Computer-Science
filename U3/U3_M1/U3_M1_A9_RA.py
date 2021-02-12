# Program name: U1_M1_A1_RA.py
# Program purpose: string formatting and "in" keyword
# Created/revised: R. Almeida on 10-15-20

# 3
print('ms. Borwning is in her office.'.capitalize())

# 4
favColor = 'yELLow'
print(favColor.capitalize())
print(favColor.upper())
print(favColor.lower())
print(favColor)

# 5
favFood = input('What is your favorite food?\n\n>>> ')
print(favFood.capitalize())
print(favFood.upper())
print(favFood.lower())
print(favFood.swapcase())

# 7
print(input('Input a color in all caps').lower())

# 8
fastAnimal = input('The name of a fast animal\n\n>>> ')
print(fastAnimal.upper())

# 10
menu = 'salad, pasta, sandwich, pizza, drinks, desserts'
print('Pizza' in menu)
print('pizza' in menu)

# 11
greeting = "Hello, World!"
print("'hello is found in greeting = ", 'hello' in greeting.lower())

# 12
greeting = "Hello, World!"
print("'HELLO' is found in greeting  =", 'HELLO'.lower() in greeting.lower())
print("’hello’ is found in greeting =", 'hello' in greeting)

# 13
menu = 'salad, pasta, sandwich, pizza, drinks, dessert'
print("'pizza' in menu =", 'pizza' in menu)
print("'soup' in menu =", 'soup' in menu)
print("'dessert' in menu =", 'dessert' in menu)

# 14
menuAsk = input('What item do you desire to find in the menu?\n\n>>> ')
print(menuAsk, 'is in the menu:', menuAsk in menu)

print('Current menu:', menu)
newItems = input('Add two new items to the menu separates by a comma\n\n>>> ')
menu += ', ' + newItems
print('New menu:', menu)

# 15
menuAsk2 = input('What other item do you desire to find in the menu?\n\n>>> ')
print(menuAsk2, 'is in the menu:', menuAsk2 in menu)

# 16
paintColors = 'red, blue, green, black, orange, pink'
print('Red is found in paint colors =', 'red' in paintColors)

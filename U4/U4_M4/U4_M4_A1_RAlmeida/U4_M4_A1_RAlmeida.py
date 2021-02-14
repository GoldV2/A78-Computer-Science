# File Name: U4_M4_A1_RAlmeida.py
# Purpose: Read Files
# Edited - Revised: 02/14/21

from textwrap import dedent

def task(n, name = ''):
    width = len(name) + 8

    s = f"""
         +{'-'*width}+
         |{f'Task {n}':^{width}}|"""

    if name:
        s += f"""
         |{f' Name: {name}':^{width}}|
         +{'-'*width}+
         """

    else:
        s += f"""
         +{'-'*width}+
         """

    print(dedent(s))

task(1, 'Cities')

# opening file
cities_file = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A1_RAlmeida\\cities.txt', 'r')

task(2)

# reading the file as a string
cities = cities_file.read()
print(cities)

task(3)

# opening file
pi_file = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A1_RAlmeida\\digits_of_pie.txt', 'r')

# initizalizing an empty string
pi_digits = ''
# loop for 6 times
for i in range(6):
    # read 4 characters every iteration and add them to pi_digits
    pi_digits += pi_file.read(4)

# printing pi_digits
print(pi_digits)
# finding the amount of chars and subtracting one to remove the period
print(len(pi_digits)-1)

pi_file.close()

task(4)

# initializing empty string
initials = ''
# iterating through every character in cities
for char in cities:
    # checking if the character is uppercase or is a new line character
    if char.isupper() or char == '\n':
        # if it is either add that to the empty string
        initials += char

# print file
print(initials)
# close file
cities_file.close()
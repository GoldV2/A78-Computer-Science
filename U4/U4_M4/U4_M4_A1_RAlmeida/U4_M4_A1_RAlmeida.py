# File Name: U4_M4_A1_RAlmeida.py
# Purpose: 
# Edited - Revised: 

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

cities_file = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A1_RAlmeida\\cities.txt', 'r')

task(2)

cities = cities_file.read()
print(cities)

task(3)

pi_file = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A1_RAlmeida\\digits_of_pie.txt', 'r')

pi_digits = ''
for i in range(6):
    pi_digits += pi_file.read(4)

print(pi_digits)
# subtracting one to remove the period
print(len(pi_digits)-1)

pi_file.close()

task(4)

initials = ''
for char in cities:
    if char.isupper() or char == '\n':
        initials += char

print(initials)
cities_file.close()
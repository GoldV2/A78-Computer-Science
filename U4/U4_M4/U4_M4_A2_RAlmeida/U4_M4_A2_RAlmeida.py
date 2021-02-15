# File Name: U4_M4_A2_RAlmeida.py
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

task(1, '.readlines()')

# opening file
cities_file = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A1_RAlmeida\\cities.txt', 'r')
# store each line of the file in a list
cities_lines = cities_file.readlines()
# looping through every lione in cities_line
for line in cities_lines:
     # print every line
     print(line)

task(2, 'remove \\n chars')

# looping through every line in cities_lines
for line in cities_lines:
     # printing every character but the last one, which is a \n character
     print(line[:-1])

task(3, '.close()')

# looping through every line in cities_lines
for line in cities_lines:
     # if line is greater than D
     if line >= 'D':
          # print line
          print(line)

# closing the file
cities_file.close()
try:
     # trying to use readlines() on file
     cities_file.readlines()

# except a ValueError
except ValueError:
     # printing the error
     print('I/O operation on closed file.')

task(4, 'readlines() poem_2')

# opening file
poem_2_file = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A2_RAlmeida\\poem_2.txt', 'r')
# reading every line of the file
poem_2_lines = poem_2_file.readlines()

# looping through the list backwards
for line in poem_2_lines[::-1]:
     # printing every character of each line except the last one which is a \n
     print(line[:-1])
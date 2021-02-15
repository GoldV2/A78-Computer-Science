# File Name: U4_M4_A3_RAlmeida.py
# Purpose: Reading Files
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

task(1, 'Use .readline() to Get Rainbow Colors')

# opening file in read only mode
rainbow_file = open("D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A3_RAlmeida\\rainbow.txt")
# reading the first three lines
color1 = rainbow_file.readline()
color2 = rainbow_file.readline()
color3 = rainbow_file.readline()

# printing each of the first three lines in upper case
print(color1.upper() + color2.upper() + color3.upper())

# closing the file
rainbow_file.close()

task(2, 'While .readline() Rainbow Colors')

# opening the file
rainbow_file = open("D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A3_RAlmeida\\rainbow.txt")
# starting infinite while loop
while True:
     # creating a variable to store the line
     line = rainbow_file.readline().capitalize()
     # check if line is not an empty string
     if line:
          print(line)

     # if it is an empty string, break the loop because that is the last line
     else:
          break

rainbow_file.close()

task(3, 'Strip and Reverse')

# opening the file in read only mode
rainbow_file = open("D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A3_RAlmeida\\rainbow.txt")
# starting infinite while loop
while True:
     # setting line to be equal toa line from rainbow_file, after using strip, and reversing it and converting it to uppercase
     line = rainbow_file.readline().strip()[::-1].upper()
     if line:
          print(line)

     else:
          break

# the instructions for this are not very clear
task(4, '.strip With Arguments')

# opening file in read only mode
cities_file = open("D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A3_RAlmeida\\cities_messy.txt")

while True:
     # stripping colon and new line character from each line
     line = cities_file.readline().strip(':\n')
     # checking if line not is empty
     if line:
          print(line)

     # break the loop if it is empty
     else:
          break

task(5, '.strip() paranthesis from poem_2_messy')

poem2_messy = open("D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A3_RAlmeida\\poem_2_messy.txt")

while True:
     # removing any trailing (, ), and \n
     line = poem2_messy.readline().strip('()\n')
     # checking if the line is not empty
     if line:
          print(line)

     # if it is empty end the loop
     else:
          break
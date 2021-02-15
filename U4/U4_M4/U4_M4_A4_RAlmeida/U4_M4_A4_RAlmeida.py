# File Name: U4_M4_A4_RAlmeida.py
# Purpose: Write Files
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

task(1, 'Create a Local File')

# opening in write and read mode
inner_planets = open("D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A4_RAlmeida\\inner_planets.txt", 'w')
# writing the name of four planets with a new line between each
inner_planets.write('Mercury\nVenus\nEarth\nMars')

# closing the file
inner_planets.close()

# opening in read only mode and reading all the contents of the file
inner_planets = open("D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A4_RAlmeida\\inner_planets.txt")
inner_planets_contents = inner_planets.read()
# printing all the contents of the file
print(inner_planets_contents)

# closing the file again
inner_planets.close()

task(2, 'Using .seek()')

# opening in write and read mode
outer_planets = open("D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A4_RAlmeida\\outer_planets.txt", 'w+')
# writing the name of four planets with a new line character between each
outer_planets.write('Jupiter\nSaturn\nUranus\nNeptune')

# setting the read and write pointer to the beginning of the file
outer_planets.seek(0)

# reading all the conents of the file and saving it to a variable in the form of a string
outer_planets_contents = outer_planets.read()
# printing all the contents of the file
print(outer_planets_contents)

# closing the file
outer_planets.close()

task(3, '.seek() With Optional Whence Argument')

# opening in write and read mode
days = open("D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A4_RAlmeida\\days.txt", 'w+')
# writing the weekdays
days.write('Monday\nTuesday\nWednesday\nThursday\nFriday')

# setting the read and write pointer to the beginning of the file
days.seek(0)
# reading all the contents of the file and saving it to days_content in the form of a string
days_content = days.read()
# printing all the conents of the file
print(days_content)

print('-'*(len('.seek() With Optional Whence Argument')+10))

# setting the read and write pointer to the end of the file
days.seek(0, 2)
# writing the weekend days
days.write('\nSaturday\nSunday')

# setting the read and write pointer to the beginning of the file
days.seek(0)
# reading all the contents of the file
days_content = days.read()
print(days_content)

task(4, 'Append')

# opening file in append plus mode
task4_file = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\U4\\U4_M4\\U4_M4_A4_RAlmeida\\task4.txt', 'a+')

# creating a loop
for item in range(5):
     # when in append plus mode, whenever you write, the pointer always goes to the end of the file
     # first, so even if you set the pointer to the beginning of the file, it makes no difference to
     # where stuff is writtens
     task4_file.write(f'append #{item}\n')
     task4_file.seek(0)

# printing contents
print(task4_file.read())

task4_file.close()
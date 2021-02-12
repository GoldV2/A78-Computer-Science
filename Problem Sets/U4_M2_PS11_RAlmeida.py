# File Name: U4_M2_PS11_RAlmeida.py
# Purpose: Problem Set 11
# Edited - Revised: 01/04/21

from textwrap import dedent

def step(n, name = ''):
    width = 25

    s = f"""
         +{'-'*width}+
         |{f'Step {n}':^{width}}|"""

    if name:
        s += f"""
         |{f'Name: {name}':^{width}}|
         +{'-'*width}+
         """

    else:
        s += f"""
         +{'-'*width}+
         """

    print(dedent(s))

step(4, 'Week Days')

# list with all the days of the week
week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(week_days)

step(5, 'Odd Week Days')

# using list comprehension to print the day in a list formed by
# week_days that starts at index 1 and skips every other item
print([day for day in week_days[1::2]])

step(6, 'Tuesday')

# accessing the third day, Tuesday
day = week_days[2]
print(day)

step(7, 'Day Index 5')

# accesssing the sixth day
day = week_days[5]
print(day)

step(8, 'Rafaday')

week_days.append('Rafaday')
print(week_days)

step(9, 'New Middle Day')

# finding the length of week_days and using whole number division to find the middle index
week_days.insert(len(week_days)//2, 'AlmeidaDay')
print(week_days)

step(10, 'More Weekend')

# using index to find the index of Friday and inserting a new day after it
week_days.insert(week_days.index('Friday')+1, 'Oliveiraday')
print(week_days)

step(11, 'Popping Day')

# passing no arguments to pop because it already removes the last item
print(week_days)
print(week_days.pop())
print(week_days)

step(12, 'Delete Middle Day')

print(week_days)
# using the length of week_days divided by two to find the middle of the list
del week_days[len(week_days)//2]
print(week_days)

step(13, 'Remove Any Day')

print(week_days)
print(week_days.pop(2))
print(week_days)

step(14, 'Phone Keys')

keys = [['', 'ABC', 'DEF'],
        ['GHI', 'JKL', 'MNO'],
        ['PQRS', 'TUV', 'WXYZ']]

# defining how wide the keys will be
key_size = 5

# initizalizing variable
result = ''

# looping through the index and row
# creating the three first rows
for index, row in enumerate(keys):
    result += f"""+{'-'*(key_size*3+2)}+
|{f'{row[0]}':^{key_size}}|{f'{row[1]}':^{key_size}}|{f'{row[2]}':^{key_size}}|
|{f'{index*3+1}':^{key_size}}|{f'{index*3+2}':^{key_size}}|{f'{index*3+3}':^{key_size}}|
"""

# creating the fourth row
result += f"""+{'-'*(key_size*3+2)}+
|{'*':^{key_size}}|{'⎵':^{key_size}}|{'#':^{key_size}}|
|{'':^{key_size}}|{'0':^{key_size}}|{'':^{key_size}}|
+{'-'*(key_size*3+2)}+"""

print(result)

step(15, 'Let to Num')

### parameters
# letter : string
### returns
# int
# I decided to code my function like this so that I could reuse the list from above
def let_to_num(letter):
    # if letter is empty
    if not letter:
        return 1

    elif letter.isalpha() or letter == ' ':
        # looping for index and row in the keys
        for index, row in enumerate(keys):
            # looping for the index of each set letters in the row
            for index2, letters in enumerate(row):
                # if the letter inputted is in an item of row
                if letter.upper() in letters:
                    # use some clever calculations to determine the number
                    return (index*3)+(index2+1)

        # if the input is not a letter it must be a space
        return 0

    # if it is not a letter or a space it can't be found
    else:
        return 'Not Found'

letter = ' '
print(f'"{letter}" corresponds to the key "{let_to_num(letter)}"')
letter = 'a'
print(f'"{letter}" corresponds to the key "{let_to_num(letter)}"')
letter = 'H'
print(f'"{letter}" corresponds to the key "{let_to_num(letter)}"')
# it was stated before that "letToNum() takes input of a single letter, space or empty string"
# it never said that it could take in a number. Be precise on what the function should deal with
letter = '3'
print(f'"{letter}" corresponds to the key "{let_to_num(letter)}"')
letter = ''
print(f'"{letter}" corresponds to the key "{let_to_num(letter)}"')

step(16, 'Challenge')

# converting string input to list
my_string = list(input('Enter a string to be flipped in place using .insert and .pop\n\n>>> '))
# looping through the items of my_string and their indexes
for index, letter in enumerate(my_string):
    # insert at the index currently in the last item of the list and remove the last item of the list
    my_string.insert(index, my_string.pop())

# join the list to become a string again
print(''.join(my_string))
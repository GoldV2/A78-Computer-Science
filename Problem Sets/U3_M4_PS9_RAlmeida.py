# Program name: U3_M4_PS9_RAlmeida.py
# Program purpose: Problemt Set 9
# Created/revised: R. Almeida on 12-22-20

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

step(4, 'Jupiter')

planet_name = 'Jupiter'

step(5)

# printing second character
print(planet_name[1])

step(6)

# printing first character
print(planet_name[0])

step(7)

# printing first and last character
print(planet_name[0], planet_name[-1])

step(8)

# printing whole word
print(planet_name[-len(planet_name)])

step(9, 'Neptune')

planet_name = 'Neptune'

step(10)

# printing first three and the rest separately
print(planet_name[:3], planet_name[3:])

step(11)

# printing backwards
print(planet_name[::-1])

step(12, 'Wise Words')

wise_word = 'Play it who opens'

step(13)

# printing every third character
print(wise_word[::3])

step(14, 'Work Tip')

work_tip = 'Collaboration and problem solving are important'

step(15)

# counting o's in the first half
print(work_tip[:len(work_tip)//2].count('o'))

step(16, 'Code Tip')

code_tip = 'Good code is commented code'

step(17)

# printing everything between index 13 and 20
print(code_tip[13:20])

step(18, 'Favorite Food')

## parameters
# food : string
def favorite_food(food):
    for char in food:
        print(char)

favorite_food(input('What is your favorite food?\n\n>>> '))

step(19, 'Empty String')

new_string = ''

step(20, '" " to "-"')

## parameters
# string : string
## returns
# new_string : string
def space_to_hyphen(string):
    global new_string
    for char in string:
        if char == ' ':
            new_string += '-'
            continue

        new_string += char

    return new_string

print(space_to_hyphen(code_tip))

step(21, 'Hiroto')

name = 'Hiroto'

# printing every letter in new line
for char in name:
    print(char)

step(22)

# printing second character and every other
print(name[1::2])

step(23, 'Mystery Name')

## parameters
# name : string
## returns
# new_name : string
def mystery_name(name):
    new_name = ''
    change = 'aet'

    for char in name:
        if char in change:
            new_name += '?'
            continue
        
        new_name += char

    return new_name

print(mystery_name(input('Please enter your name\n\n>>> ')))

step(24, 'Length of Topic')

# this is not true, the method .find() does not return the length of a string
topic = '.find() returns the length of a string'

print(len(topic))

step(25, 'MidPt of Topic')

topic = 'len() can take a sequence, like a string, as an argument'

# printing the letter that is in the middle
print(topic[len(topic)//2])

step(26)

# code_tip is already initialized

step(27, 'Find Code in Tip')

# finding where "code" starts in code_tip
print(code_tip.find('code'))

step(28, 'Find Code')

# printing "code" fron code_tip using .find()
print(code_tip[code_tip.find('code'):code_tip.find('code')+4])

# This step does not specify which variable we have to use. The step cannot be completed unambiguously
step(29, 'Find Index of Code')

# checking if "code" exists in code_tip after index 13
code_index = code_tip.find('code', 13)

if code_index == -1:
    print('Not found')

else:
    print(code_index)

step(30, '"w", "o", "code"')

print('Use of "w"', code_tip.count('w'))
print('Use of "o"', code_tip.count('o'))
print('Use of "code"', code_tip.count('code'))

step(31, 'New Code Tip')

# horrible tip
code_tip = 'code a conditional decision like you would say it'

step(32, '"i" in Code Tip')

print(code_tip.count('i'))

step(33, 'Index of all "i"s')

# looping through a set of numbers from 0 to the length of code_tip not inclusive
for i in range(len(code_tip)):
    # if that index is an 'i' print the index
    if code_tip[i] == 'i':
        print('codeTip:', i)

step(34, 'Words After "g"')

## parameters
# string : string
def after_g(string):
    word = ''
    for char in string:
        if not char.isalpha():
            if word > 'h':
                print(word)

            word = ''
            continue

        word += char

after_g(input('Enter a quote\n\n>>> ').lower())

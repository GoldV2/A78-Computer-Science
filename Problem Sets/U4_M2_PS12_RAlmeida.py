# File Name: U4_M2_PS12_RAlmeida.py
# Purpose: Problem Set 12
# Edited - Revised: 01/19/21

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

step(5, 'States of Matter')

matter_states = ['Solid', 'Liquid', 'Gas', 'Plasma']

# joining with a new line every formatted item from the iteratoin of the enumerate function of matter_states
# formatted item includes the item and its index plus 1
print('\n'.join([f'{state} - is state of matter #{index+1}' for index, state in enumerate(matter_states)]))

step(6, 'No C Birds')

birds = ['turkey', 'hawk', 'chicken', 'dove', 'crow']

# printings birds
print(birds)
# printing a list created from birds with bird only if bird starts with c
print([bird for bird in birds if not bird.startswith('c')])

step(7, 'Point Frequency')

baskets = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]

# using the count method to count the frequency of each item
print('1pt:', baskets.count(1), '2pt:', baskets.count(2), '3pt:', baskets.count(3))

step(8, 'Hello x 4')

# creating a list of 4 hellos and joining it with a new line
print('\n'.join(['hello' for i in range(4)]))

step(9, 'Half Spell')

spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
# printing all of spell list
# then pritning the first half
# then pritning the second half
# using len and dividing it by two to figure out the halves
print('Whole:', spell_list,
      '\nFirst half:', [spell for spell in spell_list[:len(spell_list)//2]],
      '\nSecond half:', [spell for spell in spell_list[len(spell_list)//2:]])

step(10, 'Twenties')

# there is no need to iterate and append, you can just convert to a list
twenties = list(range(20, 30))
print(twenties)

step(11, 'Total Twenties')

# there is no need to iterate through, you can just use the sum function
total = sum(twenties)
print(total)

step(12, 'Total Twenties?')

# finding the sum through iteration
total2 = 0
for i in range(20, 30):
    total2 += i

# printing the second total and if the first total is the same as the second total
print('Second total:', total2)
print('First total equal to second total:', total == total2)

step(13, 'Odd Nums to 25')

# list of odd numbers from 1 to 25
print(list(range(1, 26, 2)))

step(14, 'Reversed Odds')

# list of odd numbers from 25 to 1
print(list(range(25, 0, -2)))

step(15, 'Even Elements')

elements =  ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon',
             'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium',
             'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',
             'Potassium', 'Calcium']

# joining with a new line a list of formatted string by iterating through the enumrate function of all even elements
print('\n'.join([f'{index+1} - {element}' for index, element in enumerate(elements[1::2])]))

step(16, 'Odd Elements')

elements60 =  ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon',
               'Nitrogen',  'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium',
               'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',
               'Potassium', 'Calcium', 'Hydrogen', 'Helium', 'Lithium', 'Beryllium',
               'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',  'Neon', 'Sodium',
               'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine',
               'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium',
               'Chromium', 'Manganese',  'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc',
               'Gallium', 'Germanium', 'Arsenic', 'Selenium',  'Bromine', 'Krypton',
               'Rubidium', 'Strontium', 'Yttrium', 'Zirconium']

# joining with a new line a list of formatted string by iterating through the enumrate function of all odd elements
print('\n'.join([f'{index+1} - {element}' for index, element in enumerate(elements60[::2])]))

step(17, 'Adding Lists')

numbers1= [20,21,22,23,24,25,26,27,28,29]
numbers2= list(range(30,50,2))

# combining the two above lists with a plus sign, conctatenation
print(numbers1+numbers2)

step(18, 'Extending Lists')

firstRow = ['Hydrogen', 'Helium']
secondRow = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Flourine', 'Neon']

# using the extend method to extend the first list with the second list and then printing it
firstRow.extend(secondRow)
print(firstRow)

step(19, 'Combine 3 Lists')

elem1 = ['Hydrogen', 'Helium']
elem2 = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
elem3 = ['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']

# concatenating the three variables, elem1, elem2, elem3
print(elem1+elem2+elem3)

step(20, 'More Extending')

jackJill = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
nextLine = ['To', 'fetch', 'a', 'pail', 'of', 'water']

# extending jackJill with nextline and printing it
jackJill.extend(nextLine)
print(jackJill)

step(21, 'Reverse in Place')

elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon',
            'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium',
            'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',
            'Potassium', 'Calcium']

# reversing the elements in place and printing it
elements.reverse()
print(elements)

step(22, 'Reverse Len 8')

# creating a list of all spell that have a length equal to or grater than 8 in spellList
print([spell for spell in spell_list[::-1] if len(spell) >= 8])

step(23, 'Alphabetic Elem')

# Why is Neon missing in this step?
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon',
            'Nitrogen', 'Oxygen', 'Fluorine', 'Sodium', 'Magnesium',
            'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',
            'Potassium', 'Calcium']

# printing the sorted elements
print(sorted(elements))

step(24, 'Sorting Nums')

numbers = [2,2,2,1,2,1,3,1,2,2,2,2,1,3]
# printing unsorted numbers
print(numbers)
# printing sorted numbers
print(sorted(numbers))

step(25, 'Splitting Facts')

daily_fact = "Did you know that there are 1.4 billion students in the world?"
# joining with a new line every capitalized word in a list created from daily_fact by splitting at spaces
print('\n'.join([word.capitalize() for word in daily_fact.split()]))

step(26, 'Splitting Tips')

code_tip = 'Write Python Code like you speak'
# printing a list formed by splitting code_tip on every o
print(code_tip.split('o'))


step(27, 'Splitting Poem')

poem = "The bright brain, has bran!"
# splitting poem on every b
poem_words = poem.split('b')
# printing each word on a new line using a conventional for loop
for word in poem_words:
    print(word)

step(28, 'Halogens ", "')

halogens = ['Chlorine', 'Florine', 'Bromine', 'Iodine']
# creating a strring that separates halogens with a comma and space
print(', '.join(halogens))

step(29, 'No Space Tip')

code_tip = "Read code aloud or explain the code step by step to a peer"
# joining with a empty character every word in code_tip split at spaces after capitalizing every word in code_tip
print(''.join(code_tip.title().split()))
step(30, 'Casting List')

long_word = 'decelerating'
# printing each character of long_word in a new line
print('\n'.join(list(long_word)))

step(31, '? & New Line')

questions = ["What’s the closest planet to the Sun", "How deep do dolphins swim", "What time is it"]
# iterating for question in questions
for question in questions:
    # printing every string with a question mark and new line at the end
    print(question, end='?\n')

step(31, 'Printing Bones')

foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
# creating a string with every bone separated by a comma and space in a list created from the foot_bones list but with every bone name converted to a title format
print(', '.join([bone.title() for bone in foot_bones]))
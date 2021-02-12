# File Name: U4_M3_A4_RAlmeida.py
# Purpose: Strings & Lists
# Edited - Revised: 01/18/21

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

step(10, 'Split Rhyme')

rhyme = 'Jack and Jill went up to the hill To fetch a pail of water'
# turning rhyme into a list of strings with all characters separated by a space together

rhyme_words = rhyme.split()
# using the join function to join every word in rhyme_words with a new line character and printing it
print('\n'.join(rhyme_words))

step(11, 'Code Tip List')

code_tip = 'Python uses spaces for identation'
# turning code_tip into a list of strings with all characters separated by a space together
code_tip_words = code_tip.split()
# creating a string that separates every other word in code_tip_words with a space
print(' '.join([word for word in code_tip_words[::2]]))

step(16, 'Split Poem')

poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently*"
# turning poem into a list of string with all characters separated by a asterisk together
poem_phrases = poem.split('*')
# creating a string that separates every word in poem_phrases capitalized with a new line character
print('\n'.join([phrase.title() for phrase in poem_phrases]))

step(21, 'Join Asterisk')

# instead of creating a list with each character
# simply write the word and convert it to a string
letters = list('Asterisk')
# joining every letter in Asterisk with an asterisk and printing it
print('*'.join(letters))

step(22, 'Pick Separator')

# there is no need to define phraseWords with a list of all the words
# this same list was created on a previous step
def separate(separator):
     # returning a string that joins every word in rhyme_words with separatorx
     return separator.join(rhyme_words)

# asking user for a separator
separator = input('Please enter a separator\n\n>>> ')
print(separate(separator))

step(29, '3 Prints in One')

# creating a list of 3 items with my name
my_name = 'Rafael deOliveira Almeida'.split()
# looping through every word in my_name
for word in my_name:
     # printing that word separated by a dash, not a new line
     # this allows me to print the three items in the same line
     print(word, end='-')

step(30, 'Casting to List')

# this variable was never used
msg_chars = list('Always test your code')
# there is no need to cast this into a list to do what the task is asking for
fact = "At Standard Sea Level conditions (corresponding to a temperature of 15 degrees Celsius), the speed of sound is 340.3 m/s (1225 km/h, or 761.2 mph, or 661.5 knots, or 1116 ft/s) in the Earth's atmosphere."
# you can simply loop through each character by looping through the string sequence, no need to make it a list sequence
for char in fact:
     # printing every character in the same line, and printing a new line if the character is a space
     # the instructions for this task are very ambiguous
     if char == ' ':
          print()
          continue

     print(char, end='')

step(31, 'Sum of 20 Digits')

# creating a range object from number 1 to number 20
# this is my list of numbers
numbers = range(1, 21)
# joining every item in a list created from numbers after going through a lambda function that converts
# it into a string and adds it to a + symbol by using the map function. Turning that into a list and adding it to ['0']
# so that there is no + symbol on the outsides of the equation. Then using the sum function to add all the items in the range numbers
print('Equation:', ''.join(['0'] + list(map(lambda num : '+' + str(num), numbers))), '=', sum(numbers))
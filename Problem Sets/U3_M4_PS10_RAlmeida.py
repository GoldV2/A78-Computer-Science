# Program name: U3_M4_PS10_RAlmeida.py
# Program purpose: Problemt Set 10
# Created/revised: R. Almeida on 12-22-20

from textwrap import dedent
from math import ceil

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

long_word = 'supercalifragilisticexpialidocious'

step(1)

print(long_word[::-1])

step(2)

print(long_word[0], long_word[-1])

step(3)

print(long_word[-1::-2])

step(4)

# loop will run for how many lines it is needed to fit all characters
# rounding up, so that if there is a remainder, it is accounted for
for i in range(ceil(len(long_word)/8)):
    # printing the first 8 character times the iteration for up to that same value plus 8
    print(long_word[8*i:8*i+8])

step(5)

print(long_word[5:9])

step(6)

print(len(long_word))

step(7)

print(long_word[len(long_word)//2:])

step(8)

# checking if fargil is in long_word
if long_word.find('fragil') == -1:
    print('Not found')

# if it is, print the index where it starts
else:
    print(long_word.find('fragil'))

step(9)

print(long_word.count('i'))

step(10)

print(long_word.count('s'))

step(11)

print(long_word.count('a', 4, 22))

step(12)

# creating a list with all the indexes that should be printed
indexes = [16, 32, 22, 3, 10]

# creating a loop that goes over all the indexes that should be printed in order
for index in indexes:
    # print each of those indexes in a new line
    print(long_word[index])

step(13, 'Mystery Code')

# creating a dictionary that links every letter to watch it is supposed to be converted to
replaces = {'a': '@', 'e': '#', 'i': '%', 'o': '*'}

## parameters
# string : string
## returns
# new_word : string
def mystery_code(string):
    new_word = ''
    # looping over every character in string
    for char in string:
        # if the character is one of those that must be changed
        if char in replaces:
            # add to new_word the value of that char as key
            new_word += replaces[char]
            # moving on to the next iteration of the loop
            continue

        # if char is not supposed to be changed, just add it
        new_word += char

    return new_word

print(mystery_code(input('Please enter something to be encrypted\n\n>>> ')))

# extra step that decodes whatever the function above encodes
step(14, 'Mystery Decoder')

## parameters
# string : string
## returns
# decoded_message : string
def mystery_decoder(string):
    decoded_message = ''
    # iterating over every character in the string
    for char in string:
        # if that character is one of the values in the dictionary
        if char in replaces.values():
            # loop through every key in the dictionary
            for letter in replaces:
                # if a key matches the current character
                if replaces[letter] == char:
                    # add that character to the decoded message
                    decoded_message += letter
                    # break the foor loop because there is no reason to continue searching
                    break
            # continue to next iteration after finding a valid letter
            continue
        
        decoded_message += char

    return decoded_message

print(mystery_decoder(input('Enter something to be decoded\n\n>>> ')))
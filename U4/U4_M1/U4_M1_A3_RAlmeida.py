# Program name: U4_M1_A3_RAlmeida.py
# Program purpose: Iterate a String by Character
# Created/revised: R. Almeida on 12-20-20

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

step(8)

word = "cello"
for letter in word:
# the variable letter is an arbitrary variable name. Any valid variable name can be used.
     print(letter)

word = "trumpet"
for item in word:
# the variable item is an arbitrary variable name. Any valid variable name can be used.
    print(item)
word = "piano"
for xyz in word:
# the variable xyz is an arbitrary variable name. Any valid variable name can be used.
     print(xyz)
studentName = "Skye"
newName = ""
for letter in studentName:
     if letter.lower() == "y":
          newName += letter.upper()
     else:
          newName += letter
print(studentName, "to", newName)

step(9, 'Capialize First Name')

# initializing variable that will be change
new_name = ''
# getting user in
first_name = input('Please enter your first name\n\n>>> ')

letters = 'io'
for char in first_name:
     if char in letters:
          new_name += char.upper()
          continue

     new_name += char

print(new_name)

step(11)

studentName = "Skye"

for letter in studentName[:3]:
     print(letter)

# iterate BACKWARDS
studentName = "Skye"
# start at "y" (studentName[2]), iterate backwards
for letter in studentName[2::-1]:
     print(letter)

step(12, 'Juxtaposition')

# initizalizing variable that will be changed
other_word = ''
long_word = 'juxtaposition'

# looping through a string which is every other character of long_word
for c in long_word[::2]:
     # adding character to other_word
     other_word += c

print(other_word)

step(13, 'Mirror Color')

### parameters
# fav_color : string
### returns
# string
def mirror_color(fav_color):
     return fav_color[::-1] + fav_color

# taking user input inside of the parameters of mirror_color and printing the returned string
print(mirror_color(input('Please enter your favorite color\n\n>>> ')))

step(14, 'Letter Per Line')

greeting = 'Hello, world'

# printing each individual letter in a new line
for letter in greeting:
     print(letter)
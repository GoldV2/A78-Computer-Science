# File Name: U4_M3_A2_RAlmeida.py
# Purpose: Range Function
# Edited - Revised: 01/12/21

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

step(12, 'Nums 1-6')

# iterating through 1-6, remember that range is non-inclusive
for num in range(1, 7):
     print(num)

step(13, '7!')

# initializing variable as one because if it was zero the final result would also be zero
total = 1
# iterating through 2-7
for num in range(2, 8):
     # mutliplying total by num
     total *= num

print(total)

step(14, 'Second Half')

spellList = ["Wednesday", "Tuesday", "February", "November", "Annual", "Calendar", "Solstice"]

# iterating through a range that starts at half the length of spellList and ends at the length of spellList
for i in range(len(spellList)//2, len(spellList)):
     # accessing the index
     print(spellList[i])

step(19, 'Five Fifteen')

# initializing variable
five_fifteen = []
# iterating through 5-15
for num in range(5, 16):
     # appending every number
     five_fifteen.append(num)

print(five_fifteen)

step(20, '3rd-5th Spell')

# iterating through 2-4. 2 is the index of the third item and 4 is the index of the fifth
for num in range(2, 5):
     print(spellList[num])

step(21, 'Find Annual')

# iterating from 0 to the length of spellList not inclusive
for num in range(len(spellList)):
     # if it is the index of Annual
     if spellList[num] == 'Annual':
          # print index
          print(num)
          # remove 'Annual' and add it to the end of the list
          spellList.append(spellList.pop(num))
          # print new list
          print(spellList)
          # break loop so that it doesn't find annual again
          break

step(27, '10-20 by 2')

# iterating from 10-20 every second number
for num in range(10, 21, 2):
     print(num)

step(28, '20-10 Countdown')

# starting at 20 counting down to 10
# negative step allows me to countdown
for num in range(20, 9, -1):
     print(num)

step(29, 'First & Every Third')

# iterating through 1 and length of spellList minus one every other number
for num in range(1, len(spellList), 2):
     print(spellList[num])

step(30, 'Odd Even Letters')

### parameters
# word : string
### returns
# odd, even : tuple
def odd_even(word):
     # initializing variables
     odd = ['Odd letters']
     even = ['Even letters']
     # iterating through the length of the word
     for i in range(len(word)):
          # if the index does not divide by two, it must be even
          if i%2:
               even.append(word[i])
               # skip current iteration
               continue
          
          # if not skipped above, add to odd
          odd.append(word[i])

     return odd, even

# asking for user input
user_word = input('Please enter a word to find even and odd letters\n\n>>> ')
print(odd_even(user_word))

step(31, 'Fix Error')

# list range is not defined. Use range as a function instead by using paranthesis instead of square brackets
for num in range(1, 10, 2): # change square brackets to paranthesis
     print(num)
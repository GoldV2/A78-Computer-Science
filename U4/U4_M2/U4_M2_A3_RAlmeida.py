# File Name: U4_M2_A3_RAlmeida.py
# Purpose: List Insert
# Edited - Revised: 01/07/21

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

step(7)

# [ ] review and run example
# the list before Insert
partyList = ["Joana", "Alton", "Tobias"]
print("partyList before: ", partyList)
# the list after Insert
partyList[1] = "Colette"
print("partyList after:  ", partyList)

step(8)

# [ ] review and run example
partyList = ["Joana", "Alton", "Tobias"]
print("before:",partyList)
# modify index value
partyList[1] = partyList[1] + " Derosa"
print("\nafter:", partyList)

step(9)

# IndexError Example
# [ ] review and run example which results in an IndexError
# if result is NameError run cell above before running this cell
# IndexError trying to append to end of list

try:
     partyList[3] = "Alton"
     print(partyList)
except:
     print('Step 9 results in an index error')

step(10)

# [ ] review and run example changes the data type of an element
# replace a string with a number (int)
single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print("single_digits: ", single_digits)
print("single_digits[3]: ", single_digits[3], type(single_digits[3]),"\n")
# replace string with an int
single_digits[3] = 3
print("single_digits: ", single_digits)
print("single_digits[3]: ", single_digits[3], type(single_digits[3]))

step(11, 'Three Nums')

# defining three_nums
three_nums = [3, 5, 100]
print(three_nums)
# changing the value of three_nums[0]
three_nums[0] = 'small' if three_nums[0] < 5 else 'large'
print(three_nums)

step(12, 'Three Nums Func')

### parameters
# int_list : list
# idnex : integer
### returns
# int_list : list
### purpose
# change the value of int_list[index] to small or large
def str_replace(int_list, index):
     int_list[index] = 'small' if int_list[index] < 5 else 'large'
     return int_list

# defining test list
my_numbers = [132,1123, 1, 2, 51, 21]
print(my_numbers)
# replacing last index of my_numbers with small or large and assigning to my_numbers
my_numbers = str_replace(my_numbers, -1)
print(my_numbers)

step(13, 'Three Words')

three_words = ['Rafael', 'Oliveira', 'Almeida']
print(three_words)
# converting first index to upper
three_words[0] = three_words[0].upper()
# swaping the case of the last index
three_words[-1] = three_words[-1].swapcase()
print(three_words)

step(15)

# [ ] review and run example
#the list before Insert
partyList = ["Joana", "Alton", "Tobias"]
print("partyList before: ", partyList)
print("index 1 is", partyList[1], "\nindex 2 is", partyList[2], "\n")
# the list after Insert
partyList.insert(1,"Colette")
print("partyList after:  ", partyList)
print("index 1 is", partyList[1], "\nindex 2 is", partyList[2], "\nindex 3 is", partyList[3])

step(16, 'Insert Input')

# inserting an input
partyList.insert(1, input('Please enter a name to add to partyList\n\n>>> '))
print(partyList)

step(17, 'Fix Errors')

# string object has no attribute insert. Change treeList to a list
treeList = ["aok"]
print("treeList before =", treeList)
treeList.insert(1, "pine")
print("treeList after =", treeList)
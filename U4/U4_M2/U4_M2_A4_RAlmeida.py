# File Name: U4_M2_A4_RAlmeida.py
# Purpose: Sequence Manipulation
# Edited - Revised: 01/11/21

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

# [ ] review and run example
# the list before delete
sampleList = [11, 21, 13, 14, 51, 161, 117, 181]
print("sampleList before: ", sampleList)
del sampleList[1]
# the list after delete
print("sampleList after:  ", sampleList)

step(9)

# [ ] review and run example Multiple Times
# [ ] consider how to reset the list values?
print("sampleList before:", sampleList)
del sampleList[0]
print("sampleList after:", sampleList)

step(10)

 # [ ] review and run example
mixedTypes = [1, "cat"]
# append number
mixedTypes.append(3)
print("mixedTypes list: ", mixedTypes)
# append string
mixedTypes.append("turtle")
print("mixedTypes list: ", mixedTypes)

step(11, 'Feet Bones')

ftBones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
del ftBones[2]
print(ftBones)

step(12, 'More Feet')

print(ftBones)
del ftBones[2]
print(ftBones)

print('What "navicular" deleted?', 'navicular' not in ftBones)

step(14)

# [ ] review and run example
# pop() gets the last item by default
partyList = ["Joana", "Alton", "Tobias"]
print(partyList)
print("Hello,", partyList.pop())
print("\n", partyList)
print("Hello,", partyList.pop())
print("\n", partyList)
print("Hello,", partyList.pop())
print("\n", partyList)

step(15)

 # [ ] review and run example
# can pop specific index like pop(3)
numberList = [11, 21, 13, 14, 51, 161, 117, 181]
print("before:", numberList)
numberList.pop(3)
print("after :", numberList)

step(16)

 # [ ] review and run example
# set a variable to a poped value
numberList = [11, 21, 13, 14, 51, 161, 117, 181]
print("list before:", numberList)
num_1 = numberList.pop()
num_2 = numberList.pop()
print("list after :", numberList)
print("add the popped values:", num_1, "+", num_2, "=", num_1 + num_2)

step(17, 'Feet Popping')

ftBones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
print(ftBones.pop(0))
print(ftBones.pop())
print(ftBones)

step(19)

dogTypes = ['Lab', 'Pug', 'Poodle']

while dogTypes:
     print(dogTypes.pop())

step(20, 'Purchase Amounts')

# initializing variables
purchaseAmounts = []
while True:
     # asking for user input
     inp = input('Please enter the price of each item. Enter "done" to exit\n\n>>> ')

     # checking if user input is "done"
     if inp.isalpha():
          if inp.lower() == 'done':
               print(purchaseAmounts)
               break

     # if it is not alpha or "done" or not empty it must be a number
     elif inp:
          # appending number as a float
          purchaseAmounts.append(float(inp))

step(21, 'Purchase Subtotal')

subtotal = 0
while purchaseAmounts:
     subtotal += purchaseAmounts.pop()

print(subtotal)

step(23)

 # [ ] review and run example
dogTypes = ["Lab", "Pug", "Poodle"]
if "Pug" in dogTypes:
   dogTypes.remove("Pug")
else:
   print("no Pug found")
print(dogTypes)

step(24)

 # [ ] review and run example
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]
print(dogs)
while "Poodle" in dogs:
   dogs.remove("Poodle")
   print(dogs)

step(25)

 # [ ] review and run example
# Change to "Lab", etc... to fix error
dogs.remove("Lab")
print(dogs)

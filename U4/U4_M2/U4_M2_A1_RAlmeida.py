# File Name: U4_M2_A1_RAlmeida.py
# Purpose: Sequence Manipulation
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

step(8)

# [] review and run example
# define list of strings

ftBones = ["calcaneus",
           "talus",
           "cuboid",
           "navicular",
           "lateral cuneiform",
           "intermediate cuneiform",
           "medial cuneiform"]

# display type information
print("ftBones: ", type(ftBones))

# print the list
print(ftBones)

step(9)

# [] review and run example
# define list of integers
ageSurvey = [12, 14, 12, 29, 12, 14, 12, 12, 13, 12, 14, 13, 13, 46, 13, 12, 12, 13, 13, 12, 12]

# display type information
print("ageSurvey:", type(ageSurvey))

# print the list
print(ageSurvey)

step(10)

# [] review and run example
# define list of mixed data type

mixedList = [1, 34, 0.999, "dog", "cat", ftBones, ageSurvey]

# display type information
print("mixedList:", type(mixedList))

# print the list
print(mixedList)

step(11, 'Team Names')

team_names = ['Chelsea F.C.', 'FC Barcelona', 'Liverpool F.C.', 'Real Madrid C.F', 'Manchester United F.C.']

print(team_names)
print('team_names:', type(team_names))

step(12, 'Mixed List')

mixed_list = [1, 2, 3, 'a', 'b', team_names]

print(mixed_list)
print('mixed_list:', type(mixed_list))

step(14)

# [ ] review and run example
print(ftBones[0], "is the 1st bone on the list")
print(ftBones[2], "is the 3rd bone on the list")
print(ftBones[-1], "is the last bone on the list")

step(15)

# review and run example
print(ftBones[1], "is connected to the",ftBones[3])

step(16)

 # [ ] review and run example
threeAgesSum = ageSurvey[0] + ageSurvey[1] + ageSurvey[2]
print("The first three ages total", threeAgesSum)

step(17, 'Street Names')

street_names = ['North Avenue', 'South Street', 'Jefferson Street', 'Monroe Avenue', 'Parker Street']

# Accessing the first and last index of street_names
print('There is not parking on', street_names[0], 'and', street_names[-1])

step(18, 'Sum 2 Add')

num_2_add = [0, 5, 10, 15, 25]
# using the sum function to add all the items in the list sum_2_add
sum_of_2_add = sum(num_2_add)
print('The sum of the 5 numbers is', sum_of_2_add)

step(19, 'Fix the Error')

# define list payChecks
payChecks = [None, None, 33, 34.50]
# change Print to print, close print() parenthesis
print("Total of check 3 & 4 = $", payChecks[2] + payChecks[3])

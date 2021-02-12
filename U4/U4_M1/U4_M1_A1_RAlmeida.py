# Program name: U4_M1_A1_RAlmeida.py
# Program purpose: 
# Created/revised: R. Almeida on 12-115-20

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

step(8, 'Python Language')

language = 'Python'
# accessing the first letter of the string language
print(language[0], 'is at index 0 in the string "Python"')

step(10)

# Example:
studentName = "Jin"
if studentName[0].lower() == "a":
   print('Winner! Name starts with A:', studentName)

elif studentName[0].lower() == "j":
   print('Winner! Name starts with J:', studentName)

else:
   print('Not a match, try again tomorrow:', studentName)

# Example: Display the last character of the name. Note the error “cannot index out of range”. Remember index begins at 0.
studentName = "Tobias"
try:
     print(studentName[6])

except:
     print('Step 10 has a "string index out of range" error on purpose')

# Example corrected:
studentName = "Tobias"
print(studentName[5])

step(11, 'Street Name')

# defining the variable street_name and giving it the value of a string
street_name = 'North Broad Street'

# printing the first letter of street_name
print(street_name[0])
# printing the third letter of street_name
print(street_name[2])
# printing the fifth letter of street_name
print(street_name[4])

step(12, 'Team Name')

# asking for user input
team_name = input('Please enter a team name containig, "i", "o" or "u" as the second character\n\n>>> ')

# checking if the length of team_name is valid
if len(team_name) < 2:
     print("The name of your team was not long enough")

# checking if the second letter is valid
elif team_name[1] in 'iou':
     print(f'Wow, the name {team_name} is so nice and it has the letter {team_name[1].lower()} as its 2nd letter')

# if all of the above are False
else:
     print(f'Sorry, that is not a valid name, the second letter is {team_name[1].lower()} and not "i", "o" or "u"')

step(14)

# Examples:
studentName = "Joana"
# get last letter
endLetter = studentName[-1]
print(studentName,"ends with", "'" + endLetter + "'")
# get second to last letter
secondLastLetter = studentName[-2]
print(studentName,"has 2nd to last letter of", "'" + secondLastLetter + "'")
# you can get to the same letter with index counting + or -
print("for", studentName)
print("index 3 =", "'" + studentName[3] + "'")
print("index -2 =","'" + studentName[-2] + "'")

step(15, 'Street Name 2')

street_name = 'North Broad Street'

# Craeting a loop that starts at 1 and ends at 3
for i in range(1, 4):
     # printing the letter in the index of negative i, i will be between 1-3 inclusive
     print(street_name[-i])

step(16, 'My Name')

# defining the variable my name
my_name = 'Rafael'

# printing the first letter of my_name
print('First letter of', my_name, 'is', my_name[0])
# printing the last letter of my_name regardless of length
print('Last letter of', my_name, 'is', my_name[-1])

step(17)

shoe = "tennis"
# print the last letter
# square brackets must be used to access indexes
print(shoe[-1])
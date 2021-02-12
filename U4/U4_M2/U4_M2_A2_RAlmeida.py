# File Name: U4_M2_A2_RAlmeida.py
# Purpose: Appending to Lists
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

# review and run example
sampleList = [1,1,2] #the list before append
print("sampleList before:", sampleList)
sampleList.append(3)
# the list after append
print("sampleList after:", sampleList)

step(9)

# review and run example
#append number to sampleList
print("sampleList start: ", sampleList)
sampleList.append(3)
print("sampleList added: ", sampleList)
#append again
sampleList.append(8)
print("sampleList added: ", sampleList)
#append again
sampleList.append(5)
print("sampleList added: ", sampleList)
#run # 7 before running this example

step(10)

# review and run example
mixedTypes = [1, "cat"]
#append float to mixedTypes
mixedTypes.append(3.14)
print("mixedTypes list: ", mixedTypes)
#append string and boolean to mixedTypes
mixedTypes.append("turtle")
mixedTypes.append(False)
print("mixedTypes list: ", mixedTypes)

step(11, 'Currency Values')

# creating a list of lists that include the name of the currency and the value in us dollars
currency_vals = [0.19, 1.23, 0.15]
print(currency_vals)
# appending a new currency
currency_vals.append(32822.30)

step(12, 'Currency Names')

# creating list with currency names
currency_names = ['BR Real', 'Euro', 'Chinese Yuan']
print(currency_names)
# appending new currency name
currency_names.append('Bitcoin')

step(13, 'New Currencies')

# printing currency names
print(currency_names)
# asking for input and appending input
currency_names.append(input('Please enter the name of a currency\n\n>>> '))
# printing new currency_names
print(currency_names)

step(14, 'BDay Survey')

bday_survey = []

i = 0
while True:
     date = input(f'User {i}, please enter the day you were born, 1-31\n\n>>> ')

     if date.lower() == 'q':
          break

     elif not date.isdigit():
          print('Invalid birth date')

     elif '0' < date and date < '32':
          bday_survey.append(int(date))
          i += 1

     else:
          print('Date out of range')

print(bday_survey)

step(15, 'Fix Error')

threeNumbers = [1,1,2]
# index is out of range. Decreased index by one
print("an item in the list is:", threeNumbers[2])
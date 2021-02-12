# Program name: U3_M3_A1_RA.py
# Program purpose: Learning if statements
# Created/revised: R. Almeida on 11-16-20

# Step 8

hotTea = True

# Statement to check if hotTea is True
if hotTea:
    print('Enjoy some hot tea!')

else:
    print('Enjoy some tea, and perhaps try hot tea next time.')

# Step 9

# Statement to check if isSunny is True
isSunny = True
 
if isSunny:
    print('Today is sunny outside!')

else:
    print('Today is not sunny outside :(')

# Step 11

# Statement to check if I am a cool python Programmer, if programmer is True
programmer = True

if programmer:
    print('I am a Python programmer!')

else:
    print('One day you will get there.')

# Step 14

# Testing if both of these strings are lowercase
testString1 = 'welcome'
testString2 = 'I have $3'

if testString1.islower():
    print('Test string 1:', testString1, 'is all lowercase!')

else:
    print('There is at least one character in:', testString1, 'that is not lower case.')

if testString2.islower():
    print('Test string 2:', testString2, 'is all lowercase!')

else:
    print('There is at least one character in:', testString2, 'that is not lower case.')

# Step 15

# Defining a startsWithW that takes in one argument called string, that will print a stetement if string starts with 'W'
def startsWithW(string):
    if string.lower().startswith('w'):
        print(string, 'starts with W.')
    
    else:
        print(string, 'does not start with W.')

testString1 = 'welcome'
testString2 = 'I have $3'
testString3 = 'With a function it\'s efficient to repeat code'

startsWithW(testString1)
startsWithW(testString2)
startsWithW(testString3)

# Step 16

# Defining a checkAddress that takes in one argument called string, that will print a stetement if string is alphanumerical

def checkAddress(string):
    # Changed from .isalpha to .isalnum
    if string.isalnum():
        print(string, 'is alphanumerical.')

    else:
        print(string, 'is not alphanumerical.')

address1 = "600 Brewer Drive"
address2 = "42 FrankenStein Lane!"
address3 = "100 Main Street"

checkAddress(address1)
checkAddress(address2)
checkAddress(address3)
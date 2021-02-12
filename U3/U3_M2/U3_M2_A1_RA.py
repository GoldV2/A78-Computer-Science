# Program name: U3_M2_A1_RA.py
# Program purpose: learning functions
# Created/revised: R. Almeida on 11-09-20

# Step 8

# Defining hard coded variables with values that describe myself.
name = 'Rafael Almeida'
age = 15
weight = 150
height = 6

# Printing the information above
print('Hi, my name is', name, 'I am', age, 'years old and I weigh', weight, 'pounds at', height, 'feet tall')

# Step 10

# Defining a function called shooutOut that
# takes in one argument shout and returns shout in uppercase with an exclamation
def shoutOut(shout):
    return shout.upper() + '!'

# Collecting user input to be used in the function defined above
# and printing the result of the function
myPhrase = input('Type something you want to yell.\n\n>>> ')
print(shoutOut(myPhrase))

# Step 12

# Defining a function called screamThis that
# takes in one argument wordsToYell and returns wordsToYell in uppercase with an exclamation
def screamThis(wordsToYell):
    return wordsToYell.upper() + '!'

# Collecting user input to be used in the function defined above
# and printing the result of the function
wordsToYell = input('Input words to yell.\n\n>>> ')
print(screamThis(wordsToYell))

# 13
print()

# 14
# Defining a function called screamThis that was one default paramter wordsToYell
def screamThis(wordsToYell = 'this is a default message'):
    return wordsToYell.upper() + '!'

print(screamThis())
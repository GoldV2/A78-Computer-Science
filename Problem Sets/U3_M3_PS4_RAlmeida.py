# Program name: U3_M3_PS4_RAlmeida.py
# Program purpose: Problem Set 4
# Created/revised: R. Almeida on 11-26-20

from random import choice

# Step 6
# Taking user input, casting to an integer
yourAge = int(input('What is your age?\n\n>>> '))

# if yourAge is greater than or equal to 12 print yourAge+10
if yourAge >= 12:
    print(f'In 10 years, you will be: {yourAge+10} years old!')

# Simply print yourAge
else:
    print(f'It\'s good to be {yourAge} years old!')

# Step 7
# Taking in user input
num = input('Input a number please\n\n>>> ')

# Checking if user input is valid, if it is a digit
if not num.isdigit():
    print(f'Sorry {num} is not a valid input!')

# Comparing user input to 100
elif int(num) < 100:
    print(f'{num} is less than 100')

elif int(num) > 100:
    print(f'{num} is greater than 100')

else:
    print(f'WOW {num} is equal to 100')

# Step 8
# Function letterGuess takes in no paremeters
# returns nothing
def letterGuess():
    # Converting the alphabet to a list, picking a random letter
    myLetter = choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # Creating a way to limit user to only try 5 times
    n = 5
    while n > 0:
        # Takin in user inputer
        userLetter = input('Please enter a single letter to guess\n\n>>> ')

        # Checking if it is valid, if it isn't let the user try again
        if not userLetter.isalpha():
            print(f'Sorry {userLetter} is not a valid input. Try again.')
            
        # If it is valid, compare to my letter and subtract 1 from n
        elif userLetter > myLetter:
            n -= 1
            print(f'Your guess was too HIGH!. You have {n} tries left.')

        elif userLetter < myLetter:
            n -= 1
            print(f'Your guess was too LOW!. You have {n} tries left.')

        # If the user's answer is right
        else:
            n -= 1
            print(f'Congratulations, your answer of: {userLetter} matches the correct answer: {myLetter}')
            return

    # If the user runs out of tries
    print('You have failed :( Better luck next time.')
    return

letterGuess()

# Step 9
# petConversation takes in no paremeters
# returns nothing
def petConversation():
    # Taking in user input
    petInfo = input('Tell me about your pets\n\n>>> ').lower()

    # If dog is in input ask the type of dog and compare to the dog I own
    if ('dog' in petInfo):
        print('Nice I see you have a dog!')

        t = input('What type of dog is it?\n\n>>> ').lower()

        if 'poodle' in t:
            print('Wow I have a poodle too!')
        
        else:
            print(f'I wish I had a {t}, they are so cute!')

    # If pig is in input, ask if the pig is fat
    if ('pig' in petInfo):
        print('Nice, you have a pig? That\'s an interesting pet!')

        f = input('Is your pig fat? Yes or no?\n\n>>> ').lower()

        if f == 'yes':
            print('Hehe, that is funny!')

        elif f == 'no':
            print('He is probably hungry, go feed it!')

        else:
            print(f'I could not understand {f}')

    # If hedgehog is in input, MIND BLOWN
    if ('hedgehog' in petInfo):
        print('Wow, this one I have never seen before, take care of your hedgehog!')

    print('I appreciate the info given!')

petConversation()
# Step 10
# Defining a dictionary with lowercase rainbow color letters as the keys and the corresponding as values
colors = {'r': 'red', 'o': 'orange', 'y': 'yellow', 'g': 'green', 'b': 'blue', 'i': 'indigo', 'v': 'violet'}

# Asking for user input
# Use the keys() function to get a list of all the keys and join them with nothing and make it uppercase
# The input is lowercase
fav = input(f'What is your favorite color of the rainbow? Input one of these {"".join(colors.keys()).upper()}\n\n>>> ').lower()

# Checking if user input is in colors
# If it is, print the corresponding color for each letter using an if statement
if fav in colors:
    if fav == 'r':
        print('Your favorite color is red!')

    elif fav == 'o':
        print('Your favorite color is orange!')

    elif fav == 'y':
        print('Your favorite color is yellow!')

    elif fav == 'g':
        print('Your favorite color is green!')

    elif fav == 'b':
        print('Your favorite color is blue!')

    elif fav == 'i':
        print('Your favorite color is indigo!')

    elif fav == 'v':
        print('Your favorite color is violet!')

# if the fav is not in colors
else:
    print('Your color is not in the rainbow, sorry.')

# Step 11
# rainbwColor takes in one string parameter fav
# Returns a string displaying the name of the favorite color by accessing it in the dictionary. Or if the color is not available
def rainbowColor(fav):
    return f'Your favorite color is {colors[fav]}!' if fav in colors else 'Your color is no in the rainbow, sorry.'

# Similar to line 124
fav = input(f'What is your favorite color of the rainbow? Options: {"".join(colors.keys()).upper()}\n\n>>> ').lower()

print(rainbowColor(fav))

# Step 12
# function ageCalc takes in one integer paremeter, age
# Returns age + 50 if age is less than 50 or age - 50, else return age - 50
def ageCalc(age):
    return age + 50 if age < 50 else age - 50

# Loop to force the user to input a valid input that can be converted to an integer
while True:
    try:
        fake = input("What is your age?\n\n>>> ")
        age = int(fake)
        print(ageCalc(age))
        break

    except:
        print(f'Sorry, {fake} is not a valid age. Try again.')

# Step 13
# Taking in 2 user inputs and casting to floats
number1 = float(input('Enter the first number\n\n>>> '))
number2 = float(input('Enter the second number\n\n>>> '))

# Creating a sorter list of the two user inputs to easily access the min and max
l = sorted([number1, number2])
# Performing the corresponding action shown by the sign printed
print(f'{number1} + {number2} = {sum(l)}')
print(f'{number1} - {number2} = {number1-number2}')
print(f'The average of {number1} and {number2} is {sum(l)/2}')
print(f'{l[-1]} - {l[0]} = {l[-1]-l[0]}')
# Check if the lowest number is zero, if it is, do not divide
print(f'{l[-1]} / {l[0]} = {l[-1]//l[0]}' if l[0] != 0 else f'{l[-1]} / 0 is not allowed')

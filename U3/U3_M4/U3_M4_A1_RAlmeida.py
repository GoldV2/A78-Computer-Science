# Program name: U3_M4_A1_RAlmeida.py
# Program purpose: Nested Conditionals
# Created/revised: R. Almeida on 12-02-20

# A function I will now use every program to denote which step you are viewing
def step(n):
    print(f"\n{'-'*20}\nStep {n}\n{'-'*20}\n")

step(10)

sandwichType = input('"c" for Cheese or "v" for Veggie Special: ')

if sandwichType.lower() == "c":
    # select cheese type
    cheeseType = input('"c" for Cheddar or "m" for Manchego: ')

    if cheeseType.lower() == "c":
        print('Here is your Cheddar Cheese sandwich')

    else:
        print('Here is your Manchego san')

else:
    print('Here is your Veggie Special')

step(11)

print("Hi, welcome to the sandwich shop.  Please select a sandwich.")
sandwichType = input('"c" for Cheese or "v" for Veggie Special: ')
# select sandwich type based on user input
print()

if sandwichType.lower() == "c":
   # select cheese type
   print("Please select a cheese.")
   cheeseType = input('"c" for Cheddar or "m" for Manchego: ')
   print()

   if cheeseType.lower() == "c":
       print("Here is your Cheddar Cheese sandwich.  Thank you.")

   elif cheeseType.lower() == "m":
       print("Here is your Manchego Cheese sandwich. Thank you.")

   else:
       print("Sorry, we don't have", cheeseType, "choice today.")

elif sandwichType.lower() == "v":
   print("Here is your Veggie Special. Thank you.")

else:
   print("Sorry, we don't have", sandwichType, "choice today.")

print()
print("Goodbye!")

step(12)

# Getting user input and converting to lowercase so I dont have to use .lower() all the time
sayHello = input('Do you want to say hello? "yes" or "no"\n\n>>> ').lower()

if sayHello == 'yes':
    fullHello = input('Do you want to say full hello or just hi? "yes" or "no"\n\n>>> ').lower()

    # Beginning of nested conditionals
    if fullHello == 'yes':
        print('Hello')

    elif fullHello == 'no':
        print('Hi')

    # Dealing with an answer other than yes or no
    else:
        print('I could not understand your answer.')

elif sayHello == 'no':
    print('*friendly nod*')

# Dealing with an answer other than yes or no
else:
    print('I could not understand your answer.')

step(13)

# Creating a list of available birds
birds = ['parrot', 'crane', 'penguin', 'hummingbird', 'toucan', 'woodpecker']

# Function guess takes in no parameters+
# Returns a boolean and a string
def guess():
    birdGuess = input('Guess a type of bird we have\n\n>>> ').lower()

    if birdGuess in birds:
        return True, birdGuess

    else:
        return False, birdGuess

# Setting a valu to determine how many times the loop will run
x = 3
# While loop will run as long as x is greater than 0
while x > 0:
    # tf is a boolean, bird is a string
    tf, bird = guess()
    
    if tf:
        # Subtracting one from x every time the user tries
        x -= 1
        # Showing the user how many times they tried, and the bird that they guessed correctly
        print(f'Congratulations, you have tried {3-x} ' + ('time' if 3-x == 1 else 'times') + f' and guessed "{bird}"" correctly')
        break

    else:
        x -= 1
        # Showing the user the bird they guessed incorrectly, how many tries left, and if the program will continue or not
        print(f'Sorry, we do not have a "{bird}". You have {x} ' + ('try' if x == 1 else 'tries') + ' left' + ('. Try again' if x != 0 else '. Better luck next time'))

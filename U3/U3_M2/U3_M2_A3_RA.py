# Program name: U3_M2_A3_RA.py
# Program purpose: functions with parameters
# Created/revised: R. Almeida on 11-12-20

# Step 8
# Fixing the order of the code given

def hatAvailable(color):
    hatColors = 'black, red, blue, green, white, grey, brown, pink'
    return (color.lower() in hatColors)

haveHat = hatAvailable('green')
print('Hat available is ', haveHat)

# Step 9
# Creating a function called birdAvailable that takes in one parameters bird
# Returns True with bird is in the list of birds

def birdAvailable(bird):
    birdTypes = 'crow, robin, parrot, eagle, sandpiper, hawk, pigeon'

    return bird in birdTypes

bird = input('Input a type of bird\n\n>>> ')

# If birdAvailable returns true, it will print a statement saying that the bird is available
print(bird + ' is available' if birdAvailable(bird) else bird + ' is not available')

# Step 9
# Fixing code

# add the keyword def
def howMany():
    requested = input('Enter how many you want: ')

    # match the letter case from the variable defined above
    return requested

# Getting user input for numberNeeded
numberNeeded = howMany()

# Fixing prnt to print
print(numberNeeded, 'will be ordered')
# Program name: U3_M3_PS6_RAlmeida.py
# Program purpose: Problem Set 6
# Created/revised: R. Almeida on 12-03-20

def step(n):
    print(f"\n{'-'*20}\nStep {n}\n{'-'*20}\n")

step(8)

print("The new line character is \"\\n\"")

step(9)

print("\"That\'s how we escape!\"")

step(10)

print("\t1\tone\n\t22\ttwo\n\t333\tthree")

step(11)

# function quoteMe takes in one string parameter, phrase
def quoteMe(phrase):
    return f"\'{phrase}\'" if phrase.startswith('"') else f"\"{phrase}\""

phrase = input('Enter a phrase to add quotes around it\n\n>>> ')

print(quoteMe(phrase))

step(12)

# Shirt object takes in one string paremeter, size
# Shirt has 2 attributes, size, colors
# Shirt hsa 2 methods, addColor, __str__
class Shirt:
    def __init__(self, size):
        self.size = size
        self.colors = []

    def addColor(self, color):
        self.colors.append(color)
        color.sizes.append(self.size)

    def __str__(self):
        return f"{self.size}\t{' '.join([str(color) for color in self.colors])}"

# Color object takes in one string pararemeter, color
# Color has 2 attributes, color, sizes
# Color has 1 method, __str__
class Color:
    def __init__(self, color):
        self.color = color
        self.sizes = []

    def __str__(self):
        return self.color

# Generating colors
w = Color('white')
b = Color('blue')

# Generating large shirt color tree
l = Shirt('large')
# Adding w, to the colors attribute of l
l.addColor(w)

# Generating medium shirt color tree
m = Shirt('medium')
m.addColor(w)
m.addColor(b)

# Generating small shirt color tree
s = Shirt('small')
s.addColor(b)

# Dictionary to link each size to the corresponding Shirt object
inventory = {'large': l, 'medium': m, 'small': s}

# The function buyShirt takes in no parameters
# returns nothing
def buyShirt():
    # Loop to trap the user to select an available size
    while True:
        size = input(f"What size shirt do you use? Options: {', '.join(inventory)}\n\n>>> ")

        if size in inventory:
            print('We have the size your\'re looking for!')

            # Loop to trap the user to select an available color
            while True:
                # For loop creates a list of all colors of all sizes and joins them using ", " to form a single string
                color = input(f"What color shirt do you want? Options: {', '.join([str(color) for color in inventory[size].colors])}\n\n>>> ")

                if color in [str(color) for color in inventory[size].colors]:
                    print(f'Here, take your {color} {size} shirt!')
                    break

                else:
                    print(f'We do not have a {color} {size} shirt. Here is the available colors for {size} size')
                    # Using the __str__ method to get the color and sizes formatted
                    print(f"\nSize\tColor\n{inventory[size]}\n")

            break

        else:
            print('Sorry, we do not have the size you\'re looking for. Here is the available stock')
            print("\nSize\tColors")

            # If the user picks a size that is not available, print the whole stock
            for shirt in inventory.values():
                print(shirt)

            print()

buyShirt()

step(13)

# function strAnal takes in one string paremeter, myStr
def strAnal(myStr):
    # Check if is digit
    if myStr.isdigit():
        # if statement is checking if myStr is less than 99
        return ('Your string is less than 99' if int(myStr) < 99 else 'Your string is greater than or equal 99')

    # if is alpha
    elif myStr.isalpha():
        return 'Your string is all alphabetical'

    # if is anything besides digit or alpha
    else:
        return 'Your string is neither all alphabetical or all digits'

print(strAnal(input('Enter a string please\n\n>>> ')))

step(14)

# function tickCheck takes in two string paremeters, section, seats
def tickCheck(section, seats):
    # checks if seats is a number, then if it is greater than 0 and less than 11
    if seats.isdigit() and (0 < int(seats) < 11):
        # if section is possibly general
        if section.startswith('g'):
            return True
        
        # if section is possibly floor
        elif section.startswith('f'):
            return True

    # if everything fails, it must be False
    return False

section = input('Enter section. General or floor\n\n>>> ').lower()
seats = input('Enter the number of seats\n\n>>> ').lower()

print('Approved:', tickCheck(section, seats))
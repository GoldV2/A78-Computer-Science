# Program name: U3_M2_PS2_RAlmeida.py
# Program purpose: Problem Set 2
# Created/revised: R. Almeida on 11-19-20

# Exercise 1

# shortRhyme takes in no parameters
# prints a three line rhyme
def shortRhyme():
    print('Roses are red, violets are blue,\nIf you\'re a Python programmer,\nI love you!')

shortRhyme()

# Exercise 2

# titleit takes a string parameter, bookTitle
# prints the string parameter using the method .title()
def titleIt(bookTitle):
    print(bookTitle.title())

titleIt('automate the boring stuff with python')

userTitle = input("Input a book title\n\n>>> ")
titleIt(userTitle)

# Exercise 3

# displayScore takes in one string parameter, name, and one integer paremter, score
# name has a default value of 'unknown', score has a default value of 0
# prints name conc to score
def displayScore(name = 'unknown', score = 0):
    print(name + ': ' + str(score))

displayScore()
displayScore('Mickey Mouse')
displayScore('Rocky Balboa', '106')

# Exercise 4
# bookStore takes in one string argument, book, and one float paremeter, price
# price has a default value of 9.99
# prints book conc to price
def bookStore(book, price = 9.99):
    print(book + ', costs $' + str(price))

bookName1 = input("Enter the title of a book\n\n>>> ")
bookStore(bookName1)

bookName2 = input("Enter the title of another book\n\n>>> ")
price1 = float(input('What is the price of ' + bookName2 + '?\n\n>>> ' ))
bookStore(bookName2, price1)

# Exercise 5
# Correcting errors
# def makeGreeting(name, greeting = "Hello"):
#     return (greeting + " " + name + "!")
# 
# print(makeGreeting(getName(), Getgreeting())) # getName and Getgreeting haven't been defined, Name Error
# 
# Def getName(): # capitazlied the keyword "def" incorrectly, Syntax Error
#     nameEntry = input("enter a name: ")
#     return nameEntry
# 
# def getGreeting() # Missing colon after defining a function, Syntax Error
#     greetingEntry = input("enter a Greeting: ")
#     return greetingEntry

def makeGreeting(name, greeting = "Hello"):
    return (greeting + " " + name + "!")

def getName():
    nameEntry = input("enter a name: ")
    return nameEntry

def getGreeting():
    greetingEntry = input("enter a Greeting: ")
    return greetingEntry

print(makeGreeting(getName(), getGreeting()))
# File Name: U4_M2_PS13_RAlmeida.py
# Purpose: Problem Set 13
# Edited - Revised: 02/14/21

from textwrap import dedent

def task(n, name = ''):
    width = len(name) + 8

    s = f"""
         +{'-'*width}+
         |{f'Task {n}':^{width}}|"""

    if name:
        s += f"""
         |{f' Name: {name}':^{width}}|
         +{'-'*width}+
         """

    else:
        s += f"""
         +{'-'*width}+
         """

    print(dedent(s))

task(1, 'Order the Colors of the Rainbow')

# opening file
rainbow_file = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\Problem Sets\\Problem Set 13\\rainbow.txt')
# reading every line and saving it as a list
rainbow_colors = rainbow_file.readlines()
# sorting the list in place
rainbow_colors.sort()
# looping through the list
for line in rainbow_colors:
    # printing every line in uppercase excluding the last character
    print(line[:-1].upper())

rainbow_file.close()

task(2, 'The Weather')

mean_temps = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\Problem Sets\\Problem Set 13\\meantemp.txt')
# reading the first lin of mean_temps
headings = mean_temps.readline()
print(headings)
# turning headings into a list
headings = headings.split(',')
print(headings)

while True:
    line = mean_temps.readline().split(',')[:3:2]
    # if there is something in that line, print it
    # name, max temp
    if line != ['']:
        print(line)
    # if there is nothing in that line, if it is the last line, break the loop
    else:
        break

mean_temps.close()

# the steps for this task were very hard to follow and at the end of it
# the code doesn't even work properly if you follow the instructions
# i will try to rewrite the instructions and recode it so that it has the functionality i think it should have
task(3, 'Pi Guessing')

pi = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\Problem Sets\\Problem Set 13\\pi.txt')

name = input('Please enter your name\n\n>>> ')
seed = len(name)
pi.seek(seed)
# digit will always be the same in this code
# destroying the purpose of guessing
digit = pi.read(1)

correct = 0
wrong = 0
while True:
    guess = input('Enter a single digit guess or "q" to quit\n\n>>> ')
    if not guess.isdigit():
        break

    if digit == '.':
        digit = pi.read(1)

    # it is stated in the prompt that the file is one line, so there will never be a \n character in it
    elif digit == '\n':
        seed += 1
        pi.seek(seed)

    elif guess == digit:
        print('Correct!')
        correct += 1

    elif guess != digit:
        print('Wrong!')
        wrong += 1

print(f'Correct Guesses: {correct}\nWrong Guesses: {wrong}')

pi.close()

task(3, 'Pi Guessing Corrected')

# Create a program that gathers the digits of pi starting from the index equal to the length of the user's name, then
# prompts the user to guess which digit it is, and moves on to the next digit. The program
# should record how many guesses were correct or wrong.

# 1. open pi.txt in read mode and store it in the variable "pi"
# 2. prompt for the user's name and store it in the variable "name"
# 3. find the length of "name" and store it in the variable "seed"
# 4. set the read pointer of "pi" to the value of "seed" using the .seek() attribute
# 5. initialize two counter variables with the value of 0, "correct" and "wrong"
# 6. create an infinite while loop
## inside the loop ##
    # 1. read one character from "pi" and store it in the variable "digit"
    # 2. if "digit" is equal to ".", read the next character in the file
    # 3. if "digit" is equal to "", break the loop
    # 4. prompt the user to guess a digit and store it in the variable "guess"
    # 5. if the variable "guess" is equal to "digit", display the message "Correct!" and increment the variable "correct" by 1
    # 6. if the variable "guess" is not equal to "digit", display the message "Wrong!" and increment the variable "wrong" by 1
    # 7. if the variable "guess" is not a digit, break the while loop
## outside the loop ##
# 7. After the while loop ends, print a message displaying how many guesses were correct and wrong
# 8. close "pi"

pi = open('D:\\ralmeida\\Documents\\Classes\\A7-8 Computer Science Principles\\A78-Computer-Science-Classwork\\Problem Sets\\Problem Set 13\\pi.txt')
name = input('Please enter your name\n\n>>> ')
seed = len(name)
pi.seek(seed)

correct = 0
wrong = 0
while True:
    digit = pi.read(1)

    if digit == '.':
        digit = pi.read(1)

    elif digit == '':
        break

    guess = input('Please enter a single digit guess or a non-digit to quit\n\n>>> ')
    if not guess.isdigit():
        break

    elif digit == guess:
        correct += 1
        print('Correct!')

    elif digit != guess:
        wrong += 1
        print('Wrong!')

print(f'Correct Guesses: {correct}\nWrong Guesses: {wrong}')
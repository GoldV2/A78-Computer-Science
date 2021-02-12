# Program name: U3_M4_PS7_RAlmeida.py
# Program purpose: Problemt Set 7
# Created/revised: R. Almeida on 12-12-20

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

step(7, 'Forever Sum')

def forever_sum():
    # initializing place holder for variable that will be used inside the lopp
    s = 0
    while True:
        # asking for using input
        inp = input('Please enter a digit\n\n>>> ')

        # checking if input is valid
        if inp.isdigit():
            # if it is, add to s
            s += int(inp)

        # else, stop loop
        else:
            print('This is not a digit')
            print(f'Your inputs added to {s}')
            break

forever_sum()

step(8, 'Rainbow Colors')

def rainbow_colors():
    # initizaling variables that will be used in the loop
    tries = 4
    rainbow = 'red orange yellow green blue indigo violet'
    while True:
        # if the user runs out of tries, stop loop
        if tries == 0:
            print('You ran out of tries')
            break

        # if the user has tries left
        else:
            inp = input('Please enter a color in the rainbow\n\n>>> ')

            # if user input is a string in rainbow
            if inp in rainbow:
                # display how many tries it took
                print(f'Good job, it took you {4-tries+1} tries to be correct!')
                break

            # if input is not in rainbow, remove one try and display tries left
            else:
                tries -= 1
                print(f'You have {tries} tries left. Try again')

rainbow_colors()

step(9, 'Book Title')

def book_title():
    while True:
        # asking for user input
        inp = input('Please enter the title of a book\n\n>>> ')

        # checking if it is a title
        if inp.istitle():
            print(f'Nice, {inp} is my favorite book')
            break

        else:
            print('Sorry, that is not a valid title. Try again')

book_title()

step(10, 'Math Quiz')

def math_quiz():
    # initializing variables that will be used in the loop
    ans = 5

    while True:
        # asking for user input
        inp = input('What is the largest solution to: (x^2)-4x-5\n\n>>> ')

        # if input is valid
        if inp.isdigit():
            # if input is correct
            if int(inp) == ans:
                print(f'Nice, {ans} is the correct answer!')
                break

            else:
                print('Sorry, that is not the correct answer. Try again')

        else:
            print('Sorry, that is not a valid input. Try again')

math_quiz()

step(11, 'Find Error')

# [ ] review the code, run, fix the error
# need to convert input to integer
tickets = int(input("Enter tickets remaining (0 to quit): "))
while tickets > 0:
    # if tickets are multiple of 3 then "winner"
    # tickets was spelled with an uppercase T
    if int(tickets /3) == tickets /3:
       print("you win!")
   
    else:
        print("sorry, not a winner.")
   
    tickets = int(input("Enter tickets remaining (0 to quit): "))

print("Game ended")

step(12, 'Quiz Item')

# function quiz_item takes in two string paremeters, question, solution
def quiz_item(question, solution):
    # displaying question
    print(question)

    while True:
        # asking for user answer and converting to lowercase
        ans = input('Enter the answer\n\n>>> ').lower()

        # ig ans is equal to solution break loop
        if ans == solution:
            print('Congratulations, that was the correct answer!')
            break

        else:
            print('That is incorrect. Try again')

quiz_item('How many digts does a human have?', '20')


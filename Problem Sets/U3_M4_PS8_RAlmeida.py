# Program name: U3_M4_PS8_RAlmeida.py
# Program purpose: Problemt Set 8
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

step(5, 'String Analysis')

# parameters
# string: string type
def string_analyzer(string):
     # checking if string is a digit
     if string.isdigit():
          # if it is a digit check if it is greater than 100 or else
          if int(string) > 100:
               return string + ' is a big number!'

          else:
               return string + ' is a small number!'

     # check if string is alphabetic
     elif string.isalpha():
          return string + ' is all alphabetic!'

     # if it is not a digit nor alphabetic, it must oontain multiple types
     else:
          return string + ' contains multiple character types!'

# initializing variable to be used inside the loop
i = 3
# loop will run as long as i is greater than 0
while i > 0:
     # asking for user input
     user_input = input(f'Please enter a string to be analyzed. You have {i} analyses left\n\n>>> ')
     # if the user inputted something and is valid
     if user_input:
          print(string_analyzer(user_input))
          # take out 1 from i, because want the loop to run 3 times with valid inputs
          i -= 1

     # if the user inputted nothing and is not valid
     else:
          print('Your input cannot be empty. Try again')
          # do not remove anything from i if input is not valid

# after the loop is done
print('You ran out of analyses. Thank you for the data!')
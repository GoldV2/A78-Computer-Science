# Program name: U3_M3_A3_RAlmeida.py
# Program purpose: String Comparison
# Created/revised: R. Almeida on 11-19-20

# Step 7
# Creating the variable msg

msg = 'Hello'

# Step 8
# Comparing user input to msg

userMsg = input('Input a greeting please.\n\n>>> ')

if userMsg == msg:
    print(f'{userMsg} == {msg} is True')

else:
    print(f'{userMsg} == {msg} is False')

if userMsg.lower() == msg:
    print(f'{userMsg.lower()} == {msg} is True')

else:
    print(f'{userMsg.lower()} == {msg} is False')

if userMsg.upper() == msg:
    print(f'{userMsg.upper()} == {msg} is True')

else:
    print(f'{userMsg.upper()} == {msg} is False')

# Step 10 - Optional step

# Snippet 1
msg = "Save the notebook"

if msg == "have the notebook":
    print("Message was expected")

else:
    print("Message not as epxected")

# Snippet 2
msg = "Save the notebook"
prediction = 'save the notebook'

if msg.lower() == prediction.lower():
    print("Message was expected")

else:
    print("Message not as expected")

# Snippet 3
l_name = input("Enter last name: ")

if l_name.lower() <= "c":
    print("Welcome to the a, b, c line")

else:
    print("Sorry, this is the a, b, c line")

# Step 11

# Collecting user input
answerInput = input('What is 8 + 13?\n\n>>> ')

# Converting user input to an integer and comparing to 8 + 13
if int(answerInput) == 8 + 13:
    print('Congratulations, 8 + 13 is equal to', answerInput)

else:
    print('That\'s unfortunate, but', answerInput, 'is not equal to 8 + 13')


# Step 13

# Defining function tFQuiz that takes in two parameters, question and answer. Prints out True or False accordingly to if question == answer

def tFQuiz(question, answer):
    if question.lower() == answer.lower():
        print("You are correct!")
    
    else:
        print("Sorry you missed that one!")

actualAnswer = "True"
userAnswer = input("Is 8 + 13 equal to 21? 'True' or 'False'\n\n>>> ")

tFQuiz(actualAnswer, userAnswer)
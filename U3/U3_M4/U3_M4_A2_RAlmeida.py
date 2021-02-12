# Program name: U3_M4_A2_RAlmeida.py
# Program purpose: Nested Conditionals
# Created/revised: R. Almeida on 12-03-20

def step(n):
    print(f"\n{'-'*20}\nStep {n}\n{'-'*20}\n")

step(9)

print("""Escape Sequences
\\n = new line
\\t = tab
\\' = single quote
\\" = double quote
\\\ = backslash""")

step(10)

print('Hello World!\nI am formatting print with escape sequences.')

step(11)

print('Hello World!', '\n', 'I am formatting print with escape sequences.')

step(12)

studentAge = 17
studentName = 'Ben Franklin'
print('STUDENT NAME\t\tAGE')
print(studentName, '\t\t' + str(studentAge))

step(13)

print("\"quotes in quotes\"")
print("I\'ve said \"save your notebook,\" so let\'s do it!")

# using \\ (escape sequence backslash)
print("for a new line use \\n")

step(14)

print("\\\\\\WARNING!///")

step(15)

print("\"What\'s that?\" isn\'t a specific question.")

step(16)

print('One\t\tTwo\t\tThree\n\t\tFour\t\tFive\t\tSix')

step(17)

# function preWord takes in one string paremeter word
def preWord(word):
    if word.startswith('pre') and word.isalpha():
        return True
    
    else:
        return False

word = input('Enter a word starting with "pre"\n\n>>> ')

if preWord(word):
    print(f'Nice "{word}" starts with pre')

else:
    print(f'Sorry, "{word}" does not start with pre')

step(18)

# fix 1, add quotes around \n
print("Hello" + "\n" + "World!")

# fix 2, print each line individually
print("Hello")
print("World!")

# fix 3, remove plus signs, and include everything in one string
print("Hello\nWorld!")
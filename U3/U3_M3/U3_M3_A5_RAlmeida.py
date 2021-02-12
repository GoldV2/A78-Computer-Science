# Program name: U3_M3_A5_RAlmeida.py
# Program purpose: Type, and Mathematics Extended
# Created/revised: R. Almeida on 11-26-20

# 8
# review and ru nexample - 'millionmaker'
def millionmaker():
    makeBig = input('Enter a non-decimal number you wish were bigger: ')
    return int(makeBig)*1000000

print('Now you have', millionmaker())

# Step 9
print(43-15)

# Step 10
print(15*43)

# Step 11
print(156/12)

# Step 12
print(21/0.5)

# Step 13
print(111+84-(45*2))

# Step 14
print((21+4)*4)

# Step 15
# function multiply takes in 2 string paremeters, num1 and num2
def multiply(num1, num2):
    if (not num1.isdigit()) or (not num2.isdigit()):
        return 'Your input is not valid.'

    else:
        return f'{num1} * {num2} = {int(num1)*int(num2)}'

num1 = input('Please enter the first number\n\n>>> ')
num2 = input('Enter the second number\n\n>>> ')
print(multiply(num1, num2))

# Step 16
# function multiply takes in 3 string paremeters, num1, num2, operator
def multiply(num1, num2, operator = '*'):
    # Check if num1 and num2 are digits
    if (not num1.isdigit()) or (not num2.isdigit()):
        return 'Your input is not valid.'

    # Check if operator is valid
    elif operator != '*' and operator != '/':
        return 'The operator you are using is invalid.'

    else:
        # Use the function eval to evaluate the expression regardless of operator
        return f'{num1} {operator} {num2} = {eval(num1 + operator + num2)}'

num1 = input('Please enter the first number\n\n>>> ')
num2 = input('Enter the second number\n\n>>> ')
operator = input('Now enter a operator, either * or /\n\n>>> ')
print(multiply(num1, num2, operator))

# Step 17
StudentName = input("Enter name: ").capitalize()

# Wrong variable name, s must be capital
if StudentName.startswith("F"):
    # Wrong variable name, s must be capital. Missing double quotes at the end
    print(StudentName, "Congratulations, names starting with 'F' get to go first today.")

# Missing colon at the end of the elif statement
elif StudentName.startswith("G"):
    # Wrong variable name, s msut be capital. Missing comma between StudentName and string, missing double quotes in the beginning of the string
    # Double quotes must be used at the end so that single quotes can be used inside the string
    print(StudentName, "Congratulations, names starting with 'G' get to go second today.")

else:
    # Incorrect function name prnt(), must be print()
    print(StudentName, "please wait for students with the names starting with 'F' and 'G' to go first today.")
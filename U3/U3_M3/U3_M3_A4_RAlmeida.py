# Program name: U3_M3_A4_RAlmeida.py
# Program purpose: elif and castig
# Created/revised: R. Almeida on 11-23-20

# Step 8
# Checking if user input is valid, if it is display something accordingly
inputSize = input("What size shirt are you? S, M, L\n\n>>> ")

if inputSize.lower() == 's':
    print('Small = $6')

elif inputSize.lower() == 'm':
    print('Medium = $7')

elif inputSize.lower() == 'l':
    print('Large = $8')

else:
    print('The size you are looking for is not available.')

# Step 11
# Using casting to add numbers that are initially in different data types
strNum1 = '11'
strNum2 = '15'
intNum3 = 10

print(int(strNum1) + int(strNum2) + intNum3)

# Step 12
# Intentional Type Error
# print(strNum1 + strNum2 + intNum3)

# Step 13
# Converting and adding numbers that were of different data types
strInteger = '16'
intNumber = 2004
numTotal = int(strInteger) + intNumber

print(numTotal)

# Step 15
# Function calculator takes in no paremeters
# Returns the sum of a and b in string type
def calculator():
    while True:
        a = input('Input a digit\n\n>>> ')
        b = input('Input a second digit\n\n>>> ')

        if a.isdigit() and b.isdigit():
            return 'The sum of ' + str(a) + ' and ' + str(b) + ' is: ' + str(int(a) + int(b))

        else:
            print('One of the inputs were not a digit. Try again.')

print(calculator())

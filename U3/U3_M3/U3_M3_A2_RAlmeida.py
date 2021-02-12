# Program name: U3_M3_A2_RAlmeida.py
# Program purpose: Learning more ifs with conditionals
# Created/revised: R. Almeida on 11-17-20

# Step 8
# Checking if x is equal to 13, if it is, print True

x = 9 + 4

if x == 13:
    print(True)

else:
    print(False)

# Step 9
# Checking if 3 + 3 is greater tahn 2 + 4

if 3 + 3 > 2 + 4:
    print(True)

else:
    print(False)

# Step 10
# Same as Step 9 but must return True

if 3 + 3 >= 2 + 4:
    print(True)

else:
    print(False)

# Step 12
# Defining variable x and y based off of x. Checking if y is greater than or equal to x + x. Return true accordingly.
x = 3
y = x + 8

if y >= x + x:
    print('Y is greater than or equal to x + x is:', True)

else:
    print('Y is greater than or equal to x + x is:', False)
# Program name: U3_M2_A2_RA.py
# Program purpose: Learning how to use return
# Created/revised: R. Almeida on 11-12-20

# Step 8

# Creating a function called makeDoctor that takes in one argument fullName
# returns the variable fullName formatted with the prefix for a doctor
def makeDoctor(fullName):
    return 'Dr. ' + fullName

# Taking in the user's full name as an input
fullName = input('Input full name\n\n>>> ')

# Printing the result of the function
print(makeDoctor(fullName))

# Step 10

# Creating a function called makeSchedule that takes in for arguments
# day, block1, block2, block3, block4
# Returns schedule which is a string that uses formatting to display the user's schedule
def makeSchedule(day, block1, block2, block3, block4):
    schedule = "SCHEDULE\nToday is a " + day + " day\n[1st] " + block1.title() + ", [2nd] " + block2.title() + ', [3rd] ' + block3.title() + ', [4th] ' + block4.title()

    return schedule

# Asking for what school day it is, either A or B
day = input('Is today an A or B day?\n\n>>> ')

# Define each block depending on what day it is
if day.lower() == 'a':
    block1 = 'English'
    block2 = 'Chemistry'
    block3 = 'Computer Science'
    block4 = 'Spanish'

elif day.lower() == 'b':
    block1 = 'History'
    block2 = 'Health'
    block3 = 'Math'
    block4 = 'Business'

# Printing the result of makeSchedule
print(makeSchedule(day, block1, block2, block3, block4))

# Step 11

# Creating a function called personalInfo that takes in 5 arguments
# myName, age, numSiblings, favVacation, favActivity
# Returns ouput which is the parameters in a formatted string
def personalInfo(myName, age, numSiblings, favVacation, favActivity):
    output = '---------\nInfo About ' + myName + ':\n---------'+ '\nAge: ' + age + '\nSiblings: ' + numSiblings + '\nFavorite Vacation: ' + favVacation + '\nFavorite Activity: ' + favActivity

    return output

# Printing the result of the function above
print(personalInfo('Rafael Almeida', '15', '3', 'Brazil', 'Coding'))

# Program name: U1_M1_A6_RA.py
# Program purpose: input
# Created/revised: R. Almeida on 10-22-20

# 3
studentName = input("What is your name?\n\n>>> ")

# 4
print(f'The data type for {studentName} variable is: {type(studentName)}')

# 6
city = input("Enter the name of a city:\n\n>>> ")

# 7
print('The city name is: ' + city)

# 8
name = input("What is your name?\n\n>>> ")
age = int(input("What is your age?\n\n>>> "))
getMail = input("Do you want to receive emails?\n\n>>> ").lower()

if getMail == 'yes':
    print(f'Thank you {name}. You are {age}. You want to receive e-mails')

elif getMail == 'no':
    print(f'Thank you {name}. You are {age}. You do not want to receive e-mails')
    
else:
    print(f'Thank you {name}. You are {age}. Maybe you will receive emails :P')

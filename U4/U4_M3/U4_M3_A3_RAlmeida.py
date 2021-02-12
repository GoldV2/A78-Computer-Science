# File Name: U4_M3_A3_RAlmeida.py
# Purpose: Iteration and Extension
# Edited - Revised: 01/04/21

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

step(12, 'Common & Seen')

common_birds = ['Chicken', 'Blue Jay', 'Crow', 'Pigeon']
print(common_birds)
# creating list of seen birds
seen_birds = ['Toucan']
# printing list of see nbirds
print(seen_birds)
# extending common_brirds with seen_birds
common_birds.extend(seen_birds)
print(common_birds)

step(13, 'All Num')

# creating a list from 0 to 9
zero_nine = list(range(10))
# creating a list from 10 to 100 skipping by tens
ten_hundred = list(range(10, 101, 10))
# adding the lists together and printing
print(ten_hundred + zero_nine)
# extending the list
ten_hundred.extend(zero_nine)
print(ten_hundred)

step(18, 'Multi of 5')

# creating a list starting from five to 100 skipping by fives
multi_of_5 = list(range(5, 101, 5))
print(multi_of_5)
# reversing the list
multi_of_5.reverse()
print(multi_of_5)

step(19, 'Mirrored List')

# creating a list from 4 to 44 skipping by fourss
fours = list(range(4, 45, 4))
# there is no need to create another list
# creating a reversed version and adding the original to it 
# I could have used fours[::-1]
print(sorted(fours, reverse=True) + fours)

step(24, 'Visited Cities')

visitedCities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# printing the sorted cities
# the directions are not very clear, you cannot print a city using .sort() it will print a None object.
visitedCities.sort()
print(visitedCities)
# using a one line for loop that creates another list with all the cities that are less than or equal to 'q'
print([city for city in visitedCities if city.lower() <= 'q'])

step(25, 'Sorted Cities')

# instead of sorting visitedCities in place on the previous step, you couldve printed it sorted by using sorted()
# this would remove the need to redefine it in this step
visitedCities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# using a one line for loop to create a sorted version of visitedCities excluding every city with a name with less than or with 5 letters
sorted_cities = sorted([city for city in visitedCities if len(city) > 5])
# this is why you cant sort visitedCities in place, you must use it here as it is unsorted
print(visitedCities)
print(sorted_cities)

step(26, 'Add Animals')

animals = ['Chimpanze', 'Panther', "Wolf", 'Armadillo']

# initializing variable
add_animals = []
while True:
     # asking for using input
     inp = input('Please enter an animal. Press enter without typing anything to quit\n\n>>> ')
     
     # checking if the input is not empty
     if inp:
          # if it isn't append to add_animals
          add_animals.append(inp)
          # skip this iteration
          continue

     # if it is empty, break the loop
     break

# extending animals with add_animals
animals.extend(add_animals)

# asking the user to either enter 1 for soorted list or 2 for reverse sorted
# keep asking until input is valid
while True:
     order = input('Enter "1" to view sorted list, enter "2" to view reverse sorted list\n\n>>> ')

     if order == '1':
          print(sorted(animals))

     elif order == '2':
          print(sorted(animals, reverse=True))

     else:
          print("Sorry, can't understand. Try again")
          continue

     break
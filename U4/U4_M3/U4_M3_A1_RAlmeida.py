# File Name: U4_M3_A1_RAlmeida.py
# Purpose: List Iteration
# Edited - Revised: 01/11/21

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

step(8)

# [ ] review and run example
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo",
"Hyderabad"]
for city in cities:
    print(city)

step(9)

# [ ] review and run example
sales = [
6, 8, 9, 11, 12, 17, 19, 20, 22]
total = 0
for sale in sales:
    total += sale
print("total sales:", total)

step(10)

# [ ] review and run example
sales = [6, 8, 9, 11, 12, 17, 19, 20, 22]
total = 0

for dollar in sales:
     total += dollar

print('Total sales:', total)

step(11, 'Birds')

birds = ['Parrots', 'Columbidae', 'Owl', 'Finches', 'Penguins']

for bird in birds:
     print(bird)

step(12, 'Player Points')

player_points = list(range(7))
for point in player_points:
     print(point*2)

step(13, 'Bird String')

string = ''
for bird in birds:
     string += bird + ' '

print(string)

step(15)

# [ ] review and run example of sorting into strings to display
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate", "cuneiform", "medial cuneiform"]
longer_names = ""
shorter_names = ""
for bone_name in foot_bones:
     if len(bone_name) < 10:
          shorter_names += "\n" + bone_name
     else:
          longer_names += "\n" + bone_name

print(shorter_names)
print(longer_names)

step(16)

# [ ] review and run example of sorting into lists
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate", "cuneiform", "medial cuneiform"]
longer_names = []
shorter_names = []
for bone_name in foot_bones:
     if len(bone_name) < 10:
          shorter_names.append(bone_name)
     else:
          longer_names.append(bone_name)

print(shorter_names)
print(longer_names)

step(17, 'M Cities')

for city in cities:
     # checking if the item in lowercase starts with lowercase M
     if city.lower().startswith('m'):
          print(city)

step(18, 'A & No A Cities')

a_city = []
no_a_city = []

for city in cities:
     if 'a' in city.lower():
          a_city.append(city)

     else:
          no_a_city.append(city)

print(a_city)
print(no_a_city)

step(20)

# [ ] review and run example
# iterates the "cities" list, count & sum letter "a" in each city name
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo",
"Hyderabad"]
search_letter = "a"
total = 0
for city_name in cities:
     total += city_name.lower().count(search_letter)

print("The total # of \"" + search_letter + "\" found in the list is", total)

step(22)

# [ ] review and run example
# city_search function has a default list of cities to search
def city_search(search_item, cities = ["New York", "Shanghai", "Munich", "Tokyo"] ):
     for city in cities:
          if city.lower() == search_item.lower():
               return True
          else:
               # go to the next item
               pass
     
     # no more items in list
     return False
# a list of cities
visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
search = input("enter a city visited: ")
# Search the default city list - remember why?
print(search, "in default cities is", city_search(search))
# search the list visited_cities using 2nd argument
print(search, "in visitied_cites list is", city_search(search, visited_cities))

step(23, 'Paint Colors')

colors = ['red', 'green', 'blue', 'orange', 'yellow']

inp = input(f'Please search for a color. \n\n>>> ')

# There is no need to use a loop in this case. It would just be a bad practice to do so
if inp.lower() in colors:
     print('Color found!')

else:
     print('Color not found :(')

step(24, 'Foot Bones')

def find_bone(bone, bones_identified):
     if bone.lower() in foot_bones:
          print(f'Congratulations, {foot_bones.pop(foot_bones.index(bone))} was present')
          bones_identified += 1

     else:
          print(f'Incorrect, {bone} is not present')

     print(f'Bones Identified: {bones_identified}')
     return bones_identified

bones_identified = 0
bones_identified = find_bone('talus', bones_identified)
bones_identified = find_bone('talus', bones_identified)

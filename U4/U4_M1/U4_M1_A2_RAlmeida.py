# Program name: U4_M1_A2_RAlmeida.py
# Program purpose: Sequence Manipulation
# Created/revised: R. Almeida on 12-17-20

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

# assign string to studentName
studentName = "Colette"
# addressing the 3rd, 4th and 5th characters using a slice
print("slice studentName[2:5]:",studentName[2:5])
# answer: “slice studentName[2:5]: let
# assign string to studentName
studentName = "Colette"
# addressing the 3rd, 4th and 5th characters individually
print("index 2, 3 & 4 of studentName:", studentName[2] + studentName[3] + studentName[4])

longWord = 'Acknowledgement'
print(longWord[2:11])
print(longWord[2:11], "is the 3rd char through the 11th char")
print(longWord[2:11], "is the index 2, \"" + longWord[2] + "\",", "through index 10, \"" +
longWord[10] + "\"")

step(9, 'Characteristics')

long_word = 'Characteristics'
# printing act
print(long_word[4:7])
# printing tic
print(long_word[11:14])

step(10, 'Consequences')

long_word = 'Consequences'
print(long_word[3:-1])

step(12)

studentName = "Colette"
# addressing the 1st, 2nd and 3rd characters
print(studentName[:3])

step(13, 'First Half of Word')

long_word = 'Consequences'
# to print the first half of a word just print up to the length of the word divided by 2
print(long_word[:int(len(long_word)/2)])

step(15)

studentName = "Colette"
# addressing the 4th, 5th, 6th and 7th characters
print(studentName[3:])

step(16, 'Second Half of Word')

long_word = 'Consequences'
# to print the last half of a word just print everything after the index of half of the length of that word
print(long_word[int(len(long_word)/2):])

step(18)

studentName = "Colette"
# return all
print(studentName[:])
# return every other letter
print(studentName[::2])
# return every third, starting at 2nd character
print(studentName[1::2])
# return every other character, starting at index 1 and ending at 9th character
longWord = "Consequences"
print(longWord[1:9:2])

step(19, 'Acknowldgement')

long_word = 'Acknowldgement'
# every third letter
print(long_word[::3])

step(20, 'Acknowldgement 2')

# every other letter starting from the third letter
print(long_word[2::2])

step(22)

long_word = "characteristics"
# make the step increment -1 to step backwards
print(long_word[::-1])
# start at the 7th letter and go backwards to the start
print(long_word[6::-1])

step(23, 'Stressed')

new_word = 'stressed'
# printing backwards
print(new_word[::-1])

step(24, long_word)

# printing everything before the 4 index backwards
print(long_word[4::-1])

step(25, 'Timeline')

fun_word = 'Timeline'
print(fun_word[:4])

step(26, 'Reversed Timeline')

# printing everything before and including the third index backwards
print(fun_word[3::-1])

step(27, 'End of Timeline')

# to print the last n characters of a string, calculate the length of the string and remove n from it
print(fun_word[len(fun_word)-4:])

step(28, 'Middle of Timeline')

# including index 3 and index 6
print(fun_word[7:3:-1])

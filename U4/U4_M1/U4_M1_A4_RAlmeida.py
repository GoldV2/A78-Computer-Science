# Program name: U4_M1_A4_RAlmeida.py
# Program purpose: Iterate a String by Character
# Created/revised: R. Almeida on 12-23-20

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

workTip = "save your code"
print("number of characters in string")
print(len(workTip),"\n")
print('letter "e" occurrences')
print(workTip.count("e"),"\n")
print("find the index of the first space")
print(workTip.find(" "),"\n")
print('find the index of "u" searching a slice workTip[3:9] -', workTip[3:9])
print(workTip.find("u",3,9),"\n")
print('find the index of "e" searching a slice workTip[4:] -', workTip[4:])
print(workTip.find("e",4))
workTip = "good code is commented code"
print("The sentence: \"" + workTip + "\" has character length = ", len(workTip) )
# .len() examples
# find the middle index
workTip = "good code is commented code"
midPt = int(len(workTip)/2)
# print 1st half of sentence
print(workTip[:midPt])
# print the 2nd half of sentence
print(workTip[midPt:])
# .count() examples
print(workTip)
print("how many w's? ", workTip.count("w"))
print("how many o's? ", workTip.count("o"))
print("uses 'code', how many times? ", workTip.count("code"))
print(workTip[:midPt])
print("# o's in first half")
print(workTip[:midPt].count("o"))
print()
print(workTip[midPt:])
print("# o's in second half")
print(workTip[midPt:].count("o"))
# .find() examples:  .find(string, start index, end index)
workTip = "good code has meaningful variable names"
print(workTip)
# index where first instance of "code" starts
codeHere = workTip.find("code")
print(codeHere, '= starting index for "code"')
#set start index = 13 and end index = 33
print('search for "meaning" in the sub-string:', workTip[13:33],"\n")
meaningHere = workTip.find("meaning",13,33)
print('"meaning" found in workTip[13:33] sub-string search at index', meaningHere)
# if .find("o") has No Match, -1 is returned
print ("workTip:" , workTip)
location = workTip.find("o")
# keeps looping until location = -1 (no "o" found)
while location >= 0:
   print("'o' at index =", location)
   # find("o", location + 1) looks for a "o" after index the first "o" was found
   location = workTip.find("o", location + 1)
print("no more o's")

step(9, 'Half of Tip')

random_tip = 'wear a hat when it rains'
# finding the half way by doing whole number division with the length of random_tip
half = len(random_tip)//2
print(f'First half of the tip is: {random_tip[:half]}')
print(f'Second half of the tip is: {random_tip[half:]}')

step(10, 'A&E Frequency')

# finding freq of a
a_freq = random_tip.count('a')
# finding freq of e
e_freq = random_tip.count('e')
print(f'Frequency of "a" is {a_freq}')
print(f'Frequency of "e" is {e_freq}')
# deciding which one is most frequent
print(f'The most frequent letter is {"a" if a_freq > e_freq else "e"}')

step(11, 'Juxtaposition Ts')

long_word = 'juxtaposition'
# finding first t
t_1 = long_word.find('t')
# finding first t starting at the index after t_1
t_2 = long_word.find('t', t_1+1)
# printing including both ts
print(long_word[t_1:t_2+1])

step(12, 'Quoting')

# This is probably the worst code I have ever created.
# The starting code is not intuitive at all, or I simply did not understand it.
# Mrs. Patil, please change the instructions for this program.
# Please teach other data types like lists, tuples, and dictionaries earlier on as well. They are not hard to understand
def add_quotes(quote):
     start = 0
     space_index = quote.find(' ')
     while space_index != -1:
          print('"' + quote[:space_index] + '"')
          quote = quote[space_index+1:]
          space_index = quote.find(' ')

     print('"' + quote + '"')

add_quotes('they stumble who run fast')

step(12, 'Better Way')
# How it should be done
def add_quotes(quote):
     for word in quote.split(' '):
          print('"' + word + '"')

add_quotes('they stumble who run fast')
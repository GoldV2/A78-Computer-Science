from itertools import product
import os

# define the products
# this can be changed to an input so that the user can enter any product
products = 'banana, battery, bread, candy bar, chip, coffee, cookie, diaper, egg, formula, ice cream, milk, mustard, paper, paper towel, pencil, whipped cream'.split(', ')

###
# returns
###
# receipts:2D list
###
# each item in the first list represents the individual receipts
# each item in a receipt is a string of the name of the item bought
# checks if any item the user inputs does not exist
def take_input():
    receipts = []
    while True:
        l = input('Enter item names in singular form and separated by a comma and a space. Enter nothing to quit\n\n>>> ').split(', ')
        if l == ['']:
            break
    
        l_set = set(l)
        inter = l_set&set(products)
        if l_set != inter:
            print(f'The items: {", ".join([item for item in list(l_set)+list(inter) if item not in inter])}, are not valid. The program will be terminated')
            input('Press enter to terminate the program')
            exit()

        receipts.append(l)

    return receipts

###
# returns
###
# freq:dictionary
###
# returns a dictionary that has tuples of two strings as keys and integers as values
# the strings in the tuples are the name of the items
# the dictionary represents how many times the combination of products in the tuple appears in the receipts
def format_freq():
    groups = list(product(products, products))
    freq = {}
    for comb in groups:
        if comb[0] == comb[1]:
            pass

        elif (comb[1], comb[0]) in freq:
            pass

        else:
            freq[comb] = 0

    return freq

###
# returns
###
# table: 2D list
###
# the list will be used to write to the file
# the list contains N+1 lists with N+1 items, where N is the number of products.
# the first list is a header with all the names of the products
# the first item of the other lists is the name of a product
# the rest of the items are integers that represent the frequency that the product in their row and column were bought together
def format_table():
    table = [list(products)]
    for product in products:
        table.append([product]+(['']*len(products)))

    return table

###
# parameters
###
# freq:dictionary
# receipts:2D list
###
# loops through all the receipts
# for every item in a receipt, it loops through all the items in that same receipt 
    # and checks if the combination of those two items is present in the freq dictionary.
    # If it is, increments the value of the tuple key with both the item names
def fill_freq(freq, receipts):
    for receipt in receipts:
        for item in receipt:
            for item2 in receipt:
                if (item, item2) in freq:
                    freq[(item, item2)] += 1

###
# parameters
###
# freq:dictionary
# table:2D list
###
# loops through all the combination of products in the freq dictionary
# finds the coordinate of the cell that is in the corresponding row and column given the combination of products in the table 2D list
# then gives that cell the value found in the freq dictionary
def fill_table(freq, table):
    for comb in freq:
        table[products.index(comb[0])+1][products.index(comb[1])+1] = freq[comb]

###
# parameters
###
# table:2D list
###
# finds the path to the user's desktop folder and creates a .xls file
# writes to the file the items in the table list formatted properly with \t and \n
def create_file(table):
    user = os.path.expanduser('~')
    filename = f'{user}\\Desktop\\Receipts Analysis Results.xls'
    file = open(filename, 'w')
    file.write('\t')
    for row in table:
        for column in row:
            file.write(str(column) + '\t')

        file.write('\n')

receipts = take_input()
freq = format_freq()
table = format_table()
fill_freq(freq, receipts)
fill_table(freq, table)
create_file(table)
print('File was created with success. Locate the file "Receipts Analysis Results.xls" in your Desktop.')
input('Press enter to terminate the program')

# example input
# candy bar, coffee, ice cream, milk, egg, chip, paper towel, mustard
# egg, cookie, ice cream, milk, whipped cream, paper towel, mustard, bread
# diaper, ice cream, mustard, chip, whipped cream, candy bar, paper towel
# paper, battery, pencil, candy bar, milk, ice cream, chip, cookie
# formula, banana, diaper, milk, cookie, whipped cream, paper towel
# chip, coffee, egg, milk, cookie, formula, mustard
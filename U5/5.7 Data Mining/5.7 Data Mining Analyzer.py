from itertools import product
import os

# define the groups
products = tuple('banana, battery, bread, candy bar, chip, coffee, cookie, diaper, egg, formula, ice cream, milk, mustard, paper, paper towel, pencil, whipped cream'.split(', '))
products = tuple('bread, milk, rice, flour, egg, syrup'.split(', '))
def take_input():
    receipts = []
    while True:
        l = input('Enter item names in singular form and separated by a comma and a space. Enter nothing to quit\n\n>>> ').split(', ')
        if l == ['']:
            break
    
        receipts.append(l)

    return receipts

def format_pairs():
    groups = list(product(products, products))
    table = {}
    for comb in groups:
        if comb[0] == comb[1]:
            pass

        elif (comb[1], comb[0]) in table:
            pass

        else:
            table[comb] = 0

    return table

def format_result():
    result = [list(products)]
    for product in products:
        result.append([product]+(['']*len(products)))

    return result

def fill_pairs(table, receipts):
    for receipt in receipts:
        for item in receipt:
            for item2 in receipt:
                if (item, item2) in table:
                    table[(item, item2)] += 1

def fill_result(table, result):
    for comb in table:
        for row in result:
            for column in row:
                result[products.index(comb[0])+1][products.index(comb[1])+1] = table[comb]

def create_file(result):
    user = os.path.expanduser('~')
    filename = f'{user}\Desktop\Results.xls'
    file = open(filename, 'w')
    file.write('\t')
    for row in result:
        for column in row:
            file.write(str(column) + '\t')

        file.write('\n')

receipts = take_input()
table = format_pairs()
result = format_result()
fill_pairs(table, receipts)
fill_result(table, result)
create_file(result)
print('File was created with success. Locate the file "Results.txt" in your Desktop folder.')
print('Simply select the whole file and paste it into a spreadsheet.')
input('Press enter to terminate the program')

# example input
# candy bar, coffee, ice cream, milk, egg, chip, paper towel, mustard
# egg, cookie, ice cream, milk, whipped cream, paper towel, mustard, bread
# diapers, ice cream, mustard, chips, cream, candy bar, paper towel
# paper, battery, pencils, candy bar, ice cream, chip, cookie
# formula, banana, diaper, milk, cookie, whipped cream, paper towel
# chip, coffee, egg, milk, cookie, formula, mustard
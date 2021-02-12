# Program name: U3_M2_PS3_RAlmeida.py
# Program purpose: Problem Set 3
# Created/revised: R. Almeida on 11-19-20

# fishStore takes in one string parameter, and two float paremeters
# calculate quanity times price
# returns a multiline, formatted string with fish, quantity, and price & total formatted to 2 decimal places
def fishStore(fish, quantity, price):
    total = quantity*price
    return f"""
Type of fish: {fish}
Quantity: {quantity}
Cost per unit: ${price:.2f}
Total: ${total:.2f}
"""

# Collecting user input
fish = input('Enter the type of fish\n\n>>> ').title()

# Looping the user until they input a valid float
while True:
    try:
        # This variable fake was used so that I could access whatever the user inputted to show them what is not valid
        fake = input('Enter the quantity you are buying\n\n>>> ')
        # The float function is what is expected to output an error
        quantity = float(fake)
        break

    except Exception:
        # Note that I use fake instead of quantity
        print(f"Sorry, {fake} is not a valid quantity. Please try again.")

# Same as above
while True:
    try:
        fake = float(input(f"Enter the price of each unit of {fish}\n\n>>> "))
        price = float(fake)
        break

    except Exception:
        print(f"Sorry, {fake} is not a valid price. Please try again.")

# calling fishStore withing a print statement, with fish, quantity, and price as the arguments
print(fishStore(fish, quantity, price))

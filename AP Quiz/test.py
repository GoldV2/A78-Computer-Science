from math import tan, radians

def solve_right_triangle():
    situation = int(input('0: if you have 2 legs\n0: if you have one leg and the hypotenuse\n\n>>> '))

    if situation == 0:
        a = float(input('Input the length of the first leg\n\n>>> '))
        b = float(input('Input the length of the second leg\n\n>>> '))

        c = ((a**2) + (b**2))**(1/2)

        return f'The hypotenuse measures: {c} units'

    elif situation == 1:
        a = float(input('Input the length of the leg\n\n>>> '))
        c = float(input('Input the length of the hypotenuse\n\n>>> '))

        b = ((c**2) - (a**2))**(1/2)

        return f'The second leg measures: {b} units'

    else:
        print('Sorry, your situation is not valid.')
        solve_right_triangle()

def solve_quadratic():
    a = float(input('What is the value of the second degree term?\n\n>>> '))
    b = float(input('What is the value of the first degree term?\n\n>>> '))
    c = float(input('What is the value of the constant term?\n\n>>> '))

    result = (-b + ((b**2) + (-4*a*c))**(1/2))/(2*a)
    result2 = (-b - ((b**2) + (-4*a*c))**(1/2))/(2*a)

    return 'The first result is:', result, '\nThe second result is:', result2

def solve_area():
    n = int(input('How many sides does the polygon have?\n\n>>> '))
    s = float(input('What is the length of one side?\n\n>>> '))

    a = (s/2)/tan(radians(360/n/2))
    A = (n*s*a)/2

    return f'The area of the {n}-sided polygon is equal to: {round(A, 3)}'

print(solve_area())

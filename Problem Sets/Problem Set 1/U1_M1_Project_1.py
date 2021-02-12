def food_check():
    FOODS = ['dairy', 'cake', 'nut', 'chicken', 'carrot']
    
    input_test = input('Write 5 foods you ate in the last 24 hours, separated by a comma\n\n>>> ').lower()

    true_output = f"It is True that \"{input_test}\" contains \""
    false_output = f"It is False that \"{input_test}\" contains \""

    for food in FOODS:
        if food in input_test:
            true_output += food + ', '

        else:
            false_output += food + ', '

    return true_output[:-2] + "\".\n" + false_output[:-2] + "\"."

print(food_check())
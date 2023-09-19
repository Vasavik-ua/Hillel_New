def prep_check(input):
    if (input.find('-')) >= 0:
        input = input.replace('-', '', 1)
    if (input.find(',')) >= 0:
        input = input.replace(',', '.')
    if (input.find('.')) >= 0:
        input = input.replace('.', '', 1)
    return  input

print(prep_check('-1,03'))
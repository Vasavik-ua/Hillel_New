def exit_quest(val):  # Check input value for exit.
    check_list = ["вихід", "exit", "quit", "e", "q"]
    for item in range(len(check_list)):
        if check_list[item] == (val.lower()):
            return True
    return False


def prep_check(input):
    if (input.find('-')) >= 0:
        input = input.replace('-', '', 1)
    if (input.find('.')) >= 0 or (input.find(',')) >= 0:
        if (input.find('.')) >= 0:
            input = input.replace('.', '', 1)
        else :
            input = input.replace(',', '', 1)
    return input

def check_isdigit(value):  # check the value and outcome the result.
    new_value = prep_check(value)
    result = ''
    if new_value.isdigit():
        if value == '0':
            new_zero = f'Ви ввели нуль: {value}'
            return new_zero
        if value[:1] == '-':
            result = result + '''Ви ввели від'ємне '''
        else:
            result = result + 'Ви ввели позитивне '
        if (value.find('.')) >= 0 or (value.find(',')) >= 0:
            result = result + 'дробове число: '
        else:
            result = result + 'ціле число: '
        if value[:1] == '-' and value[1:2] == '.':
                result = result + (f'-0.{new_value}')
                return result
        elif value[:1] == '.':
            result = result + (f'0.{new_value}')
            return result
        return result + f'{value}'
    else:
        return False


while True:
    input_value = input('Number required: ')
    if exit_quest(input_value):
        break
    if not check_isdigit(input_value):
        print(f'Ви ввели неправильне число: {input_value}')
        pass
    else:
        print(check_isdigit(input_value))
        break

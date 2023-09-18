def exit_quest(val):  # Check input value for exit.
    check_list = ["вихід", "exit", "quit", "e", "q"]
    for item in range(len(check_list)):
        if check_list[item] == (val.lower()):
            return True
    return False


def check_isdigit(value):  # check the value and outcome the result.
    new_value = value
    if (new_value.find('-')) >= 0:
        new_value = new_value.replace('-', '', 1)
    if (new_value.find('.')) >= 0 or (new_value.find(',')) >= 0:
        if (new_value.find('.')) >= 0:
            new_value = new_value.replace('.', '', 1)
        else:
            new_value = new_value.replace(',', '', 1)
    if new_value.isdigit():
        if value == '0':
            new_zero = f'Ви ввели нуль: {value}'
            return new_zero
        if value[:1] == '-':
            if (value.find('.')) >= 0 or (value.find(',')) >= 0:
                if value[1:2] == '.' or value[1:2] == ',':
                    new_minus = f'''Ви ввели від'ємне дробове число: -0.{new_value}'''
                    return new_minus
                else:
                    new_minus = f'''Ви ввели від'ємне дробове число: {value}'''
                    return new_minus
            else:
                new_minint = f'''Ви ввели від'ємне ціле число: {value}'''
                return new_minint
        else:
            if (value.find('.')) >= 0 or (value.find(',')) >= 0:
                if value[:1] == '.' or value[:1] == ',':
                    new_intper = f'''Ви ввели позитивне дробове число: 0.{new_value}'''
                    return new_intper
                else:
                    new_intdb = f'Ви ввели позитивне дробове число: {value}'
                    return new_intdb
            else:
                new_int = f'Ви ввели позитивне ціле число: {value}'
                return new_int
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

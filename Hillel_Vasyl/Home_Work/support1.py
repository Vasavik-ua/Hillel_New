def check_isdigit(value):  # check the value and outcome the result.
    new_value = prep_check(value)
    result = ''
    if new_value.isdigit():
        if new_value == '0':
            new_zero = f'Ви ввели нуль: {new_value}'
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
        elif value[:1] == '.' or value[:1] == ',':
            result = result + (f'0.{new_value}')
            return result
        return result + f'{value}'
    else:
        return False
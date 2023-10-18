from datetime import date
from datetime import datetime


class Person:
    NAME = []
    SURNAME = []
    SEC_SURNAME = []
    DATE_OF_BIRTH = []
    DATE_OF_DEATH = []
    GENDER = []
    AGE = []
    INIT_TABLE = ['NAME', 'SURNAME', 'SEC_SURNAME',
                  'DATE_OF_BIRTH', 'DATE_OF_DEATH',
                  'GENDER', 'AGE']

    @classmethod
    def init_table(cls, shee):
        for row_id, value in enumerate(cls.INIT_TABLE):
            cell = shee.cell(row=1, column=row_id + 1)
            cell.value = value

    @classmethod
    def table_crea(cls, shee):
        rows = shee.max_row
        for item, value in enumerate(cls.NAME):
            cell = shee.cell(row=(rows + item + 1), column=1)
            cell.value = value

        for item, value in enumerate(cls.SURNAME):
            cell = shee.cell(row=(rows + item + 1), column=2)
            cell.value = value

        for item, value in enumerate(cls.SEC_SURNAME):
            cell = shee.cell(row=(rows + item + 1), column=3)
            cell.value = value

        for item, value in enumerate(cls.DATE_OF_BIRTH):
            cell = shee.cell(row=(rows + item + 1), column=4)
            cell.value = value

        for item, value in enumerate(cls.DATE_OF_DEATH):
            cell = shee.cell(row=(rows + item + 1), column=5)
            cell.value = value

        for item, value in enumerate(cls.GENDER):
            cell = shee.cell(row=(rows + item + 1), column=6)
            cell.value = value

        for item, value in enumerate(cls.AGE):
            cell = shee.cell(row=(rows + item + 1), column=7)
            cell.value = value

    @staticmethod
    def print_search_result(find_value, age_func):
        ret_val = []
        gg_val = ''
        for i in find_value:
            final_print = []
            final_print.append(f'{i[0].title()} ')
            if not i[1] == None:
                final_print.append(f'{i[1].title()} ')
            if not i[2] == None:
                final_print.append(f'{i[2].title()} ')
            final_print.append(f'{i[6]} ')
            final_print.append(f'{age_func(str(i[6]))}, ')
            if ((i[5]).lower()) == 'm' and (not i[4] == None):
                final_print.append(f'чоловік. Народився {i[3]}. Помер {i[4]}.')
            elif ((i[5]).lower()) == 'm' and i[4] == None:
                final_print.append(f'чоловік. Народився {i[3]}.')
            if ((i[5]).lower()) == 'f' and (not i[4] == None):
                final_print.append(f'жінка. Народилася {i[3]}. Померла {i[4]}.')
            elif ((i[5]).lower()) == 'f' and i[4] == None:
                final_print.append(f'жінка. Народилася {i[3]}.')

            ret_val.append(final_print.copy())
            final_print.clear()
        for item in ret_val:
            gg_val = gg_val + ''.join(map(str, item)) + '\n'
        return gg_val

    @staticmethod
    def age_word(val):
        if len(val) > 1 and (11 <= int(val[-2:]) <= 20):
            return 'років'
        else:
            tex = val[-1:]
            result_qty = lambda tik: 'рік' if int(tik) == 1 else 'роки' if 2 <= int(tik) <= 4 else 'років'
            return result_qty(tex)

    @staticmethod
    def result_of_search(val, sheet, col):  # Val:array;
        find_value = []
        for v in range(len(val)):
            row_list = []
            for i in range(col):
                cell = sheet.cell(row=int(list(val)[v]), column=i + 1)
                row_list.append(cell.value)
            find_value.append(row_list.copy())
            row_list.clear()
        return find_value

    @staticmethod
    def search_row(rows, col, sheet, val):
        array1 = []
        for item in range(col):
            for i in range(rows):
                cell = sheet.cell(row=i + 2, column=item + 1)
                x = (str(cell.value.lower()).find(val.lower()))
                if x < 0:
                    pass
                else:
                    array1.append(i + 2)
        return array1

    @staticmethod
    def check_age(data, other):  # Insert the date
        if other == '':
            dat = date.today()
            dat_t = dat.strftime("%d/%m/%Y")
            age = Person.age_generator(data, dat_t)
            return age
        else:
            age = Person.age_generator(data, other)
            return age

    @staticmethod
    def age_generator(data, other):  # Insert the date
        dat_new = Person.data_split(other)
        new_l = Person.data_split(data)
        if len(new_l[2]) == 2 and len(dat_new[2]):
            new_l[2] = '20' + new_l[2]
            dat_new[2] = '20' + dat_new[2]
        age = int(dat_new[2]) - int(new_l[2])
        if int(dat_new[1]) < int(new_l[1]):
            age -= 1
        elif int(dat_new[1]) == int(new_l[1]):
            if int(dat_new[0]) < int(new_l[0]):
                age -= 1
        return age

    @staticmethod
    def data_split(values):
        sym_v = ''
        for val in values:
            if not val.isdigit():
                sym_v += val
                break
        dat_new = values.split(sym_v)
        return dat_new

    @staticmethod
    def print_errors(errors):
        gg_val = ''
        for item in errors:
            gg_val = gg_val + ''.join(map(str, item)) + '\n'
        return gg_val

    @staticmethod
    def input_str(array):
        for i in array:
            if not i.isalpha():
                return False
        return True

    @staticmethod
    def check_data(data):
        days_bas_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                          7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
                          }
        year = datetime.now().year
        sym_val = ''
        try:
            for val in data:
                if not val.isdigit():
                    sym_val += val
                    break
            new_l = data.split(sym_val)  # Data today
            if year >= int(new_l[2]):
                if 12 >= int(new_l[1]) > 0:
                    if int(new_l[2]) % 2 in (0,):
                        days_bas_month[2] = 29
                    if 0 < int(new_l[0]) <= days_bas_month[int(new_l[1])]:
                        return new_l
                    else:
                        raise Exception
                else:
                    ...
                    raise Exception
            else:
                raise Exception
        except Exception:
            return False

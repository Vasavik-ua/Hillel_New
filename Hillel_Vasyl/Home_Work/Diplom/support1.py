import openpyxl

wb = openpyxl.load_workbook('DiploM.xlsx')
sheet = wb['Diplom Work']
rows = (sheet.max_row - 1)
col = sheet.max_column
a = 'e'
array1 = []
for i in range(rows):
    cell = sheet.cell(row=i+2, column=1)
    x = (str(cell.value).find(a))
    if x < 0:
        pass
    else:
        array1.append(i+2)
for i in range(rows):
    cell = sheet.cell(row=i+2, column=2)
    x = (str(cell.value).find(a))
    if x < 0:
        pass
    else:
        array1.append(i+2)
for i in range(rows):
    cell = sheet.cell(row=i+2, column=3)
    x = (str(cell.value).find(a))
    if x < 0:
        pass
    else:
        array1.append(i+2)

array1 = sorted(set(array1))
find_value = []
for v in range(len(array1)):
    row_list = []
    for i in range(col):
        cell = sheet.cell(row=int(list(array1)[v]), column=i+1)
        row_list.append(cell.value)
    find_value.append(row_list.copy())
    row_list.clear()

print(find_value)


def age_word(x):
    t = x[-1:]
    result_qty = lambda t: 'рік' if int(t) == 1 else 'роки' if 2 <= int(t) <= 4 else 'років'
    return result_qty(t)


final_print = []
for i in find_value:
    final_print.append(i[0])
    if not i[1] == None:
        final_print.append(i[1])
    if not i[2] == None:
        final_print.append(i[2])
    final_print.append(i[6])
    final_print.append(f'{age_word(str(i[6]))}, ')
    if ((i[5]).lower()) == 'm' and (not i[4] == None):
        final_print.append(f'чоловік. Народився {i[3]}. Помер {i[4]}.')
    elif ((i[5]).lower()) == 'm' and i[4] == None:
        final_print.append(f'чоловік. Народився {i[3]}.')
    if ((i[5]).lower()) == 'f' and (not i[4] == None):
        final_print.append(f'жінка. Народилася {i[3]}. Померла {i[4]}.')
    elif((i[5]).lower()) == 'f' and i[4] == None:
        final_print.append(f'жінка. Народилася {i[3]}.')


print(final_print)

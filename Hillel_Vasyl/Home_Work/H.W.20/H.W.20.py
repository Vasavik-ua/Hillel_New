import openpyxl
import csv


with open('h.m.19.csv', mode='r', encoding='utf-8') as f:
  reader = csv.reader(f, delimiter=',')
  new_data = []
  for item in reader:
    new_data.append(item)


def search_val(val):  # val = search element.
  for item in range(len(new_data)):
    for value in range(len(new_data[item])):
      if new_data[item][value].lower() == val.lower():
        return value


def delete_serch(val):
  for item in new_data:
    delete_items = item.pop(val)
  return new_data


id_search = (search_val('age'))
new_array = delete_serch(id_search)

woork_book = openpyxl.Workbook()
woork_book.create_sheet(title='First sheet', index=0)
sheet = woork_book['First sheet']

for row_id, row in enumerate(new_array):
  for col_id, value in enumerate(row):
    cell = sheet.cell(row=row_id + 1, column=col_id + 1)
    cell.value = value

woork_book.save('h.w.20.xlsx')

woork_book = openpyxl.load_workbook('h.w.20.xlsx')

sheet = woork_book.active
print(sheet)

rows = sheet.max_row
cols = sheet.max_column

id_new = []
for item in range(1,2):
  for val in range(1,rows + 1):
    cell = sheet.cell(row=val, column=item)
    id_new.append(cell.value)
name_new = []
for item in range(2,3):
  for val in range(1,rows + 1):
    cell = sheet.cell(row=val, column=item)
    name_new.append(cell.value)
phone_new = []
for item in range(3,4):
  for val in range(1,rows + 1):
    cell = sheet.cell(row=val, column=item)
    phone_new.append(cell.value)

new_list = []
new_list.append(id_new)
new_list.append(name_new)
new_list.append(phone_new)


for row_id, row in enumerate(new_list):
  for col_id, value in enumerate(row):
    cell = sheet.cell(row=row_id + 1, column=col_id + 1)
    cell.value = value

woork_book.save('h.w.20+.xlsx')


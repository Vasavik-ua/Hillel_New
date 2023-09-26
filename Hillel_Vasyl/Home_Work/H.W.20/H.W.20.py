import openpyxl
import csv


with open('h.m.19.csv', mode='r', encoding='utf-8') as f:
  reader = csv.reader(f, delimiter=',')
  new_data = []
  for item in reader:
    new_data.append(item)

#print(new_data)

def saerch_val(val):  # val = search element.
  for item in range(len(new_data)):
    for value in range(len(new_data[item])):
      if new_data[item][value].lower() == val.lower():
        return value


 y = saerch_val('age')

def delete_serch(val, array_data):
  for item in array_data:
    for value in item:
      delete_items = value.pop(val)
  return array_data

print(delete_serch())

import openpyxl
import csv


with open('h.m.19.csv', mode='r', encoding='utf-8') as f:
  reader = csv.reader(f, delimiter=',')
  new_data = []
  for item in reader:
    new_data.append(item)

print(new_data)


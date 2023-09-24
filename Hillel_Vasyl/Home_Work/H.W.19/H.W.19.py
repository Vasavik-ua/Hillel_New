import csv
import json

with open('h.w.18.json') as y:
    json_data = json.load(y)
    print(type(json_data))
    print(json_data)
first_row = ["ID", "Name", "Age", "Phone"]
new_list = list(json_data.items())
row1 = [new_list[0][0], new_list[0][1][0], new_list[0][1][1]]
row2 = [new_list[1][0], new_list[1][1][0], new_list[1][1][1]]
row3 = [new_list[2][0], new_list[2][1][0], new_list[2][1][1]]
row4 = [new_list[3][0], new_list[3][1][0], new_list[3][1][1]]
row5 = [new_list[4][0], new_list[4][1][0], new_list[4][1][1]]

with open('h.m.19.csv', 'w', encoding='utf-8') as f:
    file_new = csv.writer(f, delimiter=',')
    for item in (first_row, row1, row2, row3, row4, row5):
        file_new.writerow(item)




import csv
import json
import random

with open('h.w.18.json') as y:
    json_data = json.load(y)


def cre_new(x):
    g = list(x.items())
    w = []
    for i in (range(len(g))):
        h = [g[i][0], g[i][1][0], g[i][1][1]]
        w.append(h)
    return w


def rand_oper():
    my_list = ['095', '066', '098', '096', '050', '097']
    new_val = random.choice(my_list)
    num_req = 7
    for val in range(num_req):
        last = random.randint(0, 9)
        new_val += (str(last))
    return new_val


first_row = [["ID", "Name", "Age", "Phone"]]
new_list = cre_new(json_data)

with open('h.m.19.csv', 'w', encoding='utf-8') as f:
    file_new = csv.writer(f, delimiter=',')
    for item in first_row:
        file_new.writerow(item)
    for item in new_list:
        file_new.writerow(item)

import csv
import json
import random

with open('h.w.18.json') as y:
    json_data = json.load(y)


def rand_oper():
    my_list = ['095', '066', '098', '096', '050', '097']
    new_val = random.choice(my_list)
    num_req = 7
    for val in range(num_req):
        last = random.randint(0, 9)
        new_val += (str(last))
    return new_val


def prob_75(leng, prob):  # X: lenght; y: probality.
    array_new = []
    per_75 = leng - (round(leng * (prob/100)))
    for item in range(leng):
        array_new.append(rand_oper())
    for val in range(per_75):
        sost_val = random.randint(0, leng-1)
        array_new[sost_val] = ''
        return array_new


def cre_new_list(x):
    json_list = list(x.items())
    return_ls = []
    rand_val = prob_75(len(json_list), 75)
    for i in (range(len(json_list))):
        h = [json_list[i][0], json_list[i][1][0], json_list[i][1][1], rand_val[i]]
        return_ls.append(h)
    return return_ls


def main():
    first_row = [["ID", "Name", "Age", "Phone"]]
    new_list = cre_new_list(json_data)
    print(new_list)

    with open('h.m.19.csv', 'w', newline='', encoding='utf-8') as f:
        file_new = csv.writer(f, delimiter=',', lineterminator='\n')
        for item in first_row:
            file_new.writerow(item)
        for item in new_list:
            file_new.writerow(item)


main()

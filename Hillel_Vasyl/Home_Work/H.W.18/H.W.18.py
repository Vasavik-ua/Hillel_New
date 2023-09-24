import json

dict_new = {
    "100000": ('Basil', 3),
    "100001": ('Ron', 14),
    "100002": ('Harry', 15),
    "100003": ('Draco', 13),
    "100004": ('Vlad', 18)
}

with open('h.w.18.json', 'w') as f:
    json.dump(dict_new, f)


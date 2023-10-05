from datetime import date

def sum_age(data):  # Insert the date
    dat = date.today()
    dat_t = dat.strftime("%d/%m/%Y")
    sym_v = ''
    for val in dat_t:
        if not val.isdigit():
            sym_v += val
            break
    dat_new = dat_t.split(sym_v)
    sym_val = ''
    for val in data:
        if not val.isdigit():
            sym_val += val
            break
    new_l = data.split(sym_val)
    age = int(dat_new[2]) - int(new_l[2])
    if (int(dat_new[0])+int(dat_new[1])) < (int(new_l[0])+int(new_l[1])):
        age -= 1
    return age

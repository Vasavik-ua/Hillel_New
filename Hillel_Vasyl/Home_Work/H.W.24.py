class Mystr(str):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        new_add = ''
        new_add += str(self.val)
        new_add += str(other)
        return new_add

    def __sub__(self, other):
        sl_val = str(self.val)
        ot_val = str(other)
        return sl_val.replace(ot_val, '', 1)

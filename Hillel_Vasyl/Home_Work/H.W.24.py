class Mystr(str):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return super().__add__(other)

    def __sub__(self, other):
        str_x = str(self.val)
        str1_x = str(other.val)
        result = str_x.replace(str1_x, '', 1)
        return result

    def __str__(self):
        return f"""'{self.val}'"""

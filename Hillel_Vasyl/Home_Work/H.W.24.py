class Mystr(str):
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return super().__add__(other)



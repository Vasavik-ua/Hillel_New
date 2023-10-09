from math import sqrt


class Calculator:
    def __init__(self, x):
        self.x = x

    def __truediv__(self, other):
        try:
            r = self.x / other.x
            return r
        except ZeroDivisionError:
            return 'You cannot divide for 0 '
        except (ValueError, TypeError):
            return 'You must insert only int number'

    def __add__(self, other):
        try:
            r = int(self.x) + int(other.x)
            return r
        except ValueError:
            return 'You must insert only int number'

    def __sub__(self, other):
        try:
            r = int(self.x) - int(other.x)
            return r
        except ValueError:
            return 'You must insert only int number'

    def __mul__(self, other):
        try:
            r = int(self.x) * int(other.x)
            return r
        except ValueError:
            return 'You must insert only int number'

    def __pow__(self, power):
        try:
            if int(power.x) < 0:
                raise Mynewtyperror
            else:
                x = self.x ** power.x
                return x
        except Mynewtyperror:
            return 'Provide to int number'

    def sqrt(self):
        try:
            y = sqrt(self.x)
            return y
        except ValueError:
            return 'You cannot input 0 or negative'
        except TypeError:
            return 'Provide to int number'

    def __str__(self):
        pass


class Mynewtyperror(Exception):
    pass

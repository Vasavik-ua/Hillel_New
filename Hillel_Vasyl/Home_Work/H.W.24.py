class Mystr(str):
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return super().__add__(other)


    def __sub__(self, other):
        y = str(self.x)
        r = str(other.x)
        w = y.replace(r, '', 1)
        return w

a = Mystr([1,2,3,4])
b = Mystr(3)
c = a - b
print(type(c))
print(c)

#tring('New bala7nce') - 7               ->    'New balance'
#String('New balance') - 'bal'            ->    'New ance'
#String('New balance') - 'Bal'            ->    'New balance'
#String('pineapple apple pine') - 'apple' ->    'pine apple pine'
#String('New balance') - 'apple'          ->    'New balance'
#String('NoneType') - None                ->    'Type'
#String(55678345672) - 7                  ->    '5568345672'

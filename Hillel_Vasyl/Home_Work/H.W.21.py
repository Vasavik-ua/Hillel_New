class Auto:
    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.color = 'blue'
        self.mark = mark
        self.weight = 3000

    def move(self):
        print('Move')

    def birthday(self):
        self.age += 1

    def stop(self):
        print('Stop')


auto_new = Auto('Audi ', 5, 'A4')

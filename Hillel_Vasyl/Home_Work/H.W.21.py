class Auto:
    def __init__(self, brand, age, mark, color='blue', weight=3000):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('Move')

    def birthday(self):
        self.age += 1

    def stop(self):
        print('Stop')

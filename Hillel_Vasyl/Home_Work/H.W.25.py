class Car:
    FUEL_TYPES = ['бензин', 'дизель', 'електрика', 'гібрид']
    COLORS = []
    NUMBER_OF_CARS = 0

    def __init__(self, model, year, fuel_type, color, number=0):
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type
        self.number = number
        Car.NUMBER_OF_CARS += 1
        Car.COLORS.append(self.color) if self.color not in Car.COLORS else ...
        self.number = Car.NUMBER_OF_CARS
        self.fuel_type = Car.is_valid_fuel_type(self)

    @staticmethod
    def is_valid_fuel_type(self):
        if self.fuel_type in Car.FUEL_TYPES:
            return self.fuel_type
        else:
            self.fuel_type = Car.FUEL_TYPES[0]
            return self.fuel_type

    def __str__(self):
        return f'{self.model}, {self.year}, {self.fuel_type}, {self.color}'

    @property
    def numbers(self):
        return f'{self.number} from {Car.NUMBER_OF_CARS} '

    @staticmethod
    def get_used_colors():
        return len(Car.COLORS)

    @staticmethod
    def get_number_of_cars():
        return Car.NUMBER_OF_CARS


car_1 = Car('Zaz', 1979, 'дизель', 'black')

car_2 = Car('BMW', 2000, 'бензин', 'red')

car_3 = Car('VOLVO', 2012, 'електрикаcccc', 'black')

car_4 = Car('Mersedes', 2012, 'гібрид', 'black')

print('COLORS:', Car.get_used_colors())

print('NUMBER_OF_CARS:', Car.get_number_of_cars())

for item in (car_1, car_2, car_3, car_4):

    print('item:', item)

    print('numbers:', item.numbers)

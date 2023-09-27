import time


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


class Truck(Auto):
    def __init__(self, brand, age, mark, color, weight, max_load=4000):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('Attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, color, weight, max_speed=200):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'Max speed is {self.max_speed}')


truck_1 = Truck('Volvo', 5, 'Trucks', 'black', 3560, 5000)
truck_2 = Truck('Mercedes', 5, 'Astros', 'purlple', 3400, 4990)
super_car1 = Car('Ferrari', 0, 'F150', 'red', 2900, 250)
super_car2 = Car('Lambo', 0, 'Cirono', 'green', 2800, 300)

print(f'Name of first Truck brand: {truck_1.brand}')
print(f'Name of first Truck age: {truck_1.age}')
print(f'Name of first Truck color: {truck_1.color}')
print(f'Name of first Truck mark: {truck_1.mark}')
print(f'Name of first Truck weight: {truck_1.weight}')
print(f'Name of first Truck max load: {truck_1.max_load}')
truck_1.move()
truck_1.stop()
truck_1.birthday()
print(f'Age of first Truck after birthday: {truck_1.age}')
truck_1.load()

print(f'Name of second Truck brand: {truck_2.brand}')
print(f'Name of second Truck age: {truck_2.age}')
print(f'Name of second Truck color: {truck_2.color}')
print(f'Name of second Truck mark: {truck_2.mark}')
print(f'Name of second Truck weight: {truck_2.weight}')
print(f'Name of second Truck max load: {truck_2.max_load}')
truck_2.move()
truck_2.stop()
truck_2.birthday()
print(f'Age of ssecond Truck after birthday: {truck_2.age}')
truck_2.load()

print(f'Name of first Car brand: {super_car1.brand}')
print(f'Name of first Car age: {super_car1.age}')
print(f'Name of first Car color: {super_car1.color}')
print(f'Name of first Car mark: {super_car1.mark}')
print(f'Name of first Car weight: {super_car1.weight}')
print(f'Name of first Car max speed: {super_car1.max_speed}')
super_car1.move()
super_car1.birthday()
print(f'Age of first Car after birthday: {super_car1.age}')
super_car1.stop()

print(f'Name of second Car brand: {super_car2.brand}')
print(f'Name of second Car age: {super_car2.age}')
print(f'Name of second Car color: {super_car2.color}')
print(f'Name of second Car mark: {super_car2.mark}')
print(f'Name of second Car weight: {super_car2.weight}')
print(f'Name of second Car max speed: {super_car2.max_speed}')
super_car2.move()
super_car2.birthday()
print(f'Age of second Car after birthday: {super_car2.age}')
super_car2.stop()

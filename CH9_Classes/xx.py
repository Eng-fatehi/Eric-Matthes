''' A simple attempt to represents a car. '''
class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.odometer_reading = 0
   
    def get_descriptive_name(self):
        long_name = f"{self.model} {self.make} {self.year}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it. ")

my_car = Car('toyota', 'ak', 2022)
print(my_car.get_descriptive_name())

class ElectricCar(Car):
    def __init__(self, year, make, model):
        super().__init__(year, make, model)

your_car =ElectricCar('nissan', 'leaf', 2023)
print(your_car.get_descriptive_name())
#my_car.odometer_reading = 33
#my_car.read_odometer()


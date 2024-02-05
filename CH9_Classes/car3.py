''' Setting a default value for an attribute. '''
# Incrementing an attribute's value through a method.
''' A simple attempt to represent a car. '''
class Car:
    def __init__(self, make, model, year):  # parameter
        # Initialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name.
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        # Print statement showing the car's mileage.
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        # Set the odometer reading to the given value.
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        # Add the given amount to the odometer reading.
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()


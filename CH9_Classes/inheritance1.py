''' Attributes and methods for the Child Class. '''


class Car:
    """ A simple attempt to represent a car. """
    def __init__(self, year, make, model):
        ''' Initailize attributes to describe a car. '''
        self.year = year
        self.make = make
        self.model = model
        self.odometer_reading = 0
    def get_descriptive_name (self):
        ''' Return a neatly formatted descriptive name. '''
        long_name = f"{self.year} {self.make} {self.model}."
        return long_name.title()
    def read_odometer (self):
        ''' Print statement showing the car's mileage. '''
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def increment_odometer(self, miles):
        ''' Add the given amount to the omdometer reading. '''
        self.odometer_reading += miles

my_car = Car('toyota', 'k4', 2024)
print(my_car.get_descriptive_name())


class ElectricCar(Car):   # Inheritance
    def __init__(self, year, make, model):
        ''' Initialize attributes of the parent class. 
            Then initailize attributes specific to an electric car. '''
        super().__init__(year, make, model)
        self.battery_size = 40      ####

    def describe_battery(self):     ####
        ''' Print statement describing the battery size. '''
        print(f"This car has a {self.battery_size}-KWh battery.")

your_car = ElectricCar('nissan', 'leaf', 2024)
print(your_car.get_descriptive_name())
your_car.describe_battery()        ####




''' A simple attempt to model a dog. '''

class Dog: 
    def __init__(self, name, age):
        self.name = name    # attributes
        self.age = age      #attributes

    def sit(self):          # methods (functions)           
        print(f"{self.name} is now sitting.")

    def roll_over(self):    # methods (functions)       
        print(f"{self.name} rolled over! ")

my_dog = Dog('Willie',6)   # The first object is (my_dog) from the generale class (Dog).
your_dog = Dog('Lucy', 3)  # The second object is (your_dog) also from the generale class (Dog).

print(f"\nMy dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()

# Class is consisting of methods and attributes.
# Object is an instance of a class.
# Method an action that a class or object could take.
# Attributes a descriptor or characteristic, Ex. name, color.
# Dot notation (.) is used to demonstrates how Python finds an attribute's value.
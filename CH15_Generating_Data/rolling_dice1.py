'''
Python range() returns the sequence of numbers starting from a given start integer to a stop integer,
which we can iterate(تكرارها) using a for loop.'''

'''
The randint() method in Python returns a random integer value
 between the two lower and higher limits (the specified range).
'''
from random import randint 
class Die:
    ''' A class representing a single die. '''
    def __init__(self, num_sides=6):
        ''' Assume a six-sided die. '''
        self.num_sides = num_sides

    def roll(self):
        ''' Return a random value between 1 and number of sides. '''
        return randint(1, self.num_sides)  #  returns a random integer value between 1 and 6. 
    
# Make some rolls, and store results in a list.

for roll_num in range(10):   # We iterate(تكرارها) 10 times by using range() function with a for loop.
    result = Die().roll()
    print(result)
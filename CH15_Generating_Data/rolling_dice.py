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
    
# Create a D6.
die = Die()
# Make some rolls, and store results in a list.
results = []
for roll_num in range(100):  # We roll the die 6 times.
    result = die.roll()      # استدعاء الناتج العشوائي
    results.append(result) # store the result of each roll in the list results.
print(results)

# Analyze the results.
frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency =results.count(value)
    frequencies.append(frequency)

print(frequencies)
'''
# import random module and plotly.express module.
from random import randint 
import plotly.express as px

# Make a class Die with one attribute called num_sides.
class Die:
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

# Define roll() method that returns a random value between 1 and number of sides.
    def roll(self):
        return randint(1,self.num_sides)
    
# Make some rolls, and store results in a list.
die = Die()
results= []
for roll_num in range(20):
    result = die.roll()
    results.append(result)
print(results)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1)   # poos_results (possible results)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# Visualize the results.
title = "Results of rolling one D6 10 times."
labels = {'x': 'Result', 'y': 'Freqyency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title=title, labels=labels)
fig.show()

'''
# Python crash course\CH15 Generating Data\ Rolling Dice with Plotly
# Import random module and plotly.express module.
from random import randint
import plotly.express as px

# Make a class Die with one attribute called num_sides.
class Die: 
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

# Define roll() method that returns a random value between 1 and number of sides.
    def roll(self):
        return randint (1, self.num_sides)
    
# Make some rolls, and store results in a list.
die = Die()
results = []
for roll_num in range(10):
    result = die.roll()
    results.append(result)
print(results)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# Visualize the results.
title = "Results of rolling one D6 10 times."
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()


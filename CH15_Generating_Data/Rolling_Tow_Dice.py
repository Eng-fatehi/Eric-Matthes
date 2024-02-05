'''
# Rolling Tow Dice 
# Import random module and plotly.express module.
from random import randint
import plotly.express as px

# Make a class Die with one attribute called num_sides.
class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    # Define roll() method that returns a random value between 1 and number of sides.
    def roll(self):
        return randint(1, self.num_sides)
    
# Create tow dice.   
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
print(results)

# Analyze the results.
frequencies = []
max_reslults = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_reslults+1)
for value in poss_results:
    freuency = results.count(value)
    frequencies.append(freuency)
print(frequencies)

# Visualize the results.
title = "Results of Rolling Two D6 Dice 1000 times."
Labels = {'x': 'Result', 'y': 'Frequency of Result'}  # Dictionary of Labels قاموس التسميات
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=Labels)
fig.show()

'''

# Rolling Tow Dice 
# Import random module and plotly.express module.
from random import randint
import plotly.express as px

# Make a class Die with one attribute called num_sides.
class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    # Define roll() method that returns a random value between 1 and number of sides.
    def roll(self):
        return randint(1, self.num_sides)
    
# Create tow dice.   
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
print(results)

# Analyze the results.
frequencies = []
max_reslults = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_reslults+1)
for value in poss_results:
    freuency = results.count(value)
    frequencies.append(freuency)
print(frequencies)

# Visualize the results.
title = "Results of Rolling Two D6 Dice 1000 times."
Labels = {'x': 'Result', 'y': 'Frequency of Result'}  # Dictionary of Labels قاموس التسميات
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=Labels)
fig.show()

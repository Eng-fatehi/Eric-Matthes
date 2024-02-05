
''' A list of Dictionaries.'''

# Nesting is store data in a list of dictionaries (multiple dictionaries in a list)

# Create three dicionaries representing a different alien.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# Store these dicionaries in a list.
aliens = [alien_0, alien_1, alien_2]

# loop through the list and print each alien.
for alien in aliens: 
    print(alien)